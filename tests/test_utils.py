#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.cache import cache
from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase
from django.test.client import RequestFactory
from django.test.utils import override_settings
from django.utils.translation import ugettext_lazy as _

from responsive.conf import settings
from responsive.utils import Device


class UtilsTest(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    # Implement assertIsNotNone for Python runtimes < 2.7 or < 3.1
    if not hasattr(TestCase, 'assertIsNotNone'):
        def assertIsNotNone(self, value, *args):
            self.assertNotEqual(value, None, *args)

    def test_device_obj_str(self):
        device = Device()
        self.assertEqual(str(device), 'Device :: width=0 height=0 pixel-ratio=1.0')

    def test_device_default_values(self):
        device = Device()
        self.assertEqual(device.width, settings.RESPONSIVE_DEFAULT_WIDTH)
        self.assertEqual(device.height, settings.RESPONSIVE_DEFAULT_HEIGHT)
        self.assertEqual(device.pixel_ratio, settings.RESPONSIVE_DEFAULT_PIXEL_RATIO)

    @override_settings(RESPONSIVE_MEDIA_QUERIES={
        'small': {
            'verbose_name': _('Small screens'),
            'min_width': 0,
            'max_width': '640px',
        },
    })
    def test_get_media_queries_fails(self):
        # get_media_queries() should raise ImproperlyConfigured with above settings
        device = Device()
        self.assertRaises(ImproperlyConfigured, device.get_media_queries)

    @override_settings(RESPONSIVE_MEDIA_QUERIES={
        'small': {
            'verbose_name': _('Small screens'),
            'max_width': 640,
        },
    })
    def test_get_media_queries_works(self):
        # min_width, min_height, max_height, pixel_ratio is not defined in above settings
        # get_media_queries() should set them to None
        device = Device()
        media_queries = device.get_media_queries()
        for attr in ('min_width', 'min_height', 'max_height', 'pixel_ratio'):
            self.assertEqual(media_queries['small'][attr], None)

    def test_caching(self):
        device = Device(width=1366, height=768)
        # matched devices should be cached
        self.assertIsNotNone(cache.get(device.cache_key))

        # clear the cache
        device.clear()
        self.assertIsNone(cache.get(device.cache_key))

    def test_matched_media_queries(self):
        device = Device(width=1366, height=768, pixel_ratio=2)
        self.assertIn('large', device.matched)
        self.assertIn('retina', device.matched)
