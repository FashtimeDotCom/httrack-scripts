#!/usr/bin/env python

import os, sys, time
from daemon import Daemon


class HttrackDaemon(Daemon):
        def run(self):
            sleep(5)

        def pingserver(servername):
                # Check network to server

        def check_free_space():
                # Check there is enough free space on disk
                # This is already monitored by hobbit


        def update(servername):
            mirrorpath = '/data/contents/' + servername
            if (os.access(mirrorpath), os.W_OK):
                os.cwd(mirrorpath)
                print os.getcwd()
            else:
                return


if __name__ == "__main__":
	daemon = HttrackDaemon('/tmp/httrack-daemon.pid')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)
