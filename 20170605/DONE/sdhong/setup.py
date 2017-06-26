#!/usr/bin/env python

from setuptools import setup, find_packages

console_scripts = [
    'what_year = sdhong.check_date:what_year',
    'what_month = sdhong.check_date:what_month',
    'what_date = sdhong.check_date:what_date',
    'what_time = sdhong.check_date:what_time', 
]

setup(
    name='done',
    version='0.0.1',
    description='done package',
    author='sdhong',
    author_email='sdhong@netmarble.com',
    url='https://example.com',
    packages=find_packages(),
    install_requires=["flask"],
    entry_points={'console_scripts': console_scripts},
)