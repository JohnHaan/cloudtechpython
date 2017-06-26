from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.txt')) as f:
    long_description = f.read()

setup(
    name='mytime',
    version='1.0.0',
    description='A sample Python project mytime',
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(exclude=['docs', 'tests']),
    entry_points={
        'console_scripts': [
            'what_year=mytime.cmd:what_year',
            'what_month=mytime.cmd:what_month',
            'what_day=mytime.cmd:what_day',
            'what_time=mytime.cmd:what_time',
        ],
    },
)
