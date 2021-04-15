#!/usr/bin/python3
""" Module for storing the do_deploy method for fabric. """
from fabric.api import put, run, env
from os.path import exists

env.hosts = ['ubuntu@34.75.21.202', 'ubuntu@35.185.122.161']


def do_deploy(archive_path):
    """ Deploys the content of the web_static file to my web servers. """

    if archive_path is None or exists(archive_path) is False:
        return(False)
    archive_name = archive_path.split("/")[1].split(".")[0]

    put(archive_path, "/tmp/")
    run("mkdir -p /data/web_static/releases/{}".format(archive_name))
    run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}"
        .format(archive_name, archive_name))
    run("rm /tmp/{}.tgz".format(archive_name))
    run("mv /data/web_static/releases/{}/web_static/* "
        "/data/web_static/releases/{}/"
        .format(archive_name, archive_name))
    run("rm -rf /data/web_static/releases/{}/web_static")
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{} /data/web_static/current"
        .format(archive_name, archive_name))
