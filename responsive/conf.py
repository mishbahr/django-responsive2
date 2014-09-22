from django.conf import settings  # noqa
from django.utils.translation import ugettext_lazy as _

from appconf import AppConf


class ResponsiveAppConf(AppConf):
    """
    While there are several different items we can query on,
    the ones used for django-responsive2 are min-width and max-width

    min_width -- Rules applied for any device width over the value defined in the query.
    max_width -- Rules applied for any device width under the value defined in the query.

    Usage
    ------
        {% load 'responsive' %}

        {% renderblockif 'small' 'medium' %}
            [...]
        {% endrenderblockif %}

    """
    COOKIE_NAME = 'clientinfo'
    COOKIE_AGE = 365   # days

    # Borrowed from ZURB Foundation framework
    # See http://foundation.zurb.com/docs/media-queries.html

    BREAKPOINTS = {
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
