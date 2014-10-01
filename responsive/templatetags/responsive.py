from __future__ import unicode_literals

from django.core.exceptions import ImproperlyConfigured
from django.template.base import (Library, Node, TemplateSyntaxError, Variable,
                                  VariableDoesNotExist)

from ..conf import settings

register = Library()


@register.tag('renderblockif')
def renderblock_if(parser, token):

    request_context = 'django.core.context_processors.request'
    if request_context not in settings.TEMPLATE_CONTEXT_PROCESSORS:
        raise ImproperlyConfigured(
            "You must enable 'django.core.context_processors.request' "
            "in TEMPLATE_CONTEXT_PROCESSORS")

    responsive_middleware = 'responsive.middleware.ResponsiveMiddleware'
    if responsive_middleware not in settings.MIDDLEWARE_CLASSES:
        raise ImproperlyConfigured(
            "'renderblockif' tag requires the responsive middleware to "
            "be installed.  Edit your MIDDLEWARE_CLASSES setting to insert"
            "the 'responsive.middleware.ResponsiveMiddleware'")

    media_queries = token.split_contents()[1:]
    if not media_queries:
        raise TemplateSyntaxError(
            "'renderblockif' tag requires one or more "
            "RESPONSIVE_MEDIA_QUERIES as argument.")

    nodelist = parser.parse(('renderblockelif', 'renderblockelse', 'endrenderblockif'))
    conditions_nodelists = [(media_queries, nodelist)]
    token = parser.next_token()

    # {% renderblockelif ... %} (repeatable)
    while token.contents.startswith('renderblockelif'):
        media_queries = token.split_contents()[1:]
        if not media_queries:
            raise TemplateSyntaxError(
                "'renderblockif' tag requires one or more "
                "RESPONSIVE_MEDIA_QUERIES as argument.")
        nodelist = parser.parse(('renderblockelif', 'renderblockelse', 'endrenderblockif'))
        conditions_nodelists.append((media_queries, nodelist))
        token = parser.next_token()

    # {% renderblockelse %} (optional)
    if token.contents == 'renderblockelse':
        nodelist = parser.parse(('endrenderblockif',))
        conditions_nodelists.append((None, nodelist))
        token = parser.next_token()

    # {% endrenderblockif %}
    assert token.contents == 'endrenderblockif'

    return RenderBlockIfNode(conditions_nodelists)


class RenderBlockIfNode(Node):

    def __init__(self, conditions_nodelists):
        self.conditions_nodelists = conditions_nodelists

    def render(self, context):
        request = context.get('request', None)

        if request and hasattr(request, 'device'):
            for conditions, nodelist in self.conditions_nodelists:
                if conditions is not None:   # renderblockif / renderblockelif clause
                    to_be_matched = []
                    for media_query in conditions:
                        if not (media_query[0] == media_query[-1]
                                and media_query[0] in ('"', "'")):
                            try:
                                media_query = Variable(media_query).resolve(context)
                            except VariableDoesNotExist:
                                continue
                        else:
                            media_query = media_query[1:-1]

                        to_be_matched.append(media_query)
                        match = len(set(request.device.matched).intersection(to_be_matched)) > 0
                else:  # renderblockelse clause
                    match = True

                if match:
                    return nodelist.render(context)

        return ''
