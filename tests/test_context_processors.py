#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase
from django.test.client import RequestFactory
from django.test.utils import override_settings

from responsive.conf import settings
from responsive.context_processors import device
from responsive.utils import Device


class ContextProcessorsTest(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_context_processor_raises_improperlyconfigured_error(self):
        # with responsive middleware not included in MIDDLEWARE_CLASSES
        # this should raise a ImproperlyConfigured error
        request = self.factory.get('/')
        self.assertRaises(ImproperlyConfigured, device, request)

    @override_settings(MIDDLEWARE_CLASSES=('responsive.middleware.ResponsiveMiddleware', ))
    def test_context_processor_returns_device_object(self):
        request = self.factory.get('/')
        context = device(request)
        self.assertIsInstance(context[settings.RESPONSIVE_VARIABLE_NAME], Device)
