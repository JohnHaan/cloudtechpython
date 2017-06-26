#!/usr/bin/env python

from setuptools import setup, find_packages

console_scripts = [
    'what_year = sjhan.check_date:what_year',
    'what_month = sjhan.check_date:what_month',
    'what_date = sjhan.check_date:what_date',
    'what_time = sjhan.check_date:what_time',    
]

setup(
    name='checkdate',
    version='0.0.1',
    description='check date package',
    author='sjhan',
    author_email='sjhan@netmarble.com',
    url='http://example.com',
    packages=find_packages(),
    install_requires=["flask"],
    entry_points={'console_scripts': console_scripts},
)
