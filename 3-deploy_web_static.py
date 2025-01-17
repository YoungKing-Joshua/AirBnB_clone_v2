#!/usr/bin/python3
"""
Fabric script for deploying the web_static content to web servers.
This script builds on the functionality of do_pack and do_deploy.
Usage: fab -s web_static.js deploy -i ~/.ssh/rsa -u ubuntu
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

env.hosts = ['54.210.52.15', '54.172.81.139']


def do_pack():
    """
    Generates a compressed tar archive (tgz).
    """
    try:
        et = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir -p versions")
        me_f = "versions/web_static_{}.tgz".format(et)
        local("tar -cvzf {} web_static".format(me_f))
        return me_f
    except Exception as e:
        print("Error with deployment:", str(e))
        return None


def do_deploy(archive_path):
    """
    Distributes the compressed tar archive (tgz) to the web servers.
    """
    if exists(archive_path) is False:
        return False
    try:
        n_f = archive_path.split("/")[-1]
        xt_re = n_f.split(".")[0]
        rectory = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(rectory, xt_re))
        run('tar -xzf /tmp/{} -C {}{}/'.format(n_f, rectory, xt_re))
        run('rm /tmp/{}'.format(n_f))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(rectory, xt_re))
        run('rm -rf {}{}/web_static'.format(rectory, xt_re))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(rectory, xt_re))
        return True
    except Exception as e:
        print("Error in deployment:", str(e))
        return False


def deploy():
    """
    Generates and distributes a tar archive (tgz) to web servers.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

