import transaction
import urllib2
import zeit.cms.browser.preview
import zeit.cms.interfaces
import zeit.connector.interfaces
import zope.component


class WorkingcopyPreview(zeit.cms.browser.preview.Preview):
    """Preview for workingcopy versions of content objects.

    Uploads the workingcopy version of an object to the repository, retrieves
    the html and returns it.

    """

    def __call__(self):
        preview_obj = self.get_preview_object()
        url = self.get_preview_url_for(preview_obj)
        preview_request = urllib2.urlopen(url)
        del preview_obj.__parent__[preview_obj.__name__]
        return preview_request.read()

    def get_preview_url_for(self, preview_context):
        url = zope.component.getMultiAdapter(
            (preview_context, self.preview_type),
            zeit.cms.browser.interfaces.IPreviewURL)
        querystring = self.request.environment['QUERY_STRING']
        if querystring:
            url = '%s?%s' % (url, querystring)
        return url

    def get_preview_object(self):
        # create a copy and remove unique id
        content = zeit.cms.interfaces.ICMSContent(
            zeit.connector.interfaces.IResource(self.context))
        content.uniqueId = None

        target_folder = zeit.cms.interfaces.ICMSContent(
            self.context.uniqueId).__parent__

        temp_id = self.get_temp_id(self.context.__name__)
        target_folder[temp_id] = content

        config = zope.app.appsetup.product.getProductConfiguration('zeit.cms')
        if config['workingcopy-preview-commit'] == 'True':
            # Our normal commit happens *after* the request to the preview, and
            # relying on the DAV invalidations to get the changes into the ZODB
            # so they are visible for zeit.web is too timing-sensitive to be
            # reliable.
            # XXX Committing early seems to cause ConflictErrors with the async
            # task processor, so we make it configurable until we know why.
            transaction.commit()
        return content

    def get_temp_id(self, name):
        return 'preview-%s-%s' % (
            self.request.principal.id, name)
