=============================
django-responsive2
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

Why would you use django-responsive2?
-------------------------------------

This project was inspired by Twitter Bootstrap's `Responsive Utilities <http://getbootstrap.com/css/#responsive-utilities>`_.

Bootstrap provides some handful helper classes, for faster mobile-friendly development.

These can be used for showing and hiding content by device via media query combined with large, small, and medium devices.

More Information: http://getbootstrap.com/css/#responsive-utilities

Similarly ``django-responsive2`` can be used to render different content based on device screen sizes and pixel ratios.

It’s best explained through examples.


**Sample template**::

    <div class="container">
        <div class="row">
            {% if device.is_xsmall or device.is_small %}
                <div class="col-sm">
                    Visible on x-small/small
                </div>
            {% elif device.is_medium %}
                <div class="col-md">
                    Visible on medium screens
                </div>
            {% else %}
                <div class="col-lg">
                    Visible on large/xlarge screens
                </div>
            {% endif %}
        </div>
    </div>

In this very simple example, `col-sm` will only be rendered for small screen devices
(e.g. an iPhone), `col-m` will be displayed for medium screen devices (e.g. an iPad)
and lastly `col-lg` will be visible for large screen devices or any devices that don't
match the rules for small/medium devices.

Configuration
-------------

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


Documentation
-------------

The full documentation is at https://django-responsive2.readthedocs.org.

