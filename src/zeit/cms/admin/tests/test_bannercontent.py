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
            ICommonMetadata(self.content).banner_content)

    def test_banner_contents_correct_stored_value(
            self):
        zeit.cms.content.interfaces.ICommonMetadata(
            self.content).banner_content = False
        self.assertFalse(
            ICommonMetadata(self.content).banner_content)
        zeit.cms.content.interfaces.ICommonMetadata(
            self.content).banner_content = True
        self.assertTrue(
            ICommonMetadata(self.content).banner_content)
