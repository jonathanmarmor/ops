from fabric.api import task

from fab_utils import apt
from fab_utils import git
from fab_utils import npm
from fab_utils import forever


REPO = 'centaur'


@task
def install():
    apt.add_repository('ppa:chris-lea/node.js')
    apt.update()
    apt.install([
        'gcc',
        'make',
        'g++',
        'git',
        'python',
        'python-software-properties',
        'nodejs'
    ])
    git.clone(REPO)
    npm.install(REPO)
    npm.install_globals('forever')
    start()


@task
def start():
    forever.start(REPO)


@task
def stop():
    forever.stop(REPO)


@task
def restart():
    forever.restart(REPO)


@task
def deploy(rm_node_modules=False):
    git.update(REPO)
    if rm_node_modules:
        npm.rm_node_modules(REPO)
    npm.install(REPO)
    restart()
