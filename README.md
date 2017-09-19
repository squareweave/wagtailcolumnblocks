A generic, reusable column block for Wagtail streamfields.

Allows developers to create column layouts with a number of different layout
ratios that are supported in the admin in a visually appealing way.

![Admin interface showing column blocks in a streamfield](/docs/admin.png?raw=true)

A basic frontend template is included, but no frontend CSS. Due to the
variations of responsive layouts and frontend layout frameworks,
frontend templates should be overridden by the developer.

Usage Example
-------------

```python
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
```

License
-------

Licensed under the BSD 3-clause "New" or "Revised" License.

(c) 2017, Squareweave. All rights reserved.