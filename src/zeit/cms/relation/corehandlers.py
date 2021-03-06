import gocept.async
import logging
import zeit.cms.checkout.helper
import zeit.cms.checkout.interfaces
import zeit.cms.interfaces
import zeit.cms.relation.interfaces
import zope.component


log = logging.getLogger(__name__)


@zope.component.adapter(
    zeit.cms.interfaces.ICMSContent,
    zeit.cms.checkout.interfaces.IBeforeCheckinEvent)
def update_index_on_checkin(context, event):
    if getattr(event, 'publishing', False):
        return
    relations = zope.component.getUtility(
        zeit.cms.relation.interfaces.IRelations)
    relations.index(context)


@zope.component.adapter(
    zeit.cms.interfaces.ICMSContent,
    zeit.cms.checkout.interfaces.IAfterCheckinEvent)
def update_referencing_objects_handler(context, event):
    """Update metadata in objects which reference the checked-in object."""
    if event.publishing:
        return
    # prevent recursion
    if not gocept.async.is_async():
        update_referencing_objects(context)


@zeit.cms.async.function()
def update_referencing_objects(context):
    relations = zope.component.getUtility(
        zeit.cms.relation.interfaces.IRelations)
    relating_objects = relations.get_relations(context)
    for related_object in list(relating_objects):
        log.info(
            'Cycling %s to update referenced metadata (after checkin of %s)',
            related_object.uniqueId, context.uniqueId)
        # the actual work is done by IBeforeCheckin-handlers
        zeit.cms.checkout.helper.with_checked_out(
            related_object, lambda x: True)
