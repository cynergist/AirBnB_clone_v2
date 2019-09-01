#!/usr/bin/python3
'''
Fabric script that creates and distributes an archive to my web servers,
using the function deploy
'''
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
from fabric.api import *
import os
import datetime


def deploy():
    # Call do_pack() function and store the path of the created archive
    path_archive = do_pack()
    if path_archive is None:
        return False
    return do_deploy(path_archive)
