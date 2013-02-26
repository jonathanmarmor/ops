from fabric.api import task, sudo


@task
def install(packages=[], node=True):
    if isinstance(packages, str):
        packages = [packages]

    if not packages:
        # Some packages we'll probably need
        packages = [
            'gcc',
            'make',
            'g++',
            'git',
            'python',
            'python-software-properties',
            'nodejs',
            'npm'
        ]

    if node:
        # Add node repo
        sudo('add-apt-repository ppa:chris-lea/node.js')
        sudo('apt-get update')

    sudo('DEBIAN_FRONTEND=noninteractive apt-get install -y {}'.format(
        ' '.join(packages)))
