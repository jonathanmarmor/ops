from fabric.api import env, task, cd, run, sudo

import apt
import git
import npm
import forever


env.repo = 'phase'


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
