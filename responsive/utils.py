import six

from django.core.cache import cache
from django.core.exceptions import ImproperlyConfigured

from .conf import settings


class Device(object):
    def __init__(self,
                 width=settings.RESPONSIVE_DEFAULT_WIDTH,
                 height=settings.RESPONSIVE_DEFAULT_HEIGHT,
                 pixel_ratio=settings.RESPONSIVE_DEFAULT_PIXEL_RATIO):

        self.width = int(width)
        self.height = int(height)
        self.pixel_ratio = float(pixel_ratio)
        self.matched = []

        self.cache_key = '%(prefix)s%(width)s_%(height)s_%(pixel_ratio)s' % {
            'prefix': settings.RESPONSIVE_CACHE_PREFIX,
            'width': self.width,
            'height': self.height,
            'pixel_ratio': self.pixel_ratio
        }
        matches = cache.get(self.cache_key, None)
        if not matches:
            matches = self.match_media_queries()
            cache.set(self.cache_key, matches, settings.RESPONSIVE_CACHE_DURATION)

        for name, value in six.iteritems(matches):
            setattr(self, 'is_%s' % name, value)
            if value is True:
                self.matched.append(name)

    def match_media_queries(self):
        matches = {}
        media_queries = self.get_media_queries()
        for alias, config in six.iteritems(media_queries):
            yesno = []
            if config['min_width']:
                yesno.append(self.width >= config['min_width'])
            if config['max_width']:
                yesno.append(self.width <= config['max_width'])
            if config['min_height']:
                yesno.append(self.height >= config['min_height'])
            if config['max_height']:
                yesno.append(self.height <= config['max_height'])
            if config['pixel_ratio']:
                yesno.append(self.pixel_ratio == config['pixel_ratio'])

            matches[alias] = all(yesno)
        return matches

    @staticmethod
    def get_media_queries():
        media_queries = settings.RESPONSIVE_MEDIA_QUERIES
        for name, config in six.iteritems(media_queries):
            for attr in ('min_width', 'max_width', 'min_height', 'max_height', 'pixel_ratio'):
                if attr not in config:
                    config[attr] = None
                elif config[attr] is not None:
                    try:
                        config[attr] = int(config[attr]) if attr != 'pixel_ratio' \
                            else float(config[attr])
                    except ValueError:
                        raise ImproperlyConfigured(
                            'RESPONSIVE_MEDIA_QUERIES - %s for %s breakpoint must '
                            'be a number.' % (attr, name))
                else:
                    media_queries[name][attr] = config[attr]
        return media_queries

    def clear(self):
        cache.delete(self.cache_key)

    def __str__(self):
        return 'Device :: width=%(width)s height=%(height)s pixel-ratio=%(pixel_ratio)s' % {
            'width': self.width,
            'height': self.height,
            'pixel_ratio': self.pixel_ratio
        }
