#!/usr/bin/env python

from setuptools import setup, find_packages

console_scripts = [
    'sjhan = sjhan.check_date:main',
]

setup(
    name='sjhan',
    version='0.0.2',
    description='example package',
    author='John Haan',
    author_email='sjhan@netmarble.com',
    url='https://zeroxkim.com',
    packages=find_packages(),
    install_requires=["flask"],
    entry_points={'console_scripts': console_scripts},
)
