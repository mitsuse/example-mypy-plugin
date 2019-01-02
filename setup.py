#!/usr/bin/env python3
# coding: utf-8

from setuptools import find_packages
from setuptools import setup

setup(
    name='example_mypy_plugin',
    version='0.1.0',
    description='An example for mypy plugin',
    url='https://github.com/mitsuse/example-mypy-plugin',
    author='Tomoya Kose',
    author_email='tomoya@mitsuse.jp',
    install_requires=[
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords=[
    ],
    packages=find_packages(exclude=[
        'tests',
    ]),
    entry_points={
        'console_scripts': [],
    },
)
