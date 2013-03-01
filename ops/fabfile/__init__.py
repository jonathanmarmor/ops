from fabric.api import env, task, sudo

# Utilities
import pip
import npm
import git
import forever

# Application-specific tasks
import centaur
import phase


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
