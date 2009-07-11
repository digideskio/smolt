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

import os
from portage.const import WORLD_FILE
from overlays import Overlays

class _WorldSet:
    def __init__(self):
        self._collect()

    def _collect(self):
        root = '/' # TODO
        world_file = os.path.join(root, WORLD_FILE)
        file = open(world_file, 'r')
        atoms = [line.rstrip("\r\n") for line in file]
        self._total_count = len(atoms)
        self._cps = set([e for e in atoms if not Overlays().is_secret_package(e)])
        self._secret_count = self._total_count - len(self._cps)
        file.close()

    def get(self):
        """
        Returns a set of <cat-pkg> and <cat-pkg-slot> atoms
        """
        return self._cps

    def contains(self, cat, pkg, slot):
        if slot in (None, '', '0'):
            world_set_test = '%s/%s' % (cat, pkg)
        else:
            world_set_test = '%s/%s:%s' % (cat, pkg, slot)
        return world_set_test in self._cps

    def total_count(self):
        return self._total_count

    def secret_count(self):
        return self._secret_count

    def known_count(self):
        return self.total_count() - self.secret_count()

    def dump(self):
        print 'World:'
        for i in self._cps:
            print i
        print 'Total: ' + str(self.total_count())
        print '  Known: ' + str(self.known_count())
        print '  Secret: ' + str(self.secret_count())
        print


_world_set_instance = None
def WorldSet():
    """
    Simple singleton wrapper around _Overlays class
    """
    global _world_set_instance
    if _world_set_instance == None:
        _world_set_instance = _WorldSet()
    return _world_set_instance


if __name__ == '__main__':
    worldset = WorldSet()
    worldset.dump()
