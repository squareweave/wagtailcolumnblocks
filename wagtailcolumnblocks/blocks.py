"""
Block definitions for generic column blocks.
"""
import warnings

from django import forms
from django.apps import apps
from django.templatetags.static import static
from django.utils.html import format_html
from wagtail import VERSION as wagtail_version


if wagtail_version >= (5, 0):
    from wagtail import blocks, hooks
    hook_register_name = 'insert_global_admin_css'

else:
    from wagtail.core import blocks, hooks
    hook_register_name = 'insert_editor_css'


@hooks.register(hook_register_name)
def global_admin_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('wagtailcolumnblocks/columns.css')
    )


class ColumnsBlock(blocks.StructBlock):
    """
    A generic, reusable column block.

    Has one required argument, the child blocks that can be used within
    the columns. Pass ratios to specify a number of columns and their
    relative sizes in the admin.

    Due to the variations of responsive layouts and frontend layout frameworks,
    frontend templates should be overridden by the developer.

    Usage example::

        class CommonBlocks(blocks.StreamBlock):
            content = RichTextBlock(group="Common")
            image = ImageChooserBlock(group="Common")
            embed = EmbedBlock(group="Common")


        class ColumnBlocks(blocks.StreamBlock):
            column_1_1 = ColumnsBlock(
                CommonBlocks,
                # Two halves
                ratios=(1, 1),
                group="Columns",
            )
            column_2_1 = ColumnsBlock(
                CommonBlocks,
                # Two thirds/One third
                ratios=(2, 1),
                group="Columns",
            )
            column_1_1_1 = ColumnsBlock(
                CommonBlocks,
                # Three thirds
                ratios=(1, 1, 1),
                group="Columns",
            )


        class AllBlocks(ColumnBlocks, CommonBlocks):
            pass

    :param childblocks: the blocks that can be used with the columns
    :param ratios: the ratios of each columns relative to each other
    :param **kwargs: additional block configuration
    """

    def __init__(self, childblocks, ratios=(1, 1), **kwargs):
        if not callable(childblocks):
            childblocks_instance = childblocks
            childblocks = lambda: childblocks_instance
            warnings.warn(
                'Using instance as `childblocks` argument for `ColumnsBlock` has been deprecated. Use class instead.',
                category=DeprecationWarning,
            )
        super().__init__([
            ('column_%i' % index, childblocks())
            for index, _ in enumerate(ratios)
        ], **kwargs)
        self.ratios = ratios

    def get_column_widths(self):
        """Calculate the column widths as shares of the grid width."""
        multiplier = self.meta.grid_width // sum(self.ratios)
        return [
            multiplier * ratio
            for ratio in self.ratios
        ]

    def get_form_context(self, *args, **kwargs):
        context = super().get_form_context(*args, **kwargs)
        children = context['children']
        context.update({
            'columns': zip(children.values(), self.ratios),
        })
        return context

    def get_context(self, value, **kwargs):
        context = super().get_context(value, **kwargs)
        context.update({
            'columns': zip(value.values(), self.get_column_widths()),
        })

        return context

    class Meta:
        form_classname = 'columns-block struct-block'
        form_template = 'block_forms/columnsblock.html'
        template = 'blocks/columnsblock.html'

        grid_width = 12  # 12 columns in the grid

        if apps.is_installed('wagtailfontawesome'):
            icon = 'fa-columns'

    @property
    def media(self):
        # Wagtail <2.13
        return super().media + forms.Media(css={
            'all': ('wagtailcolumnblocks/columns.css',),
        })

