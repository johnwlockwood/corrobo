import os
import sys
import uuid

try:
    from setuptools import find_packages
    from setuptools import setup
    packages = find_packages()
except ImportError:
    from distutils.core import setup
    packages = ['stream_tap', 'stream_tap.tests']

from pip.req import parse_requirements

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


def read(fname):
    """
    Open and read a filename in this directory.
    :param fname: `str` file name in this directory

    Returns contents of file fname
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version():
    import imp

    with open('stream_tap/_meta.py', 'rb') as fp:
        mod = imp.load_source('_meta', 'stream_tap', fp)

    return mod.version


def get_requirements(filename):
    try:
        reqs = list(parse_requirements(filename))
    except TypeError:
        reqs = list(parse_requirements(filename, session=uuid.uuid1()))

    return [str(r.req) for r in reqs]


def get_install_requires():
    return get_requirements('requirements.txt')


def get_test_requires():
    return get_requirements('requirements_dev.txt')


try:
    license_info = open('LICENSE').read()
except:
    license_info = 'APACHE 2.0'

setup_args = dict(
    name="auth_leader",
    version=get_version(),
    author="John W Lockwood IV",
    author_email="john@tackletronics.com",
    description="",
    license=license_info,
    keywords="data",
    url="https://github.com/johnwlockwood/auth_leader",
    package_dir={'auth_leader': 'auth_leader'},
    packages=packages,
    install_requires=get_install_requires(),
    tests_require=get_test_requires(),
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)

if __name__ == '__main__':
    setup(**setup_args)
