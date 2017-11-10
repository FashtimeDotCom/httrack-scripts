#!/usr/bin/python

import logging
import sys
from time import sleep
from daemonize import Daemonize

pidfile = '/tmp/myservice-py-test.pid'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propogate = False
fh = logging.FileHandler("/var/log/myservice.log", "w")
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
keep_fds = [fh.stream.fileno()]


def main():
    while True:
        sleep(5)

daemon = Daemonize(app="myservice", pid=pidfile, action=main, keep_fds=keep_fds)
daemon.start()

