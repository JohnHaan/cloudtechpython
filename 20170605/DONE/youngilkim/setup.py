#!usr/bin/env python

from setuptools import setup, find_packages

console_scripts = [
    'what_year = youngilkim.check_date:what_year',
    'what_month = youngilkim.check_date:what_month',
    'what_date = youngilkim.check_date:what_date',
    'what_time = youngilkim.check_date:what_time',
]

setup(
    name='youngilkim',
    version='0.0.2',
    description='check_date package',
    author='youngilkim',
    author_email='youngilkim@netmarble.com',
    url='https://example.com',
    packages=find_packages(),
    install_requires=["datetime"],
    entry_points={'console_scripts': console_scripts},
)