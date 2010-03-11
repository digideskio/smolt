# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import *
from sqlalchemy.orm import *
#from sqlalchemy.ext.assignmapper import assign_mapper
from datetime import timedelta, date, datetime


# Context dependent metadata and mapper creation
import sys
import logging
if 'turbogears' in sys.modules:
    logging.debug('Turbogears context')
    from turbogears.database import metadata
    from turbogears.database import mapper
else:
    logging.debug('Plain SQL alchemy context')
    from sqlalchemy.orm import mapper
    from sqlalchemy import MetaData
    metadata = MetaData()


import os
import sys
import inspect
sys.path.append(os.path.join(os.path.dirname(inspect.currentframe().f_code.co_filename), '..', '..'))
from playmodel import *


#ctx = session.context


computer_logical_devices = \
       Table('device', metadata,
             Column("id", INT, autoincrement=True,
                    nullable=False, primary_key=True),
             Column("description", VARCHAR(128),
                    nullable=False),
             Column("bus", TEXT),
             Column("driver", TEXT),
             Column("class", VARCHAR(24),
                    ForeignKey("classes.cls"),
                    key="cls"),
             Column("date_added", DATETIME),
             Column("device_id", INT),
             Column("vendor_id", INT),
             Column("subsys_device_id", INT),
             Column("subsys_vendor_id", INT))

host_links = Table('host_links', metadata,
                   Column("id", INT,
                          autoincrement=True,
                          nullable=False,
                          primary_key=True),
                   Column('host_link_id', INT,
                          ForeignKey("host.id"),
                          nullable=False),
                   Column("device_id", INT,
                          ForeignKey("device.id")),
                   Column("rating", INT))

host_links_archive = Table('host_links_archive', metadata,
                   Column("id", INT,
                          autoincrement=True,
                          nullable=False,
                          primary_key=True),
                   Column('host_link_id', INT,
                          ForeignKey("host.id"),
                          nullable=False),
                   Column("device_id", INT,
                          ForeignKey("device.id")),
                   Column("rating", INT))

hosts = Table('host', metadata,
              Column("id", INT,
                     autoincrement=True,
                     nullable=False,
                     primary_key=True),
              Column('uuid', VARCHAR(36),
                     nullable=False,
                     unique=True),
              Column('pub_uuid', VARCHAR(40),
                     nullable=False,
                     unique=True),
              Column('os', TEXT),
              Column('platform', TEXT),
              Column('bogomips', DECIMAL),
              Column('system_memory', INT),
              Column('system_swap', INT),
              Column('vendor', TEXT),
              Column('system', TEXT),
              Column('cpu_vendor', TEXT),
              Column('cpu_model', TEXT),
              Column('num_cpus', INT),
              Column('cpu_speed', DECIMAL),
              Column('language', TEXT),
              Column('default_runlevel', INT),
              Column('kernel_version', TEXT),
              Column('formfactor', TEXT),
              Column('last_modified', DATETIME,
                     default=0, nullable=False),
              Column('rating', INT, nullable=False, default=0),
              Column('selinux_enabled', INT, nullable=False),
              Column('selinux_policy', TEXT),
              Column('selinux_enforce', TEXT),
              Column('cpu_stepping', INT, default=None),
              Column('cpu_family', INT, default=None),
              Column('cpu_model_num', INT, default=None))
#              Column('myth_systemrole', TEXT),
#              Column('mythremote', TEXT),
#              Column('myththeme', TEXT))

hosts_archive = Table('host_archive', metadata,
              Column("id", INT,
                     autoincrement=True,
                     nullable=False,
                     primary_key=True),
              Column('uuid', VARCHAR(36),
                     nullable=False,
                     unique=True),
              Column('pub_uuid', VARCHAR(40),
                     nullable=False,
                     unique=True),
              Column('os', TEXT),
              Column('platform', TEXT),
              Column('bogomips', DECIMAL),
              Column('system_memory', INT),
              Column('system_swap', INT),
              Column('vendor', TEXT),
              Column('system', TEXT),
              Column('cpu_vendor', TEXT),
              Column('cpu_model', TEXT),
              Column('num_cpus', INT),
              Column('cpu_speed', DECIMAL),
              Column('language', TEXT),
              Column('default_runlevel', INT),
              Column('kernel_version', TEXT),
              Column('formfactor', TEXT),
              Column('last_modified', DATETIME,
                     default=0, nullable=False),
              Column('rating', INT, nullable=False, default=0),
              Column('selinux_enabled', INT, nullable=False),
              Column('selinux_policy', TEXT),
              Column('selinux_enforce', TEXT),
              Column('cpu_stepping', INT, default=None),
              Column('cpu_family', INT, default=None),
              Column('cpu_model_num', INT, default=None))

fas_links = Table('fas_link', metadata,
                  Column("id", INT, autoincrement=True,
                         nullable=False, primary_key=True),
                  Column('uuid', VARCHAR(36),
                         ForeignKey("host.uuid"),
                         nullable=False),
                  Column("user_name", VARCHAR(255),
                         nullable=False))

hardware_classes = Table('classes', metadata,
                         Column("class", VARCHAR(24),
                                nullable=False,
                                primary_key=True, key="cls"),
                         Column("description", TEXT,
                                key="class_description"))

file_systems = Table('file_systems', metadata,
                     Column('id', INT, autoincrement=True,
                            nullable=False, primary_key=True),
                     Column('host_id', INT,
                            ForeignKey("host.id")),
                     Column('mnt_pnt', TEXT),
                     Column('fs_type', TEXT),
                     Column('f_favail', INT),
                     Column('f_bsize', INT),
                     Column('f_frsize', INT),
                     Column('f_blocks', INT),
                     Column('f_bfree', INT),
                     Column('f_bavail', INT),
                     Column('f_files', INT),
                     Column('f_ffree', INT),
                     Column('f_fssize', INT))

batch_queue = Table('batch_queue', metadata,
                    Column('id', Integer,
                            primary_key=True, autoincrement=True),
                    Column('arrival', TIMESTAMP,
                            nullable=False),
                    Column('added', Boolean,
                            nullable=False),
                    Column('hw_uuid', VARCHAR(36),
                            nullable=False),
                    Column('data', CLOB(1000000)))


class Host(object):
    def __init__(self, selinux_enabled=False,
                 rating=0, last_modified=datetime.today()):
        self.selinux_enabled = selinux_enabled
        self.rating = rating
        self.last_modified = last_modified

class HostArchive(object):
    def __init__(self, rating=0):
        self.rating = rating

class ComputerLogicalDevice(object):
    pass

class HostLink(object):
    def __init__(self, rating=0):
        self.rating = rating

class HostLinkArchive(object):
    def __init__(self, rating=0):
        self.rating = rating

class FasLink(object):
    def __init__(self, uuid, user_name):
        self.uuid = uuid
        self.user_name = user_name

class HardwareClass(object):
    def _set_cls(self, cls):
        if cls is None:
            cls = "NONE"
        self._cls = cls
    def _get_cls(self):
        return self._cls
    pass
    cls = property(_get_cls, _set_cls)

class FileSystem(object):
    pass

class BatchJob(object):
    def __init__(self, data, hw_uuid, added):
        self.data = data
        self.hw_uuid = hw_uuid
        self.added = added
        self.arrival = text('NOW()')


mapper(Host, hosts,
       properties=dict(_devices=relation(HostLink,
                                         cascade="all,delete-orphan",
                                         backref=backref('host'),
                                         lazy=None),
                      devices=relation(HostLink, cascade='all,delete-orphan'),
                      fas_account=relation(FasLink, uselist=False),
                      file_systems=relation(FileSystem,
                                            backref='host')))

mapper(HostArchive, hosts_archive)

mapper(ComputerLogicalDevice,
       computer_logical_devices,
       properties = {"_host_links": relation(HostLink,
                                            cascade="all,delete-orphan",
                                            backref=backref('device'),
                                            lazy=None),
                     "host_links": relation(HostLink,
                                            cascade="all,delete-orphan")})

mapper(HostLink, host_links)
mapper(HostLinkArchive, host_links_archive)

mapper(FasLink, fas_links, properties = {'hosts': relation(Host),
                                         'uuid': fas_links.c.uuid})

mapper(HardwareClass,
       hardware_classes,
       properties = {'devices': relation(ComputerLogicalDevice,
                                         cascade="all,delete-orphan",
                                         backref=backref('hardware_class'),
                                         lazy=None),
                     '_cls': hardware_classes.c.cls,
                     'cls': synonym('_cls')})

mapper(FileSystem, file_systems)

mapper(BatchJob, batch_queue)
