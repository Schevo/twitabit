from paver.easy import *
import paver.misctasks
import paver.setuputils
from paver.setuputils import setup

from textwrap import dedent

from setuptools import Extension, find_packages


VERSION = '1.0'
DEVELOPMENT = True


# Use branch name if git information is available; otherwise, use
# version number from setup_meta.
if DEVELOPMENT:
    try:
        git_head_path = path('.git/HEAD')
        contents = git_head_path.open('rU').readline().strip()
        name, value = contents.split()
        BRANCH = value.split('/')[-1]
        if BRANCH != 'master':
            VERSION += '-' + BRANCH
    except:
        pass
    VERSION += '-dev'


setup(
    name='Twitabit',
    version=VERSION,
    description='Simple example application using Schevo',
    long_description=dedent("""
    Twit-a-bit is a simple example application that demonstrates how to
    integrate the following software packages:

    * Schevo
    * SchevoPolicy
    * Pylons
    * AuthKit

    The app itself is intentionally narrow in scope:

    * register new accounts
    * post bits of information
    * read an individual's bits
    * read all users' bits
    
    You can also get the `latest development version
    <http://github.com/gldnspud/twitabit/zipball/master#egg=Twitabit-dev>`__.
    """),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database :: Database Engines/Servers',
        'Topic :: Software Development :: Libraries :: '
            'Application Frameworks',
    ],
    keywords='database dbms',
    author='Orbtech, L.L.C. and contributors',
    author_email='schevo@googlegroups.com',
    url='http://www.schevo.org/',
    license='MIT',
    packages=find_packages(exclude=['doc', 'tests']),
    package_data={'twitabit': ['i18n/*/LC_MESSAGES/*.mo']},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Pylons >= 0.9.7',
        'Schevo >= 3.1',
        'SchevoPolicy >= 3.1',
        'AuthKit == dev, >= 0.4.0dev-r114',
    ],
    dependency_links = [
        'http://schevo.org/wiki/Twitabit',
    ],
    tests_require=['nose >= 0.10.4'],
    test_suite='nose.collector',
    entry_points = """
    [paste.app_factory]
    main = twitabit.config.middleware:make_app
    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
    )


options(
    cog=Bunch(
        basdir='doc/source',
        includedir='doc/source',
        pattern='*.txt',
        beginspec='<==',
        endspec='==>',
        endoutput='<==end==>',
    ),
    publish=Bunch(
        username='schevo',
        server='web7.webfaction.com',
        path='/home2/schevo/schevo_docs/twitabit/%s' % VERSION,
    ),
    sphinx=Bunch(
        docroot='doc',
        builddir='build',
        sourcedir='source',
    ),
)


@task
@needs('generate_setup', 'minilib', 'setuptools.command.sdist')
def sdist():
    """Overrides sdist to make sure that our setup.py is generated."""
    pass


try:
    import paver.doctools
except ImportError:
    pass
else:
    @task
    @needs(['paver.doctools.cog', 'paver.doctools.html', 'paver.doctools.uncog'])
    def html():
        pass


    @task
    @needs('html')
    def docs():
        import webbrowser
        index_file = path('doc/build/html/index.html')
        webbrowser.open('file://' + index_file.abspath())


    @task
    @needs(['paver.doctools.cog', 'paver.doctools.html', 'paver.doctools.uncog'])
    @cmdopts([("username=", "u", "Username for remote server"),
              ("server=", "s", "Server to publish to"),
              ("path=", "p", "Path to publish to")])
    def publish():
        src_path = path('doc/build/html') / '.'
        dest_path = path(options.path) / '.'
        # Create the remote directory and copy files to it.
        if options.username:
            server = '%s@%s' % (options.username, options.server)
        else:
            server = options.server
        if sys.platform == 'win32':
            sh('plink %s "mkdir -p %s"' % (server, options.path))
            sh('pscp -r -v -batch %s %s:%s' % (src_path, server, dest_path))
        else:
            sh('ssh %s "mkdir -p %s"' % (server, options.path))
            sh('rsync -zav --delete %s %s:%s' % (src_path, server, dest_path))


    @task
    def doctests():
        from paver.doctools import _get_paths
        import sphinx
        options.order('sphinx', add_rest=True)
        paths = _get_paths()
        sphinxopts = ['', '-b', 'doctest', '-d', paths.doctrees, 
            paths.srcdir, paths.htmldir]
        ret = dry(
            "sphinx-build %s" % (" ".join(sphinxopts),), sphinx.main, sphinxopts)


    @task
    @needs(['doctests', 'nosetests'])
    def test():
        pass
