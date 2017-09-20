from wagtail.utils.setup import sdist, check_bdist_egg

from setuptools import setup


setup(
    name='wagtailcolumnblocks',
    description='Wagtail Column Blocks',
    use_scm_version=True,
    author='Danielle Madeley',
    author_email='danielle.madeley@squareweave.com.au',
    url='https://github.com/squareweave/wagtailcolumnblocks',
    long_description=open('README.md').read(),
    license='BSD',
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django :: 1.11',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],

    packages=['wagtailcolumnblocks'],
    include_package_data=True,

    install_requires=[
        'wagtail >= 1.12',
    ],
    setup_requires=[
        'wagtail >= 1.12',
        'setuptools_scm',
    ],
    cmdclass={
        'sdist': sdist,
        'bdist_egg': check_bdist_egg,
    },
)
