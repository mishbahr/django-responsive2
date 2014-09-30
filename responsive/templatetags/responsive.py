from __future__ import unicode_literals

from django.core.exceptions import ImproperlyConfigured
from django.template.base import (Library, Node, TemplateSyntaxError, Variable,
                                  VariableDoesNotExist)

from ..conf import settings

register = Library()


@register.tag('renderblockif')
def renderblock_if(parser, token):
    media_queries = token.contents.split()[1:]
    if not media_queries:
        raise TemplateSyntaxError(
            "'renderblockif' tag requires one or more "
            "RESPONSIVE_MEDIA_QUERIES as argument.")

    nodelist = parser.parse(('endrenderblockif',))
    parser.delete_first_token()
    return RenderBlockIfNode(media_queries, nodelist)


class RenderBlockIfNode(Node):

    def __init__(self, media_queries, nodelist):
        self.media_queries, self.nodelist = media_queries, nodelist

    def render(self, context):

        request_context = 'django.core.context_processors.request'
        if not request_context in settings.TEMPLATE_CONTEXT_PROCESSORS:
            raise ImproperlyConfigured(
                "You must enable 'django.core.context_processors.request' "
                "in TEMPLATE_CONTEXT_PROCESSORS")

        responsive_middleware = 'responsive.middleware.ResponsiveMiddleware'
        if not responsive_middleware in settings.MIDDLEWARE_CLASSES:
            raise ImproperlyConfigured(
                "'renderblockif' tag requires the responsive middleware to "
                "be installed.  Edit your MIDDLEWARE_CLASSES setting to insert"
                "the 'responsive.middleware.ResponsiveMiddleware'")

        request = context.get('request', None)

        if hasattr(request, 'device'):
            to_be_matched = []
            for media_query in self.media_queries:
                if not (media_query[0] == media_query[-1] and media_query[0] in ('"', "'")):
                    try:
                        media_query = Variable(media_query).resolve(context)
                    except VariableDoesNotExist:
                        continue
                else:
                    media_query = media_query[1:-1]

                to_be_matched.append(media_query)

            match = len(set(request.device.matched).intersection(to_be_matched)) > 0
            if match:
                return self.nodelist.render(context)

        return ''
