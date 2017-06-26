#!/usr/bin/env python

from setuptools import setup, find_packages

console_scripts = [
    'jaemin = jaemin.check_date:main',
]

setup(
    name='jaemin',
    version='0.0.1',
    description='jaemin package',
    author='jaemin',
    author_email='jaemin@netmarble.com',
    url='https://example.com',
    packages=find_packages(),
    install_requires=["flask"],
    entry_points={'console_scripts': console_scripts},
)