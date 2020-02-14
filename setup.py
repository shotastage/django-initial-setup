from setuptools import find_packages, setup
from first_setup.version import version


setup(
    name='django-initial-setup',
    version=version,
    description='Django Initial Setup provides inital setup screen developed with Django for first launch.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Shota Shimazu',
    author_email='hornet.live.mf@gmail.com',
    url='https://github.com/shotastage/django-initial-setup',
    download_url='https://pypi.python.org/pypi/django-initial-setup',
    license='MIT',
    packages=find_packages(exclude=('tests')),
    install_requires=[
        'django>=2.0',
    ],
    extras_require={
    },
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Security',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
    ],
)
