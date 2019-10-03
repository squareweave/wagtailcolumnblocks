A generic, reusable column block for Wagtail's StreamField.

Allows developers to create column layouts with a number of different layout
ratios that are supported in the admin in a visually appealing way.

![Admin interface showing column blocks in a streamfield](/docs/admin.png?raw=true)

A basic frontend template is included, but no frontend CSS. Due to the
variations of responsive layouts and frontend layout frameworks,
frontend templates should be overridden by the developer.

Installation
------------

Once you have set up Wagtail, you should just need to do the following:

1. pip install wagtailcolumnblocks
2. Edit INSTALLED\_APPS in your settings.py to include 'wagtailcolumnblocks'.

Usage Example
-------------

Assuming you have set up Wagtail according to [these instructions](https://wagtail.io/developers/) (and those above), you can see wagtailcolumnblocks in action as follows.

Edit home/models.py to look like this. HomePage is from the original templated code, and we've added SidebarPage and the \*Blocks classes:

```python
from django.db import models

from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core import fields
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtailcolumnblocks.blocks import ColumnsBlock


class MyContentBlocks(blocks.StreamBlock):
    """
    The blocks you want to allow within each MyColumnBlocks column.
    """

    image = ImageChooserBlock()
    text = blocks.CharBlock()


class MyColumnBlocks(blocks.StreamBlock):
    """
    All the root level blocks you can use
    """
    column_2_1 = ColumnsBlock(
        # Blocks you want to allow within each column
        MyContentBlocks(),
        # Two columns in admin, first twice as wide as the second
        ratios=(2, 1),
        # Used for grouping related fields in the streamfield field picker
        group="Columns",
        # 12 column frontend grid (this is the default, so can be omitted)
        grid_width=12,
        # Override the frontend template
        template='home/blocks/two_column_block.html',
    )


class SidebarPage(Page):
    content = fields.StreamField(MyColumnBlocks)

    content_panels = [
        FieldPanel('title'),
        StreamFieldPanel('content')
    ]

class HomePage(Page):
    pass
```

Edit `home/templates/home/sidebar_page.html` to look like this:
```html
{% extends "base.html" %}
{% load static %}
{% load wagtailcore_tags %}

{% block content %}
<div class="row">
    {{page.content}}
</div>
{% endblock content %}
```

Edit `home/templates/home/blocks/two_column_block.html` to look like this:
```html
{% load wagtailcore_tags %}

<div class="row">
    {% for column, width in columns %}
        <div class="col-xs-12 col-md-6">
            Column width = {{ width }}
            {% include_block column %}
        </div>
    {% endfor %}
</div>
```

Run `python manage.py makemigrations && python manage.py migrate` to add our SidebarPage migration and execute it.

In the Wagtail admin you should now be able to create a Sidebar page which shows up in a two column layout. When you view or preview the page you should see the templated content.

License
-------

Licensed under the BSD 3-clause "New" or "Revised" License.

(c) 2019, Squareweave. All rights reserved.
