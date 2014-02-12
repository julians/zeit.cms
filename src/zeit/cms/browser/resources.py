# Copyright (c) 2014 gocept gmbh & co. kg
# See also LICENSE.txt

from fanstatic import Library, Group
from js.jquery import jquery
from js.mochikit import mochikit
import fanstatic
import os.path
import pkg_resources
import sys


lib_css = Library('zeit.cms', 'resources')
lib_js = Library('zeit.cms.js', 'js')

backend = Group([])


def register(resource):
    depends = backend.depends.union(
        set(fanstatic.core.normalize_groups([resource])))
    for dep in depends:
        backend.resources.update(dep.resources)


class Resource(fanstatic.Resource):

    def __init__(self, filename, *args, **kw):
        globs = kw.pop('globs', sys._getframe(1).f_globals)
        lib = kw.pop('lib', globs.get('lib'))
        super(Resource, self).__init__(lib, filename, *args, **kw)
        globs['%s_%s' % self.splitext(filename)] = self
        register(self)

    def splitext(self, path):
        base, ext = os.path.splitext(os.path.basename(path))
        type_ = ext[1:]
        return base, type_


class SplitDirResource(Resource):

    def __init__(self, filename, *args, **kw):
        base, type_ = self.splitext(filename)
        kw['globs'] = sys._getframe(1).f_globals
        kw['lib'] = kw['globs']['lib_%s' % type_]
        super(SplitDirResource, self).__init__(filename, *args, **kw)


SplitDirResource('forms.css')
SplitDirResource('tables.css')
SplitDirResource('lightbox.css')
SplitDirResource('cms_widgets.css')
SplitDirResource('object_details.css')
SplitDirResource('cms.css')

# Only explicitly included by .error.ErrorView.
error_css = fanstatic.Resource(lib_css, 'error.css', depends=[cms_css])


# XXX js.jqueryui doesn't have 1.9, only 1.8 or 1.10, we might want to upgrade.
jqueryui_theme = fanstatic.Resource(
    lib_js, 'jquery/jquery-ui-1.9.1-custom-theme/jquery-ui-1.9.1.custom.css',
    minified='jquery/jquery-ui-1.9.1-custom-theme/'
    'jquery-ui-1.9.1.custom.min.css')
jqueryui = fanstatic.Resource(
    lib_js, 'jquery/jquery-ui-1.9.1.custom.js',
    minified='jquery/jquery-ui-1.9.1.custom.min.js',
    depends=[jquery, jqueryui_theme])
register(jqueryui)


zc_table = Library(
    'zc.table', pkg_resources.resource_filename('zc.table', 'resources'))
zc_table_js = fanstatic.Resource(zc_table, 'sorting.js')
register(zc_table_js)


zc_datetimewidget = Library(
    'zc.datetimewidget', pkg_resources.resource_filename(
        'zc.datetimewidget', 'resources'))
datetime_css = fanstatic.Resource(zc_datetimewidget, 'calendar-system.css')
datetime_calendar_js = fanstatic.Resource(zc_datetimewidget, 'calendar.js')
datetime_calendar_setup_js = fanstatic.Resource(
    zc_datetimewidget, 'calendar-setup.js', depends=[datetime_calendar_js])
datetime_calendar_en_js = fanstatic.Resource(
    zc_datetimewidget, 'languages/calendar-en.js',
    depends=[datetime_calendar_js])
datetime_widget_js = fanstatic.Resource(
    zc_datetimewidget, 'datetimewidget.js', depends=[
        datetime_css, datetime_calendar_en_js, datetime_calendar_setup_js,
])
register(datetime_widget_js)


SplitDirResource('namespace.js')
SplitDirResource('logging.js', depends=[namespace_js, mochikit, jquery])
SplitDirResource('base.js', depends=[namespace_js, mochikit, jquery, jqueryui])

base = Group([
    namespace_js, logging_js, base_js,
    cms_css, forms_css, tables_css, lightbox_css,
    cms_widgets_css, object_details_css,
])

SplitDirResource('objectbrowser.js', depends=[base])
SplitDirResource('tooltip.js', depends=[base])
SplitDirResource('lightbox.js', depends=[base])
SplitDirResource('details.js', depends=[base])
SplitDirResource('dnd.js', depends=[base])
SplitDirResource('object_reference.js', depends=[base])
SplitDirResource('object_sequence.js', depends=[base])
SplitDirResource('restructuredtext.js', depends=[base])
SplitDirResource('autocomplete.js', depends=[base])
SplitDirResource('table.js', depends=[base])
SplitDirResource('xeyes.js', depends=[base])
SplitDirResource('menu.js', depends=[base])
SplitDirResource('json-template.js', depends=[base])
SplitDirResource('view.js', depends=[base])
SplitDirResource('messages.js', depends=[base, view_js])
SplitDirResource('tab.js', depends=[base, view_js])
SplitDirResource('tree.js', depends=[base])
SplitDirResource('filteringtable.js', depends=[base])
SplitDirResource('panelHandlers.js', depends=[base])
