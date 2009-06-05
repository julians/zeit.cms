# Copyright (c) 2009 gocept gmbh & co. kg
# See also LICENSE.txt

import martian
import zeit.cms.interfaces
import zeit.cms.type
import zeit.connector.interfaces
import zeit.connector.resource
import zope.component.zcml


def annotate_interface(interface, key, value):
    interface.setTaggedValue(key, value)



class TypeGrokker(martian.ClassGrokker):

    martian.component(zeit.cms.type.TypeDeclaration)

    def execute(self, context, config, **kw):
        context = context()
        if context.interface is None:
            return False

        # Resource -> Content
        zope.component.zcml.adapter(
            config, (context.content,), zeit.cms.interfaces.ICMSContent,
            (zeit.connector.interfaces.IResource,), name=context.type)

        # Content -> Resource
        zope.component.zcml.adapter(
            config, (context.resource,), zeit.connector.interfaces.IResource,
            (context.interface,))

        # Annotate interface
        if context.register_as_type:
            config.action(
                discriminator=(
                    'annotate_interface', context.interface, 'zeit.cms.type'),
                callable=annotate_interface,
                args=(context.interface, 'zeit.cms.type', context.type))
            config.action(
                discriminator=(
                    'annotate_interface', context.interface, 'zeit.cms.title'),
                callable=annotate_interface,
                args=(context.interface, 'zeit.cms.title', context.title))
            zope.component.zcml.interface(
                config, context.interface, context.interface_type)

        return True

