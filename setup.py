#!/usr/bin/env python

import os, glob
from distutils.core import setup
from distutils.command.install import install

_VERSION="0.9.1"

class my_install(install):
   def init_siteconfig(self):
        config = open("RequiemNotify/siteconfig.py", "w")
        print >> config, "prefix = '%s'" % os.path.abspath(self.prefix)
        print >> config, "conf_dir = '/etc/requiem-notify'"
        print >> config, "version = '%s'" % _VERSION
        config.close()

   def run(self):
        os.umask(022)
        self.init_siteconfig()
        install.run(self)



setup(name="requiem-notify",
      version=_VERSION,
      maintainer = "Alexandre De Dommelin",
      maintainer_email = "adedommelin@tuxz.net",
      url = "https://github.com/requiem-forasiem/requiem-notify",
      packages=[ 'RequiemNotify' ],
      data_files=[ ("share/requiem-notify/themes/default", glob.glob("pixmaps/themes/default/*")),
                   ("share/requiem-notify/themes/default/tray", glob.glob("pixmaps/themes/tray/*")),
                   ("share/applications", ["requiem-notify.desktop"]),
                   ("/etc/requiem-notify", ["requiem-notify.conf"]) ],
      scripts=[ "requiem-notify" ],
      cmdclass={ 'install': my_install } )
