from zeit.cms.admin.interfaces import IBannerContentDisplay
from zeit.cms.testcontenttype.testcontenttype import ExampleContentType
import pytz
import zeit.cms.content.interfaces
import zeit.cms.testing

class TestBannerContentDisplay(zeit.cms.testing.ZeitCmsTestCase):

    def setUp(self):
        super(TestBannerContentDisplay, self).setUp()
        self.content = ExampleContentType()

    def test_banner_content_has_correct_default_value(
            self):
        self.assertFalse(
            IBannerContentDisplay(self.content).banner_content_display)

    def test_banner_content_displays_correct_stored_value(
            self):
        zeit.cms.content.interfaces.ICommonMetadata(
            self.content).banner_content = False
        self.assertFalse(
            IBannerContentDisplay(self.content).banner_content_display)
        zeit.cms.content.interfaces.ICommonMetadata(
            self.content).banner_content = True
        self.assertTrue(
            IBannerContentDisplay(self.content).banner_content_display)
