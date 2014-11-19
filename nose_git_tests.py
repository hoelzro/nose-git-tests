import os
import subprocess32 as subprocess

from nose.plugins.base import Plugin
from nose.selector import Selector

class GitOnlySelector(Selector):
    def wantFile(self, filename):
        result = super(GitOnlySelector, self).wantFile(filename)
        if not result:
            return result

        with open(os.devnull, 'w') as nowhere:
            try:
                output = subprocess.check_output(['git', 'ls-files', filename], stderr=nowhere)
                return output != ''
            except subprocess.CalledProcessError:
                return False

class GitTests(Plugin):
    name = 'git-tests'

    def options(self, parser, env):
        parser.add_option('--git-tests-only',
            action='store_true',
            dest=self.enableOpt,
            default=env.get('NOSE_GIT_TESTS'),
            help='Only run tests tracked by git')

    def prepareTestLoader(self, loader):
        loader.selector = GitOnlySelector(loader.config)
