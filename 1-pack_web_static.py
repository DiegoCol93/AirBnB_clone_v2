#!/usr/bin/python3
""" Module for storing the do_pack() method. """


def do_pack():
    """ Packs the contents of the /web_static directory in .tgz """
    from datetime import datetime
    from fabric.api import local
    from os import path

    if path.exists("./versions") is False:
        local("mkdir versions")

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(time)
    try:
        local("tar -cvzf {} web_static".format(file_name))
        return(file_name)
    except Exception as e:
        return(None)
