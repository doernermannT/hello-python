#!/usr/bin/env python

from setuptools import setup

setup(
    name='hello-flake-python',
    version='0.1.0',
    py_modules=['hello'],
    entry_points={
        'console_scripts': ['hello-flake-python = hello:main']
    },
)
