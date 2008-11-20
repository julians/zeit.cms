# Copyright (c) 2007-2008 gocept gmbh & co. kg
# See also LICENSE.txt

import unittest

from zope.testing import doctest

import zeit.cms.testing


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(doctest.DocFileSuite(
        'adapter.txt',
        'field.txt',
        'keyword.txt',
        'lxmlpickle.txt',
        'property.txt',
        optionflags=(doctest.REPORT_NDIFF + doctest.NORMALIZE_WHITESPACE +
                     doctest.ELLIPSIS),
        setUp=zeit.cms.testing.setUp))

    suite.addTest(zeit.cms.testing.FunctionalDocFileSuite(
        'dav.txt',
        'liveproperty.txt',
        'metadata.txt',
        'sources.txt',
        'xmlsupport.txt',
    ))
    return suite
