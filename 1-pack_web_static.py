#!/usr/bin/python3
"""
Fabric script that deploys static sites to a web server
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    with prefix("mkdir -p versions"):
        dt = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
        status = local(f'tar -cf versions/web_static_{dt}.tgz web_static')
        if not status.failed:
            return f"versions/web_static_{dt}.tgz"
        return None
