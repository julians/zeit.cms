import unittest
import zeit.cms.testing
from zope.testing import doctest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(zeit.cms.testing.FunctionalDocFileSuite(
        'README.txt'))
    return suite
