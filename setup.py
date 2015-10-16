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
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()


readme = open('README.rst').read()

setup(
    name='django-responsive2',
    version=version,
    description="""Utilities for building responsive websites in Django""",
    long_description=readme,
    author='Mishbah Razzaque',
    author_email='mishbahx@gmail.com',
    url='https://github.com/mishbahr/django-responsive2',
    packages=[
        'responsive',
    ],
    include_package_data=True,
    install_requires=[
        'django-appconf',
        'six',
    ],
    license='BSD',
    zip_safe=False,
    keywords='django-responsive2, responsive',
    classifiers=[
        'Development Status :: 4 - Beta',
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
