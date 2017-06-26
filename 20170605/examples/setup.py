#!/usr/bin/env python

from setuptools import setup, find_packages

console_scripts = [
    'example' = example:main',
]

setup(
    name='exmaple',
    version='0.0.1',
    description='example package',
    author='John Haan',
    author_email='sjhan@netmarble.com',
    url='https://example.com',
    packages=find_packages(),
    install_requires=["flask"],
    entry_points={'console_scripts': console_scripts},
)