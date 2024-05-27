#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from
the contents of the web_static folder
"""
from datetime import datetime
from fabric.api import (prefix, local)


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    """
    dt = datetime.now()
    tarfile = 'web_static_{}{}{}{}{}{}.tgz'.format(
            dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
            )
    with prefix('mkdir -p versions'):
        path = local('tar -cvzf versions/{} web_static'.format(tarfile))
        if path.succeeded:
            return f"versions/{tarfile}"
    return None
