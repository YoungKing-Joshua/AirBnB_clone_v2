#!/usr/bin/python3
"""
Script genereates a .tgz archive from pack
executww: do_pack of the web_tatic folder
Creates the versions folder if it doesn't exist
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    Create&archive .tgz archive web_static folder.
    """

    ytm = datetime.now()
    hive = 'web_static_' + ytm.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    earth = local('tar -cvzf versions/{} web_static'.format(hive))
    if earth is not None:
        return hive
    else:
        return None
