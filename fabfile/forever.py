from fabric.api import task, run, cd, sudo
from fabric.contrib.files import exists


@task
def start(repo, node_env='development'):
    """Start a node service with logging."""

    base = '/home/ubuntu/apps/{}'.format(repo)
    cmd = '{}/index.js'.format(base)

    log_dir = '{}/log'.format(base)
    logs = '{}/{}'.format(log_dir, repo)
    forever_log = '{}.forever.log'.format(logs)
    out_log = '{}.out.log'.format(logs)
    err_log = '{}.err.log'.format(logs)

    if not exists(log_dir):
        run('mkdir {}'.format(log_dir))

    with cd(base):
        sudo('NODE_ENV={} forever start -a -l {} -o {} -e {} {}'.format(
            node_env, forever_log, out_log, err_log, cmd))


@task
def stop(repo):
    base = '/home/ubuntu/apps/{}'.format(repo)
    cmd = '{}/index.js'.format(base)
    sudo('forever stop {}'.format(cmd))


@task
def restart(repo):
    base = '/home/ubuntu/apps/{}'.format(repo)
    cmd = '{}/index.js'.format(base)
    sudo('forever restart {}'.format(cmd))


@task
def list():
    sudo('forever list')
