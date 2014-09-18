#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import responsive

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = responsive.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print('You probably want to also tag the version now:')
    print('  git tag -a %s -m 'version %s'' % (version, version))
    print('  git push --tags')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-responsive2',
    version=version,
    description="""Utilities for building responsive websites in Django""",
    long_description=readme + '\n\n' + history,
    author='Mishbah Razzaque',
    author_email='mishbahx@gmail.com',
    url='https://github.com/mishbahr/django-responsive2',
    packages=[
        'responsive',
    ],
    include_package_data=True,
    install_requires=[
        'django-appconf',
    ],
    license='BSD',
    zip_safe=False,
    keywords='django-responsive2, responsive',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)