#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydwd import __version__

try:
    from setuptools import setup, find_packages

except ImportError as error:
    raise ImportError(error)

setup(
    name='pydwd',
    version=__version__,
    url='https://github.com/ckaus/pydwd',
    download_url='https://github.com/ckaus/pydwd/tarball/1.0.1',
    author='ckaus',
    author_email='christian.kaus@hotmail.de',
    description='Python library for crawling weather data of Germany.',
    long_description='''PyDWD crawl weather data from german weather stations.
    The weather data are provided by Deutscher Wetterdienst.''',
    license='MIT',
    packages=find_packages(exclude="example"),
    package_data={'pydwd.utils': ['parameter.cfg']},
    include_package_data=True,
    keywords=['dwd', 'weather', 'crawler'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
