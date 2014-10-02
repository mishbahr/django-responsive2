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


django-responsive2 is an experimental Django project that gives web designers tools for building
responsive websites. It can dynamically swap content based on breakpoints.

Why would you use django-responsive2?
-------------------------------------

This project was inspired by Twitter Bootstrap's `Responsive Utilities <http://getbootstrap.com/css/#responsive-utilities>`_.

Bootstrap provides some handful helper classes, for faster mobile-friendly development. These
can be used for showing and hiding content by device via media query combined with large, small,
and medium devices.

More Information: http://getbootstrap.com/css/#responsive-utilities

Similarly ``django-responsive2`` can be used to render different content based on device
screen sizes and pixel ratios. It’s best explained through examples.


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

In this very simple example, ``col-sm`` will only be rendered for small screen devices
(e.g. an iPhone), ``col-m`` will be displayed for medium screen devices (e.g. an iPad)
and lastly ``col-lg`` will be visible for large screen devices or any devices that don't
match the rules for small/medium devices.

Configuration
-------------
``django-responsive2`` lets you to define the breakpoints at which your layout will change,
adapting to different screen sizes.  Here's the default breakpoints::

    RESPONSIVE_MEDIA_QUERIES = {
        'small': {
            'verbose_name': _('Small screens'),
            'min_width': None,
            'max_width': 640,
        },
        'medium': {
            'verbose_name': _('Medium screens'),
            'min_width': 641,
            'max_width': 1024,
        },
        'large': {
            'verbose_name': _('Large screens'),
            'min_width': 1025,
            'max_width': 1440,
        },
        'xlarge': {
            'verbose_name': _('XLarge screens'),
            'min_width': 1441,
            'max_width': 1920,
        },
        'xxlarge': {
            'verbose_name': _('XXLarge screens'),
            'min_width': 1921,
            'max_width': None,
        }
    }

** Borrowed from ZURB Foundation framework, see http://foundation.zurb.com/docs/media-queries.html

While there are several different items we can query on, the ones used for django-responsive2
are min-width, max-width, min-height and max-height.

* min_width — Rules applied for any device width over the value defined in the config.
* max_width — Rules applied for any device width under the value defined in the config.
* min_height — Rules applied for any device height over the value defined in the config.
* max_height — Rules applied for any device height under the value defined in the config.
* pixel_ratio — Rules applied for any device with devicePixelRatio defined in the config.

You can override the default media queries by defining own in your ``RESPONSIVE_MEDIA_QUERIES``
in your ``settings.py``. For example::

    RESPONSIVE_MEDIA_QUERIES = {
        'iphone': {
            'verbose_name': _('iPhone Retina'),
            'min_width': 320,   # mobile first queries
            'pixel_ratio': 2
        },
        ...
    }

For every media queries, the  `device` object will have a ``is_FOO`` attribute, where FOO
is the name of the media query. This attribute returns ``True/False``.

Continuing with the example ``RESPONSIVE_MEDIA_QUERIES`` settings above, here’s a simple corresponding template::

	<div class="container">
		<div class="row">
			{% if device.is_iphone %}
				<div class="app-store">
					<a href="https://itunes.apple.com/gb/app/yo./id834335592">Available on the App Store</a>
				</div>
			{% endif %}

			...

		</div>
	</div>

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

Credits
--------

This app started as a clone of ``django-responsive`` with some minor modifications to fit my own project requirements. So a big thank you to `@mlavin <https://github.com/mlavin>`_ for his hard work.

Shout out to `@jezdez <https://github.com/jezdez>`_ for the awesome ``django-appconf`` — used by this project to handle default configurations.
