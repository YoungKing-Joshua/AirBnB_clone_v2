#!/usr/bin/python3
"""
script (based on the file your web servers)
thsi huech skue
describes what the function nstead
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['54.210.52.15', '54.172.81.139']


def do_deploy(archive_path):
    """hive web distribut server oih"""
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
        print("Error:", str(e))
        return False
