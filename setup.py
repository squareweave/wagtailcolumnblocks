from setuptools import setup

setup(
    name='wagtailcolumnblocks',
    description='Wagtail Column Blocks',
    use_scm_version=True,
    author='Squareweave',
    author_email='hosting+pypi@squareweave.com.au',
    url='https://github.com/squareweave/wagtailcolumnblocks',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    license='BSD',
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Framework :: Django :: 2.0',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],

    packages=['wagtailcolumnblocks'],
    include_package_data=True,

    install_requires=[
        'wagtail >= 2.10',
    ],
    setup_requires=[
        'setuptools_scm',
    ],
)
