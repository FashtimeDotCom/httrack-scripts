#!/usr/bin/python

from __future__ import print_function
  
import six.moves.configparser as configparser

from datetime import datetime
import os
import sys
import subprocess
import shutil
import shlex


def run_httrack():
    os.system('httrack')
    return

def site_modification():
    try:
        shutil.move('index-2.html', 'index.html')
    except IOError as e:
        print("I/O error({0}): {1}: {2}".format(e.errno, e.strerror, e.filename))
    return

def rsync_to_apollo():
    cmd = 'rsync --delete -rhlptdOiv --exclude="hts-*" %s/ %s' % (os.path.realpath(os.curdir), conf['destination'])
    print(cmd)
    os.system(cmd)
    return

def do_site_update():
    print("About to update mirror: %s" % site)
    os.chdir(os.path.join('/data', 'contents', site))
    print('cd %s' % os.path.realpath(os.curdir))
    run_httrack()
    site_modification()
    rsync_to_apollo()
    return

if __name__ == '__main__':
    appconfig = configparser.ConfigParser()
    appconfig.read(os.path.join('/etc', 'sites.conf'))
    sites = []
    for (dirpath, dirnames, filenames) in os.walk(os.path.join('/data', 'contents')):
        sites.extend(dirnames)
        break

    confSections = appconfig.sections()

    if( len(sys.argv) == 2 and sys.argv[1] in sites and sys.argv[1] in confSections):
        site = sys.argv[1]
        conf = dict(appconfig.items(site))
        do_site_update()
    else:
        print("Usage: %s [%s]" % (sys.argv[0], '|'.join(sites)))


# message = "We have liftoff"
# print(message)
