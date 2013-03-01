from fabric.api import env, task

from fab_apt import apt

import git
import npm
import forever


env.repo = 'centaur'


@task
def install():
    apt.install()
    git.clone(env.repo)
    npm.install(env.repo)
    npm.install_globals('forever')
    start()


@task
def start():
    forever.start(env.repo)


@task
def stop():
    forever.stop(env.repo)


@task
def restart():
    forever.restart(env.repo)


@task
def deploy(rm_node_modules=False):
    git.update(env.repo)
    if rm_node_modules:
        npm.rm_node_modules(env.repo)
    npm.install(env.repo)
    restart()
