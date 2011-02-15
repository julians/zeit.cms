# Copyright (c) 2011 gocept gmbh & co. kg
# See also LICENSE.txt

import mock
import unittest2
import zeit.cms.testing


class TestWidget(zeit.cms.testing.SeleniumTestCase,
                 unittest2.TestCase):

    def setup_tags(self, *codes):
        import stabledict
        tags = stabledict.StableDict()
        for code in codes:
            tag = mock.Mock()
            tag.code = tag.label = code
            tag.disabled = False
            tags[code] = tag
        patcher = mock.patch('zeit.cms.tagging.interfaces.ITagger')
        self.addCleanup(patcher.stop)
        tagger = patcher.start()
        tagger.return_value = tags
        return tags

    def open_content(self):
        self.open('/repository/testcontent/@@checkout')
        s = self.selenium
        s.type('name=form.year', '2011')
        s.select('name=form.ressort', 'label=Deutschland')
        s.type('name=form.title', 'Test')
        s.type('name=form.authors.0.', 'Hans Wurst')

    def test_tags_should_be_sortable(self):
        self.setup_tags('t1', 't2', 't3', 't4')
        self.open_content()
        s = self.selenium
        s.assertTextPresent('t1*t2*t3*t4')
        s.dragAndDropToObject(
            "xpath=//li[contains(., 't1')]",
            "xpath=//li[contains(., 't3')]")
        s.assertTextPresent('t2*t3*t1*t4')

    def test_sorted_tags_should_be_saved(self):
        tags = self.setup_tags('t1', 't2', 't3', 't4')
        self.open_content()
        s = self.selenium
        s.dragAndDropToObject(
            "xpath=//li[contains(., 't1')]",
            "xpath=//li[contains(., 't3')]")
        s.assertTextPresent('t2*t3*t1*t4')
        s.clickAndWait('name=form.actions.apply')
        self.assertEqual(4, tags['t2'].weight)
        self.assertEqual(3, tags['t3'].weight)
        self.assertEqual(2, tags['t1'].weight)
        self.assertEqual(1, tags['t4'].weight)

    def test_unchecked_tags_should_be_disabled(self):
        tags = self.setup_tags('t1', 't2', 't3', 't4')
        self.open_content()
        s = self.selenium
        s.click("xpath=//li/label[contains(., 't1')]")
        s.clickAndWait('name=form.actions.apply')
        self.assertTrue(tags['t1'].disabled)
        self.assertFalse(tags['t2'].disabled)
