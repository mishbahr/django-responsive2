============
Installation
============

1. Install django-responsive2::

    pip install django-responsive2

2. Add ``responsive`` to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'responsive',
        ...
    )

3. Add ``django.core.context_processors.request``  and ``responsive.context_processors.device`` to your ``TEMPLATE_CONTEXT_PROCESSORS``::

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        'django.core.context_processors.request',
        'responsive.context_processors.device',
        ...
    )

4. Add the ``ResponsiveMiddleware`` to MIDDLEWARE_CLASSES::

    MIDDLEWARE_CLASSES = (
        ...
        'responsive.middleware.ResponsiveMiddleware',
        ...
    )

