#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'rdflib',
]

test_requirements = [
]

setup(
    name='bambu',
    version='0.1.0',
    description='Bambu integrates Pandas and RDF',
    long_description=readme + '\n\n' + history,
    author='Wes Turner',
    author_email='wes@wrd.nu',
    url='https://github.com/westurner/bambu',
    packages=[
        'bambu',
    ],
    package_dir={'bambu':
                 'bambu'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    entry_points="""
    [console_scripts]
    bambu = bambu.bambu:main
    """,
    keywords='bambu',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
