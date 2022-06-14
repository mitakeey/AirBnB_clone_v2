from fabric.api import *
from fabric import Connection
from invoke import task

@task
def execute(conn):
    conn.run("uname -s")fav -v