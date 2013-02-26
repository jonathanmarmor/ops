from fabric.api import task, run, cd


@task
def clone(repo, user='jonathanmarmor'):
    with cd('/home/ubuntu'):
        run('mkdir apps')

    with cd('/home/ubuntu/apps'):
        run('git clone https://github.com/{}/{}.git'.format(user, repo))


# @task
# def clone_private(repo, user):
#     # @todo


@task
def update(repo):
    with cd('/home/ubuntu/apps/{}'.format(repo)):
        run('git reset --hard')
        run('git pull')
