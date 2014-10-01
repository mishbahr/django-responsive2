=============================
django-responsive2 (WIP)
=============================

.. image:: http://img.shields.io/travis/mishbahr/django-responsive2.svg?style=flat-square
    :target: https://travis-ci.org/mishbahr/django-responsive2/

.. image:: http://img.shields.io/pypi/v/django-responsive2.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-responsive2/
    :alt: Latest Version

.. image:: http://img.shields.io/pypi/dm/django-responsive2.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-responsive2/
    :alt: Downloads

.. image:: http://img.shields.io/pypi/l/django-responsive2.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-responsive2/
    :alt: License

.. image:: http://img.shields.io/coveralls/mishbahr/django-responsive2.svg?style=flat-square
  :target: https://coveralls.io/r/mishbahr/django-responsive2?branch=master


django-responsive2 is an experimental Django project that gives web designers tools for building responsive websites. It can dynamically swap content based on breakpoints.

Features
--------

* TODO


Quickstart
----------

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

Usage
------

* TODO

Configuration
-------------

* TODO

Documentation
-------------

The full documentation is at https://django-responsive2.readthedocs.org.

