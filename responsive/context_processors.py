from django.core.exceptions import ImproperlyConfigured

from .conf import settings
from .utils import Device


def device(request):
    responsive_middleware = 'responsive.middleware.ResponsiveMiddleware'
    if responsive_middleware not in settings.MIDDLEWARE_CLASSES:
        raise ImproperlyConfigured(
            "You must enable the 'ResponsiveMiddleware'. Edit your "
            "MIDDLEWARE_CLASSES setting to insert"
            "the 'responsive.middleware.ResponsiveMiddleware'")

    device_obj = getattr(request, settings.RESPONSIVE_VARIABLE_NAME, None)
    if not device_obj:
        device_obj = Device()

    return {
        settings.RESPONSIVE_VARIABLE_NAME: device_obj
    }
