try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='validator',
    author='Hugo Dworak and Creative Commons',
    install_requires=['setuptools',
                      'nose',
                      'Paste',
                      'WebHelpers<0.4',
                      'Pylons == 0.9.6.1',
                      'PylonsGenshi',
                      'SQLAlchemy',
                      'libvalidator'
                      ],
    packages=find_packages(exclude=['ez_setup',]),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'validator': ['i18n/*/LC_MESSAGES/*.mo']},
    entry_points="""
    [paste.app_factory]
    main = validator.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """
)
