# -*- coding: utf-8 -*-
# smolt - Fedora hardware profiler
#
# Copyright (C) 2007 Mike McGrath
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

from turbogears import expose

class Error(object):
    def error_client(self, *args, **keys):
        ''' Exception handler, sends messages back
            to the command line client'''
        message = str(keys['tg_exceptions'])
        return dict(handling_value=True,exception=message)

    @expose(template="hardware.templates.error")
    def error_web(self, *args, **keys):
        ''' Exception handler, sends messages back
            to the web brower'''
        message = 'Error: %s' % keys['tg_exceptions']
        return dict(handling_value=True,exception=message)

error = Error()
