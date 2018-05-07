"""
Block definitions for generic column blocks.
"""

from django import forms
from django.apps import apps
from django.contrib.staticfiles.templatetags.staticfiles import static

from wagtail.core import blocks


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
                CommonBlocks(),
                ratios=(1, 1),
                label="Two halves",
                group="Columns",
            )
            column_2_1 = ColumnsBlock(
                CommonBlocks(),
                ratios=(2, 1),
                label="Two thirds/One third",
                group="Columns",
            )
            column_1_1_1 = ColumnsBlock(
                CommonBlocks(),
                ratios=(1, 1, 1),
                label="Three thirds",
                group="Columns",
            )


        class AllBlocks(ColumnBlocks, CommonBlocks):
            pass

    :param childblocks: the blocks that can be used with the columns
    :param ratios: the ratios of each columns relative to each other
    :param **kwargs: additional block configuration
    """

    def __init__(self, childblocks, ratios=(1, 1), **kwargs):
        super().__init__([
            ('column_%i' % index, childblocks)
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
        return super().media + forms.Media(css={
            'all': ('wagtailcolumnblocks/columns.css',),
        })
