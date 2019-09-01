#!/usr/bin/python3
'''
Fabric script that generates a .tgz archive from the contents
of the web_static folder of my AirBnB Clone repo,
using the function do_pack.
'''
from fabric.api import local
import datetime


def do_pack():
    # Make dir
    local("mkdir -p versions")
    # Variable to run datetime.now() method
    created_time = datetime.datetime.now()
    # Checks commands can run locally; creates tgz file containing
    # web_static html files
    check_local = local("tar -cvzf versions/web_static_{}.tgz web_static".
                        format(created_time.strftime("%Y%m%dT%H%M%S")))
    if check_local.failed:
        return None
    else:
        return check_local
