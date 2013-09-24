# Copyright (c) 2013  Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import fixtures
import testtools

from oslo.config import cfg


class TestBase(testtools.TestCase):

    def setUp(self):
        super(TestBase, self).setUp()

        self.conf = cfg.ConfigOpts()
        self.useFixture(fixtures.FakeLogger('marconi'))

        # NOTE(kgriffs): Don't monkey-patch stdout since it breaks
        # debugging with pdb.
        stderr = self.useFixture(fixtures.StringStream('stderr')).stream
        self.useFixture(fixtures.MonkeyPatch('sys.stderr', stderr))

    def config(self, group=None, **kw):
        """Override some configuration values.

        The keyword arguments are the names of configuration options to
        override and their values.

        If a group argument is supplied, the overrides are applied to
        the specified configuration option group.

        All overrides are automatically cleared at the end of the current
        test by the tearDown() method.
        """
        for k, v in kw.items():
            self.conf.set_override(k, v, group)
