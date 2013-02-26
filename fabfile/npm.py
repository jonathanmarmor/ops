from fabric.api import task, cd, sudo


@task
def install(repo):
    with cd('/home/ubuntu/apps/{}'.format(repo)):
        sudo('npm install')


@task
def install_globals(packages):
    if isinstance(packages, str):
        packages = [packages]

    sudo('npm install -g {}'.format(' '.join(packages)))


@task
def rm_node_modules(repo):
    with cd('/home/ubuntu/apps/{}'.format(repo)):
        sudo('rm -rf node_modules')
