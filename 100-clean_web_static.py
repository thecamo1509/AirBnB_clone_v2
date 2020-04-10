#!/usr/bin/python3

from fabric.api import local, run, env, put, sudo
from datetime import datetime
from os.path import exists
env.hosts = ["3.84.104.13", "35.237.21.147"]


def do_clean(number=0):
    """Deletes the useless versions"""
    try:
        stat("versions")
    except Exception:
        pass
    if number == "0" or number == "1":
        number = 1
    number = int(number)
    loc = local("ls -t versions/", capture=True)
    loc = str(loc).split("\n")
    n = len(loc)
    for i in range(number, n):
        local("rm versions/{}".format(loc[i]))
        name = loc[i].split(".")
        name = name[0]
        run("rm -rf /data/web_static/releases/{}/".format(name))
