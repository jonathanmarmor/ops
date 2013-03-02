from fabric.api import env, task

from fab_utils import apt
from fab_utils import git
from fab_utils import npm
from fab_utils import forever


env.repo = 'phase'


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
        'nodejs',
        'npm'
    ])
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


# @task
# def rm_audio():
#     """Delete all files except sample.mp3 from /static/audio/"""

#     # This doesn't work via fab for some reason
#     sudo("""for file in /home/ubuntu/apps/{}/static/audio/*
#     do
#        case "$file" in
#          sample.mp3 ) continue;;
#          * ) rm $file;;
#        esac
#     done""".format(env.repo))

#     # neither does this
#     with cd('/home/ubuntu/apps/{}/static/audio/'.format(env.repo)):
#         run('shopt -s extglob')  # Enables extglob
#         sudo('rm !(sample*)')
#         run('shopt -u extglob')  # Disables extglob
