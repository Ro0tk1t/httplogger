#!/usr/bin/env python
# coding=utf-8

from setuptools import find_packages, setup
import httplogger

setup(
        name = 'httplogger',
        version = httplogger.__version__,
        url = 'git@github.com:Ro0tk1t/httplogger.git',
        description = 'A Simple package to parse apache‘s access.log',
        author = 'Ro0tk1t',
        packages = find_packages(),
        install_requires = [
                            'six',
                            ]
    )
