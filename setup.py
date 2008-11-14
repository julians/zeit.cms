from setuptools import setup, find_packages

setup(
    name='zeit.cms',
    version='1.3dev',
    author='gocept',
    author_email='mail@gocept.com',
    url='https://svn.gocept.com/repos/gocept-int/zeit.cms',
    description="""\
""",
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data = True,
    zip_safe=False,
    license='gocept proprietary',
    namespace_packages = ['zeit', 'zeit.content'],
    install_requires=[
        'PILwoTk',
        'SilverCity',
        'ZODB3>=3.8.1',
        'transaction',
        'decorator',
        'gocept.cache>=0.2',
        'gocept.fckeditor',
        'gocept.form[formlib]>=0.7.5',
        'gocept.lxml>=0.2.1',
        'gocept.mochikit>=1.3.2',
        'gocept.runner',
        'gocept.pagelet',
        'guppy',
        'zc.iso8601',
        'lovely.remotetask',
        'lxml>=2.0.2',
        'python-cjson',
        'rwproperty>=1.0',
        'setuptools',
        'sprout',
        'z3c.conditionalviews>=1.0b2.dev-r91510',
        'z3c.etestbrowser',
        'z3c.flashmessage',
        'z3c.menu.simple>=0.5.1',
        'z3c.traverser',
        'zc.datetimewidget',
        'zc.form',
        'zc.recipe.egg>=1.1.0dev-r84019',
        'zc.relation',
        'zc.relation',
        'zc.resourcelibrary',
        'zc.set',
        'zc.sourcefactory',
        'zc.table',
        'zdaemon',
        'zeit.connector>=1.1',
        'zeit.objectlog>=0.6',
        'zope.app.apidoc',
        'zope.app.catalog',
        'zope.app.component>=3.4.0b3',
        'zope.app.form>=3.6.0',
        'zope.app.locking',
        'zope.app.onlinehelp',
        'zope.app.preference',
        'zope.app.securitypolicy',
        'zope.app.twisted',
        'zope.copypastemove',
        'zope.file',
        'zope.i18n>3.4.0',
        'zope.location>=3.4.0b2',
        'zope.sendmail',
        'zope.xmlpickle',
    ],
    entry_points = dict(
        console_scripts =
        ['run-lifetime-hits-importer = zeit.today.yesterday:main'])
)
