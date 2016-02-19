#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


setup(
    name='raspberrypi-py',
    version='1.0.2',
    description=("RaspberryPI Python library for programming "
                 "GPIO LEDs, buttons and other fun features"),
    long_description=('Accessible interface between users and '
                      'RaspberryPI\'s components.'),
    keywords="raspberry raspberrypi gpio raspberrypi-py leds lights",
    author='Andrei Prădan',
    author_email='andrei.pradan@gmail.com',
    url='https://github.com/andreipradan/raspberrypi-py',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'RPi.GPIO==0.6.1',
    ]
)
