import zeit.cms.admin.interfaces
import zeit.cms.content.interfaces
import zeit.cms.interfaces
import zeit.cms.workflow.interfaces
import zope.component
import zope.interface


class DisplayBannerInContent(object):

    zope.component.adapts(zeit.cms.content.interfaces.ICommonMetadata)
    zope.interface.implements(zeit.cms.admin.interfaces.IBannerContentDisplay)

    def __init__(self, context):
        self.context = context

    @property
    def banner_content_display(self):
        return zeit.cms.content.interfaces.ICommonMetadata(
            self.context).banner_content

    @banner_content_display.setter
    def banner_content_display(self, value):
        banner_content_info = zeit.cms.content.interfaces.ICommonMetadata(
            context)
        banner_content_info.banner_content = value
