# smolt - Fedora hardware profiler
#
# Copyright (C) 2009 Sebastian Pipping <sebastian@pipping.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA.

from gate import GateFromConfig
import unittest
import ConfigParser
import os
import sys

def _wrap_gate():
    return GateFromConfig(os.path.join(sys.path[0], 'test.cfg'))

class TestGate(unittest.TestCase):

    def test_singleton(self):
        a = _wrap_gate()
        b = _wrap_gate()
        self.assertEqual(a, b)

    def test_valid(self):
        self.assertFalse(_wrap_gate().grants("any", "arch"))
        self.assertTrue(_wrap_gate().grants("any", "cpu"))
        self.assertTrue(_wrap_gate().grants("cpu"))

    def test_invalid(self):
        self.assertTrue(_wrap_gate().grants("any", "FOO"))
        self.assertTrue(_wrap_gate().grants("FOO", "BAR"))
