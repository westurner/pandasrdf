#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
"""
bambu
------
pandas RDF functionality


Installation
--------------
::

    # pip install pandas
    pip install rdflib

"""
import sys

import pandas as pd
import rdflib


def bambu():
    """
    mainfunc
    """
    pass


def to_rdf(df):
    """
    Args:
        df (DataFrame): pandas DataFrame to serialize to RDF
        kwargs (dict): TODO
    Returns:
        rdflib.Graph: a serializable RDFLib Graph
    """


def read_rdf(path, **kwargs):
    """
    Args:
        path (str): path to an RDF source
        kwargs (dict): TODO
    Returns:
        DataFrame: pandas DataFrame
    """


def to_rdfa(df, **kwargs):
    """
    Args:
        df (DataFrame): pandas DataFrame to serialize to RDF
        kwargs (dict): TODO
    Returns:
        (list, StringIO): namespaces, RDFa table
    """


def read_rdfa(path, **kwargs):
    """
    Args:
        path (str): path to an RDF source
        kwargs (dict): TODO
    Returns:
        DataFrame: pandas DataFrame
    """


def to_jsonld(df, **kwargs):
    """
    Args:
        df (DataFrame): pandas DataFrame to serialize to RDF
        kwargs (dict): TODO
    Returns:
        (context, StringIO): JSONLD context, JSONLD data
    """


def read_jsonld(path, **kwargs):
    """
    Args:
        path (str): path to a JSONLD source
        kwargs (dict): TODO
    Returns:
        DataFrame: pandas DataFrame
    """


import unittest


class Test_bambu(unittest.TestCase):

    def test_bambu(self):
        pass

    def test_10_to_rdf(self):
        df = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
        output = to_rdf(df)
        print(output)
        self.assertTrue(output)


def main(*args):
    import optparse
    import logging

    prs = optparse.OptionParser(usage="%prog: [args]")

    prs.add_option('-v', '--verbose',
                   dest='verbose',
                   action='store_true',)
    prs.add_option('-q', '--quiet',
                   dest='quiet',
                   action='store_true',)
    prs.add_option('-t', '--test',
                   dest='run_tests',
                   action='store_true',)

    args = args and list(args) or sys.argv[1:]
    (opts, args) = prs.parse_args(args)

    if not opts.quiet:
        logging.basicConfig()

        if opts.verbose:
            logging.getLogger().setLevel(logging.DEBUG)

    if opts.run_tests:
        sys.argv = [sys.argv[0]] + args
        import unittest
        sys.exit(unittest.main())

    output = bambu()
    return 0

if __name__ == "__main__":
    sys.exit(main())
