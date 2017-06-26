#!/usr/bin/env python

from setuptools import setup, find_packages

console_scripts = [
    'what_year = jaemin.check_date:what_year',
    'what_month = jaemin.check_date:what_month',
    'what_date = jaemin.check_date:what_date',
    'what_time = jaemin.check_date:what_time',    
]

setup(
    name='CheckDate',
    version='0.0.3',
    description='example date check package',
    author='jaemin',
    author_email='jaemin@netmarble.com',
    url='https://jaemin.com',
    packages=find_packages(),
    install_requires=["flask"],
    entry_points={'console_scripts': console_scripts},
)
