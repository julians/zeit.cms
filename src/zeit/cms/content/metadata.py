# Copyright (c) 2007-2008 gocept gmbh & co. kg
# See also LICENSE.txt
# $Id$

import zope.component
import zope.interface

import zeit.cms.content.dav
import zeit.cms.content.interfaces
import zeit.cms.content.property
import zeit.cms.content.xmlsupport


class KeywordsProperty(zeit.cms.content.property.MultiPropertyBase):

    def __init__(self):
        super(KeywordsProperty, self).__init__('.head.keywordset.keyword')

    def __set__(self, instance, value):
        super(KeywordsProperty, self).__set__(instance, value)
        tree = instance.xml
        for keyword in self.path.find(tree, []):
            keyword.set('source', 'manual')

    def _element_factory(self, node, tree):
        taxonomy = zope.component.getUtility(
            zeit.cms.content.interfaces.IKeywords)
        rdf_id = unicode(node)
        return taxonomy[rdf_id]

    def _node_factory(self, entry, tree):
        return entry.code


class CommonMetadata(zeit.cms.content.xmlsupport.XMLContentBase):

    zope.interface.implements(
        zeit.cms.content.interfaces.ICommonMetadata)

    zeit.cms.content.dav.mapProperties(
        zeit.cms.content.interfaces.ICommonMetadata,
        zeit.cms.interfaces.DOCUMENT_SCHEMA_NS,
        ('serie', 'copyrights', 'year', 'volume', 'ressort', 'page',
         'sub_ressort', 'vg_wort_id'))

    authors = zeit.cms.content.dav.DAVProperty(
        zeit.cms.content.interfaces.ICommonMetadata['authors'],
        zeit.cms.interfaces.DOCUMENT_SCHEMA_NS,
        'author',
        use_default=True)

    keywords = KeywordsProperty()

    title = zeit.cms.content.property.ObjectPathProperty(
        '.body.title')
    subtitle = zeit.cms.content.property.ObjectPathProperty(
        '.body.subtitle')
    supertitle = zeit.cms.content.property.ObjectPathProperty(
        '.body.supertitle')
    byline = zeit.cms.content.property.ObjectPathProperty(
        '.body.byline')

    teaserTitle = zeit.cms.content.property.ObjectPathProperty(
        '.teaser.title')
    teaserText = zeit.cms.content.property.ObjectPathProperty(
        '.teaser.text')

    shortTeaserTitle = zeit.cms.content.property.ObjectPathProperty(
        '.indexteaser.title')
    shortTeaserText = zeit.cms.content.property.ObjectPathProperty(
        '.indexteaser.text')
