# Copyright (c) 2007 gocept gmbh & co. kg
# See also LICENSE.txt
# $Id$

import os.path

import zope.app.appsetup.product


cms_config = zope.app.appsetup.product.getProductConfiguration('zeit.cms')


if cms_config is None:
    # Test configuration
    base_path = os.path.join(os.path.dirname(__file__), 'content')

    SERIE_URL = 'file://%s' % os.path.join(base_path, 'serie.xml')
    RESSORT_URL = 'file://%s' % os.path.join(base_path, 'ressort.xml')
    PRINT_RESSORT_URL = 'file://%s' % os.path.join(base_path, 'ressort.xml')
    KEYWORD_URL = 'file://%s' % os.path.join(
        base_path, 'zeit-ontologie-prism.xml')

    PREVIEW_PREFIX = 'http://localhost/preview-prefix'
    LIVE_PREFIX = 'http://localhost/live-prefix'
    DEVELOPMENT_PREVIEW_PREFIX = 'http://localhost/development-preview-prefix'

else:

    SERIE_URL = cms_config.get('source-serie')
    RESSORT_URL = cms_config.get('source-ressort')
    PRINT_RESSORT_URL = cms_config.get('source-print-ressort')
    KEYWORD_URL = cms_config.get('source-keyword')

    PREVIEW_PREFIX = cms_config.get('preview-prefix')
    LIVE_PREFIX = cms_config.get('live-prefix')
    DEVELOPMENT_PREVIEW_PREFIX = cms_config.get('development-preview-prefix')

