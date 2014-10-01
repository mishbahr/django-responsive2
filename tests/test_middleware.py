#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test.client import RequestFactory

from responsive.middleware import ResponsiveMiddleware
from responsive.conf import settings
from responsive.utils import Device


from django.http import HttpResponse


def hello(request):
    html = """
        <html>
            <head>
                <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
            </head>
            <body>

            </body>
        </html>
    """
    return HttpResponse(html)


class MiddlewareTest(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.middleware = ResponsiveMiddleware()

    def test_process_request_with_valid_cookie(self):
        # test given a valid responsive cookie, device obj is set on request
        request = self.factory.get('/')
        request.COOKIES = {
            settings.RESPONSIVE_COOKIE_NAME: '1024:768:2'  # valid responsive cookie
        }

        self.middleware.process_request(request)
        self.assertIsInstance(getattr(request, settings.RESPONSIVE_VARIABLE_NAME), Device)

    def test_process_request_with_a_bad_cookie(self):
        # test given a bad responsive cookie, an INVALID_RESPONSIVE_COOKIE flag is set
        request = self.factory.get('/')
        request.COOKIES = {
            settings.RESPONSIVE_COOKIE_NAME: 'xxx:xxx:x'  # cookie values should be numbers
        }

        self.middleware.process_request(request)
        self.assertTrue(getattr(request, 'INVALID_RESPONSIVE_COOKIE'))

        request.COOKIES = {
            settings.RESPONSIVE_COOKIE_NAME: 'xxxxxxx'  # 3 parts to a responsive cookie
        }

        self.middleware.process_request(request)
        self.assertTrue(getattr(request, 'INVALID_RESPONSIVE_COOKIE'))

    def test_reposnsive_htnl_snippet_is_injected_into_response(self):
        request = self.factory.get('/')
        response = hello(request)
        # test no <script> tag before any processing by the middleware
        self.assertFalse(b'</script>' in response.content)
        processed_response = self.middleware.process_response(request, response)
        self.assertTrue(b'</script>' in processed_response.content)

    def test_snippet_is_not_injected_if_reponsive_cookie_already_exists(self):
        request = self.factory.get('/')
        request.COOKIES = {
            settings.RESPONSIVE_COOKIE_NAME: '1024:768:2'  # valid responsive cookie
        }
        response = hello(request)
        processed_response = self.middleware.process_response(request, response)
        self.assertFalse(b'</script>' in processed_response.content)

    def test_non_html_content_type(self):
        # Don't inject snippet if the content type is not html or xhtml.
        request = self.factory.get('/')
        response = HttpResponse({}, content_type='application/json')
        processed_response = self.middleware.process_response(request, response)
        self.assertNotIn(b'</script>', processed_response.content)

    def test_gzipped_html(self):
        # Don't insert if the content had been gzipped.
        request = self.factory.get('/')
        request.COOKIES = {
            settings.RESPONSIVE_COOKIE_NAME: '1024:768:2'  # valid responsive cookie
        }
        response = hello(request)
        processed_response = self.middleware.process_response(request, response)
        processed_response['Content-Encoding'] = 'gzip'
        self.assertFalse(b'</script>' in processed_response.content)
