from zeit.cms.i18n import MessageFactory as _
import gocept.form.grouped
import zeit.cms.admin.interfaces
import zeit.cms.browser.form
import zope.formlib.form


class EditForm(zeit.cms.browser.form.EditForm):

    form_fields = zope.formlib.form.Fields(
        zeit.cms.admin.interfaces.IAdjustSemanticPublish)

    # Without field group it will look weird when context is an Article.
    field_groups = (gocept.form.grouped.RemainingFields(
        _('admin-field-group'), 'column-left-small'),)
