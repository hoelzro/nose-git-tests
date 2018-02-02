from setuptools import setup
import sys

requirements = []

if sys.version_info.major != 3:
    requirements.append('subprocess32')

setup(
    name='nose-git-tests',
    version='1.0',
    author='Rob Hoelz',
    author_email='rob.hoelz@skinnycorp.com',
    description='Only run tests in files that are tracked by Git',
    long_description='''
I often create files named test.py or something in the root of a project for
playing around.  Unfortunately, nosetests picks these up and runs them, leading
me to wasted seconds of confusion when I discover that the test suite isn't actually
failing.  This nose plugin will require that a file be tracked in Git before being
run by nosetests
    '''.strip(),
    url='https://github.com/hoelzro/nose-git-tests',

    py_modules = ['nose_git_tests'],
    license    = 'Public Domain',

    entry_points={
        'nose.plugins.0.10': [
            'git-tests = nose_git_tests:GitTests'
        ],
    },
    install_requires=requirements,
)
