#!/usr/bin/python3
'''
Fabric script that that distributes an archive to web servers,
using the function do_deploy:
'''
from fabric.api import *
import os
# All remote commands must be executed on your both web servers
env.hosts = ['34.74.170.32', '35.229.125.98']


def do_deploy(archive_path):
    # Check if path to file exists
    if not os.path.isfile(archive_path):
        return False
    # Using .split() to remove all before delimeter '/' and all after '.'
    # Split at slash variable = sl
    sl = archive_path.split('/')
    # sl[0] = 'versions' sl[1] = "web_static_2019.. .tgz"
    # Split at dot variable = sd
    sd = sl[1].split('.')
    # sd[0] = "web_static_2019..." sd[1] = "tgz"
    # Checking that archive has uploaded to /tmp/ directory
    check_upload = put(archive_path, "/tmp/{}".format(sl[1]))
    if check_upload.failed:
        return False
    # Uncompress archive to folder /data/web_static/releases
    # <archive filename without extension> on the web server
    u_arch = run("mkdir -p /data/web_static/releases/{}/".format(sd[0]))
    if u_arch.failed:
        return False
    u_arch2 = run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
                  format(sl[1], sd[0]))
    if u_arch2.failed:
        return False
    # Delete the archive from the web server
    del_arch = run("rm /tmp/{}".format(sl[1]))
    if del_arch.failed:
        return False
    u_arch3 = run("mv/data/web_static/releases/{}/web_static/* /data/web_static/releases/{}".format(sd[0], sd[0]))
    if u_arch3.failed:
        return False
    u_arch4 = run("rm -rf /data/web_static/releases/{}/web_static".
                  format(sd[0]))
    if u_arch4.failed:
        return False
    # Delete the symbolic link /data/web_static/current from the web server
    del_sym = run("rm -rf /data/web_static/current")
    if del_sym.failed:
        return False
    # Create a new the symbolic link /data/web_static/current on the
    # web server, linked to the new version of your code
    # (/data/web_static/releases/<archive filename without extension>)
    make_sym = run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(sd[0]))
    if make_sym.failed:
        return False
    # Returns True if all operations have been done correctly
    return True
