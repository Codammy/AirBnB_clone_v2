#!/usr/bin/python3
"""
Script that distributes an archive to my web servers,
using the functions below
"""
from datetime import datetime
from fabric.api import *
import sys


env.hosts = ['54.237.48.59', '54.144.249.31']
# env.user = "ubuntu"


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    """
    dt = datetime.today()
    file_path = "web_static_{}{}{}{}{}{}.tgz".format(
            dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
            )
    with prefix("mkdir -p versions"):
        status = local("tar -cvzf versions/{} web_static".format(file_path))
        if status.succeeded:
            return "versions/{}".format(file_path)
    return None


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    """
    archive = archive_path.split('/')[-1]
    fold = '/data/web_static'

    status = put(archive_path, '/tmp')
    if not status.succeeded:
        return False
    with prefix("mkdir -p {}/releases/{}".format(fold, archive[:-4])):
        status = sudo('tar -xzf /tmp/{} -C {}/releases/{}'
                      .format(archive, fold, archive[:-4]))
    status = sudo('rm /tmp/{}'.format(archive))
    status = sudo('mv {}/releases/{}/web_static/* {}/releases/{}/'
                  .format(fold, archive[:-4], fold, archive[:-4]))
    with prefix('rm -rf {}/current'.format(fold)):
        status = sudo('ln -fs /data/web_static/releases/{} {}/current'
                      .format(archive[:-4], fold))

    if status.succeeded:
        return True
    return False
