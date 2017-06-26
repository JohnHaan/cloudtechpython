#!/usr/bin/env python

from setuptools import setup, find_packages

console_scripts = [
    'ianlee = ianlee.check_date:main',
]

setup(
    name='ianlee',
    version='0.0.4',
    description='example package',
    author='ianlee',
    author_email='conlee82@gmail.com',
    url='https://example.com',
    packages=find_packages(),
    install_requires=["flask"],
    entry_points={'console_scripts': console_scripts},
    )