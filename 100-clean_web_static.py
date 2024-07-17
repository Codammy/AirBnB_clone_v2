#!/usr/bin/python3
"""
Fabric script that deploys static sites to a web server
"""
from fabric.api import *
from datetime import datetime


env.hosts = ["34.239.250.147", "54.174.134.107"]
# env.user = "ubuntu"


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    with prefix("mkdir -p versions"):
        dt = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
        status = local(f'tar -cf versions/web_static_{dt}.tgz web_static')
        if not status.failed:
            return f"versions/web_static_{dt}.tgz"
        return None


def do_deploy(archive_path):
    """destribute archive to web server"""
    if put(archive_path, "/tmp/").failed:
        return False

    new_version_path = "{}/{}".format(
                     "/data/web_static/releases/",
                     archive_path.strip("versions/").strip(".tgz"))

    with prefix(f"mkdir -p {new_version_path}"):
        if run(f"tar -xf /tmp/{archive_path.strip('/versions')} \
                 -C {new_version_path}").failed:
            return False

    if run(f"mv {new_version_path}/web_static/* {new_version_path}").failed:
        return False

    if run(f"rm -rf /tmp/{archive_path}").failed:
        return False

    if run(f"rm -rf /data/web_static/current").failed:
        return False

    stat = run(f"ln -fs {new_version_path} /data/web_static/current")

    if stat.failed:
        return False
    return True


def deploy():
    """make a full deployment by calling do_pack and do_deploy"""
    return do_deploy(do_pack())

def do_clean(number=0):
    """deletes out-of-date archives, making the server clean"""
    local(f"rm $(ls -lt versions | head {number}-)")
    run(f"rm $(ls -lt /data/web_static/releases | head {number}-)").
