from django.conf import settings  # noqa
from django.utils.translation import ugettext_lazy as _

from appconf import AppConf


class ResponsiveAppConf(AppConf):
    """
    While there are several different items we can query on,
    the ones used for django-responsive2 are min-width and max-width

    min_width -- Rules applied for any device width over the value defined in the config.
    max_width -- Rules applied for any device width under the value defined in the config.
    pixel_ratio -- Rules applied for any device with devicePixelRatio defined in the config.

    Usage
    ------
        {% load 'responsive' %}

        {% renderblockif 'small' 'medium' %}
            [...]
        {% endrenderblockif %}

    """

    COOKIE_NAME = 'clientinfo'
    COOKIE_AGE = 365  # days

    # prefix for classes for showing and hiding content by device via media query
    CSS_VISIBLE_PREFIX = 'visible-'
    CSS_HIDDEN_PREFIX = 'hidden-'

    # Borrowed from ZURB Foundation framework.
    # See http://foundation.zurb.com/docs/media-queries.html
    MEDIA_QUERIES = {
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

    class Meta:
        prefix = 'responsive'
