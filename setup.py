try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='Twitabit',
    
    version="1.0a1",
    
    #description="",
    
    #author="",
    
    #author_email="",
    
    #url="",
    
    install_requires=[
    "Pylons >= 0.9.6dev-r2294",
    'Schevo >= 3.1a1dev-r3383',
    'SchevoPolicy >= 1.0a1dev-r3384',
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
