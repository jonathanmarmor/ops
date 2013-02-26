from fabric.api import task, sudo, cd


@task
def install(packages):
    if isinstance(packages, str):
        packages = [packages]

    sudo('pip install {}'.format(' '.join(packages)))


@task
def install_requirements(repo):
    with cd('/home/ubuntu/apps/{}'.format(repo)):
        sudo('pip install -r requirements.txt')


@task
def upgrade(packages):
    if isinstance(packages, str):
        packages = [packages]

    sudo('pip install --upgrade {}'.format(' '.join(packages)))
