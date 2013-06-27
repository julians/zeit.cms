# Copyright (c) 2013 gocept gmbh & co. kg
# See also LICENSE.txt

import zc.sourcefactory.contextual
import zc.sourcefactory.source
import zeit.cms.content.contentsource
import zope.interface
import zope.schema.interfaces


class IWhitelistSource(zope.schema.interfaces.IIterableSource):
    """Tag whitelist"""


class WhitelistSource(
        zc.sourcefactory.contextual.BasicContextualSourceFactory):

    # this should be in .interfaces, but that leads to a circular import
    # between zeit.cms.content.interfaces and .interfaces

    # this is only contextual so we can customize the source_class

    class source_class(zc.sourcefactory.source.FactoredContextualSource):

        zope.interface.implements(
            IWhitelistSource,
            zeit.cms.content.contentsource.IAutocompleteSource)

        def get_check_types(self):
            """IAutocompleteSource"""
            return ['tag']

    @property
    def whitelist(self):
        import zeit.cms.tagging.interfaces
        return zope.component.getUtility(
            zeit.cms.tagging.interfaces.IWhitelist)

    def getValues(self, context):
        return self.whitelist.values()

    def getTitle(self, context, value):
        return value.label

    def getToken(self, context, value):
        return value.code
