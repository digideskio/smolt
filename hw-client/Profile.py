#!/usr/bin/python

import hardware
import sys
import os
import commands
import re

initdefault_re = re.compile(r':(\d+):initdefault:')

class Profile:
    def __init__(self):
        try:
            self.UUID = file('/etc/sysconfig/hw-uuid').read()
        except IOError:
            try:
                self.UUID = file('/proc/sys/kernel/random/uuid').read()
                try:
                    file('/etc/sysconfig/hw-uuid', 'w').write(self.UUID)
                except:
                    sys.stderr.write('Unable to save UUID, continuing...\n')
            except IOError:
                sys.stderr.write('Unable to determine UUID of system!\n')
                sys.exit(1)

        self.hw = hardware.Hardware()
        
        self.lsbRelease = ''
        if os.access('/usr/bin/lsb_release', os.X_OK):
            self.lsbRelease = commands.getstatusoutput('/usr/bin/lsb_release')[1]

        try:
            self.OS = file('/etc/redhat-release').read()
        except IOError:
            self.OS = 'Unknown'

        self.defaultRunlevel = 'Unknown'
        try:
            inittab = file('/etc/inittab').read()
            match = initdefault_re.search(inittab)
            if match:
                self.defaultRunlevel = match.group(1)
        except IOError:
            sys.stderr.write('Unable to read /etc/inittab, continuing...')

        self.language = os.environ['LANG']

        self.platform = self.bogomips = self.CPUVendor = self.numCPUs = self.CPUSpeed = self.systemMemory = self.systemSwap = self.vendor = self.system = ''

        for device in self.hw:
            try:
                self.platform = device['platform']
                self.bogomips = device['bogomips']
                self.CPUVendor = "%s - %s" % (device['type'], device['model'])
                self.numCPUs = device['count']
                self.CPUSpeed = device['speed']
            except:
                pass
            try:
                self.systemMemory = device['ram']
                self.systemSwap = device['swap']
            except:
                pass
            try:
                self.vendor = device['vendor']
                self.system = device['system']
            except:
                pass

    def get_host_string(self):
        return "UUID=%s&lsbRelease=%s&OS=%s&defaultRunlevel=%s&language=%s&platform=%s&bogomips=%s&CPUVendor=%s&numCPUs=%s&CPUSpeed=%s&systemMemory=%s&systemSwap=%s&vendor=%s&system=%s" % (self.UUID, self.lsbRelease, self.OS, self.defaultRunlevel, self.language, self.platform, self.bogomips, self.CPUVendor, self.numCPUs, self.CPUSpeed, self.systemMemory, self.systemSwap, self.vendor, self.system)

    def get_device_string(self):
        for device in self.hw:
            try:
                Bus = device['bus']
                Driver = device['driver']
                Class = device['class']
                Description = device['desc']
            except:
                continue
            else:
                yield "UUID=%s&Bus=%s&Driver=%s&Class=%s&Description=%s" % (self.UUID, Bus, Driver, Class, Description)

    def print_data(self):
        print 'We are about to send the following information to the Fedora Smolt server:'
        print
        print '\tUUID: %s' % self.UUID
        print '\tlsbRelease: %s' % self.lsbRelease
        print '\tOS: %s' % self.OS
        print '\tdefaultRunlevel: %s' % self.defaultRunlevel
        print '\tlanguage: %s' % self.language
        print '\tplatform: %s' % self.platform
        print '\tbogomips: %s' % self.bogomips
        print '\tCPUVendor: %s' % self.CPUVendor
        print '\tnumCPUs: %s' % self.numCPUs
        print '\tCPUSpeed: %s' % self.CPUSpeed
        print '\tsystemMemory: %s' % self.systemMemory
        print '\tsystemSwap: %s' % self.systemSwap
        print '\tvendor: %s' % self.vendor
        print '\tsystem: %s' % self.system
        print
        print '\t\t Devices'
        print '\t\t================================='
        for device in self.hw:
            try:
                Bus = device['bus']
                Driver = device['driver']
                Class = device['class']
                Description = device['desc']
            except:
                continue
            else:
                print '\t\t%s, %s, %s, %s' % (Bus, Driver, Class, Description)
        
