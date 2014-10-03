========
Usage
========

``django-responsive2`` lets you to define the breakpoints at which your layout will change,
adapting to different screen sizes.  Here's the default breakpoints::

    RESPONSIVE_MEDIA_QUERIES = {
        'small': {
            'verbose_name': _('Small screens'),
            'min_width': None,
            'max_width': 640,
        },
        'medium': {
            'verbose_name': _('Medium screens'),
            'min_width': 641,
            'max_width': 1024,
        },
        'large': {
            'verbose_name': _('Large screens'),
            'min_width': 1025,
            'max_width': 1440,
        },
        'xlarge': {
            'verbose_name': _('XLarge screens'),
            'min_width': 1441,
            'max_width': 1920,
        },
        'xxlarge': {
            'verbose_name': _('XXLarge screens'),
            'min_width': 1921,
            'max_width': None,
        }
    }

** Borrowed from ZURB Foundation framework, see http://foundation.zurb.com/docs/media-queries.html

While there are several different items we can query on, the ones used for django-responsive2
are min-width, max-width, min-height and max-height.

* min_width — Rules applied for any device width over the value defined in the config.
* max_width — Rules applied for any device width under the value defined in the config.
* min_height — Rules applied for any device height over the value defined in the config.
* max_height — Rules applied for any device height under the value defined in the config.
* pixel_ratio — Rules applied for any device with devicePixelRatio defined in the config.

You can override the default media queries by defining own in your ``RESPONSIVE_MEDIA_QUERIES``
in your ``settings.py``. For example::

    RESPONSIVE_MEDIA_QUERIES = {
        'iphone': {
            'verbose_name': _('iPhone Retina'),
            'min_width': 320,
            'pixel_ratio': 2
        },
        ...
    }

For every media queries, the  ``device`` object will have a ``is_FOO`` attribute, where FOO
is the name of the media query. This attribute returns ``True/False``.

Continuing with the example ``RESPONSIVE_MEDIA_QUERIES`` settings above, here’s a simple corresponding template::

    <div class="container">
        <div class="row">
            {% if device.is_iphone %}
                {# this snippet will only be rendered for retina devices with min_width = 320 #}
                <div class="app-store">
                    <a href="#">Available on the App Store</a>
                </div>
            {% endif %}
        </div>
    </div>


