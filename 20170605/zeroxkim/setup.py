#!/usr/bin/env python

from setuptools import setup, find_packages

console_scripts = [
    'zeroxkim = zeroxkim.check_date:main',
]

setup(
    name='zeroxkim',
    version='0.0.2',
    description='example package',
    author='ZeroXKim',
    author_email='zeroxkim@netmarble.com',
    url='https://zeroxkim.com',
    packages=find_packages(),
    install_requires=["flask"],
    entry_points={'console_scripts': console_scripts},
)
