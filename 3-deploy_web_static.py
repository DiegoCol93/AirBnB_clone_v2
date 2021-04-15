#!/usr/bin/python3
""" Module for storing the deploy method for fabric. """
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """ Method for deploying using the previous fabric methods. """
    return(do_deploy("version/{}".format(do_pack().split("/")[-1])))
