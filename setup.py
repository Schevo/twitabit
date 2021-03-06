try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='Twitabit',
    
    version="1.0a2",

    description = 'Simple example application using Schevo',
    
    long_description="""
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
    <http://getschevo.org/hg/repos.cgi/twitabit-dev/archive/tip.tar.gz#egg=Twitabit-dev>`__.
    """,
    
    classifiers=[
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Database :: Database Engines/Servers',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],

    author='Orbtech, L.L.C. and contributors',
    author_email='schevo@googlegroups.com',
    
    url='http://schevo.org/wiki/Twitabit',

    license='MIT',

    platforms=['UNIX', 'Windows'],

    install_requires=[
    'PasteDeploy >= 1.3.1',             # To prevent dependency probs.
    "Pylons >= 0.9.6.1",
    'Schevo == dev, >= 3.1a1dev',
    'SchevoPolicy == dev, >= 1.0a1dev',
    'AuthKit == dev, >= 0.4.0dev-r114',
    ],
    
    dependency_links = [
    'http://schevo.org/wiki/Twitabit',
    ],

    packages=find_packages(exclude=['ez_setup']),
    
    include_package_data=True,
    
    test_suite='nose.collector',
    
    package_data={'twitabit': ['i18n/*/LC_MESSAGES/*.mo']},
    
    entry_points="""
    [paste.app_factory]
    main = twitabit.config.middleware:make_app
    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
