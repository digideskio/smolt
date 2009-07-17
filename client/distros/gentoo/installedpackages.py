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

import portage
from portage.dbapi.vartree import vartree
from portage.versions import catpkgsplit
from overlays import Overlays
from globaluseflags import GlobalUseFlags
from worldset import WorldSet
from packagestar import PackageMask, PackageUnmask, ProfilePackageMask
from packageprivacy import is_private_package_atom

class InstalledPackages:
    def __init__(self, debug=False,
            cb_enter=None, cb_done=None):
        self._cpv_flag_list = []
        var_tree = vartree()
        installed_cpvs = var_tree.getallcpv()  # TODO upstream plans rename?
        self._total_count = len(installed_cpvs)
        self._private_count = 0
        i = 0
        for cpv in installed_cpvs:
            i = i + 1
            if cb_enter:
                cb_enter(cpv, i, self._total_count)
            entry = self._process(var_tree, cpv, debug=debug)
            if entry:
                self._cpv_flag_list.append(entry)
            else:
                self._private_count = self._private_count + 1
        if cb_done:
            cb_done()

    def _keyword_status(self, ARCH, ACCEPT_KEYWORDS, KEYWORDS):
        k = set(KEYWORDS.split(' '))
        if ARCH in k:
            return ''
        TILDE_ARCH = '~' + ARCH
        if TILDE_ARCH in k:
            ak = set(ACCEPT_KEYWORDS.split(' '))
            if TILDE_ARCH in ak:
                return ''
            else:
                return '~arch'
        else:
            return '**'

    def _process(self, var_tree, cpv, debug=False):
        cat, pkg, ver, rev = catpkgsplit(cpv)
        package_name = "%s/%s" % (cat, pkg)
        if rev == 'r0':
            version_revision = ver
        else:
            version_revision = "%s-%s" % (ver, rev)

        SLOT, KEYWORDS, repository, IUSE, USE = \
            var_tree.dbapi.aux_get(cpv, ['SLOT', 'KEYWORDS', 'repository',
            'IUSE', 'USE'])

        # Perform privacy check and filtering
        installed_from = [repository, ]
        if is_private_package_atom('=' + cpv, installed_from=installed_from,
                debug=debug):
            return None
        repository = installed_from[0]

        ACCEPT_KEYWORDS = portage.settings['ACCEPT_KEYWORDS']
        ARCH = portage.settings['ARCH']
        keyword_status = self._keyword_status(ARCH, ACCEPT_KEYWORDS, KEYWORDS)

        unmasked = PackageUnmask().hits(cpv)
        # A package that is (1) installed and (2) not unmasked
        # cannot be masked so we skip the next line's checks
        masked = unmasked and (PackageMask().hits(cpv) or \
            ProfilePackageMask().hits(cpv))

        # World set test
        if SLOT != '0':
            world_set_test = '%s/%s:%s' % (cat, pkg, SLOT)
        else:
            world_set_test = '%s/%s' % (cat, pkg)
        is_in_world = world_set_test in WorldSet().get()

        # Use flags
        use_flags = GlobalUseFlags()
        flags = set(e for e in USE.split() if use_flags.is_known(e)) & \
            set(x.lstrip("+-") for x in IUSE.split() if use_flags.is_known(x))
        entry = [package_name, version_revision, SLOT, keyword_status,
            masked, unmasked, is_in_world, repository, sorted(flags)]
        return entry

    def total_count(self):
        return self._total_count

    def private_count(self):
        return self._private_count

    def known_count(self):
        return len(self._cpv_flag_list)

    def serialize(self):
        return self._cpv_flag_list

    def dump(self):
        print 'Installed packages:'
        for list in self._cpv_flag_list:
            package_name, version_revision, SLOT, keyword_status, \
                masked, unmasked, is_in_world, repository, sorted_flags_list = \
                list
            tags = [e for e in [
                masked and 'MASKED' or '',
                unmasked and 'UNMASKED' or '',
                is_in_world and 'WORLD' or ''] if e]
            print [package_name, version_revision, SLOT, keyword_status,
                tags, repository, sorted_flags_list]
        print
        print '  Total: ' + str(self.total_count())
        print '    Known: ' + str(self.known_count())
        print '    Private: ' + str(self.private_count())
        print

if __name__ == '__main__':
    def cb_enter(cpv, i, count):
        print '[%s/%s] %s' % (i, count, cpv)

    installed_packages = InstalledPackages(debug=True, cb_enter=cb_enter)
    installed_packages.dump()
