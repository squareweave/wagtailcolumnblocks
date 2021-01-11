from setuptools import setup

setup(
    name='wagtailcolumnblocks',
    description='Wagtail Column Blocks',
    use_scm_version=True,
    author='Squareweave',
    author_email='hosting+pypi@squareweave.com.au',
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
        'wagtail >= 2.0',
    ],
    setup_requires=[
        'setuptools_scm',
    ],
)
