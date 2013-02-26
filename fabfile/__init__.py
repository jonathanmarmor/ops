from fabric.api import env, task, sudo

# utilities
import apt
import pip
import npm
import git
import forever


# Fabric config
env.warn_only = True
env.user = 'ubuntu'


@task
def easy_install(packages):
    if isinstance(packages, str):
        packages = [packages]

    sudo('easy_install {}'.format(' '.join(packages)))


@task
def install_pip():
    easy_install('pip')
    pip.upgrade('pip')
