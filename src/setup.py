"""
# install it by: pip install --process-dependency-links --trusted-host guthub.com -e .
"""

from os.path import join, dirname
import re
from setuptools import setup, find_packages
__author__ = 'aida'

# reading package version (same way the sqlalchemy does)
with open(join(dirname(__file__), 'tarsier', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)

test_dependencies = [
    'webtest',
    'nose'
]

dependencies = [
    'Mako',
    'aiohttp',
    'aiohttp_mako',
    'wheezy.web',
    'khayyam',
    'pymlconf',
    'appdirs',
    'lutino'
] + test_dependencies

dependency_links = [

]

setup(
    name='tarsier',
    version=package_version,
    author='Aida Mirabadi',
    author_email='aida.mirabadi@gmail.com',
    long_description=open(join('..', 'README.md'), encoding='UTF-8').read(),
    install_requires=dependencies + test_dependencies,
    packages=find_packages(),
    dependency_links=dependency_links,
    message_extractors={'tarsier': [
        ('**.py', 'python', None),
        ('**.mak', 'python', None),
    ]},
    entry_points={
        'console_scripts': [
            'tarsier = tarsier.cli:main'
        ]
    },
)
