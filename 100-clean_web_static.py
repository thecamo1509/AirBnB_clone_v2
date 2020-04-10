#!/usr/bin/python3

from fabric.api import local, run, env, put, sudo
from datetime import datetime
from os.path import exists
env.hosts = ["3.84.104.13", "35.237.21.147"]


def do_clean(number=0):
    """Deletes the useless versions"""
    number = int(number)
    local("ls -d -1tr versions/* | tail -n +{} | \
          xargs -d '\n' rm -f --".format(number < 1 ? 2: number + 1))
    run("ls -d -1tr /data/web_static/releases/* | tail -n +{} | \
          xargs -d '\n' rm -rf --".format(number < 1 ? 2: number + 1))
