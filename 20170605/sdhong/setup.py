#!/usr/bin/env python

from setuptools import setup, find_packages

console_scripts = [
    'sdhong = sdhong.check_date:main',
#    'what_time = sdhong.what_time:main',
]

setup(
    name='sdhong',
    version='0.0.2',
    description='example package',
    author='sdhong',
    author_email='sdhong@netmarble.com',
    url='https://example.com',
    packages=find_packages(),
    install_requires=["flask"],
    entry_points={'console_scripts': console_scripts},
)