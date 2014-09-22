from __future__ import unicode_literals

import datetime
import logging
import re


from django.template.loader import render_to_string
from django.utils.encoding import force_text

from .conf import settings

logger = logging.getLogger('responsive')


class ResponsiveMiddleware(object):

    def process_request(self, request):
        responsive_cookie = request.COOKIES.get(settings.RESPONSIVE_COOKIE_NAME, None)
        if responsive_cookie:
            parts = responsive_cookie.split(':')
            if len(parts) != 3:
                logger.error(
                    'InvalidCookie: Something went wrong while decoding responsive cookie.')
                return

            try:
                width, height, pixelratio = parts
                width, height, pixelratio = int(width), int(height), float(pixelratio)
            except ValueError:
                logger.error(
                    'ValueError: Something went wrong while decoding responsive cookie.')
                return

            print width, height, pixelratio

    def process_response(self, request, response):
        html_types = ('text/html', 'application/xhtml+xml')
        content_type = response.get('Content-Type', '').split(';')[0]
        content_encoding = response.get('Content-Encoding', '')
        if any((getattr(response, 'streaming', False),
                'gzip' in content_encoding,
                content_type not in html_types)):
            return response

        if settings.RESPONSIVE_COOKIE_NAME not in request.COOKIES:
            expires = datetime.datetime.utcnow() + \
                datetime.timedelta(days=settings.RESPONSIVE_COOKIE_AGE)
            snippet = render_to_string('responsive/snippet.html', {
                'cookie_name': settings.RESPONSIVE_COOKIE_NAME,
                'cookie_age': 60 * 60 * 24 * settings.RESPONSIVE_COOKIE_AGE,  # convert to secs
                'cookie_expires': expires.strftime('%a, %d %b %Y %H:%M:%S GMT')
            })
            pattern = re.compile(b'<head>', re.IGNORECASE)
            response.content = pattern.sub(b'<head>' + snippet, force_text(response.content))

        if response.get('Content-Length', None):
            response['Content-Length'] = len(response.content)
        return response
