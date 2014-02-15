from fabric.api import env, roles, run, put
# Define sets of servers as roles

env.roledefs = {
    'production': ['matthewdhowell.com']
}
 
# Set the user to use for ssh
env.hosts = ['servername']
env.directory = '/home/misterinterrupt/.virtualenvs/matthewdhowell.com/bin/python'
env.activate = 'workon matthewdhowell.com'
env.home_path = '/home/misterinterrupt'
env.domain_path = '%(home_path)s/matthewdhowell.com' % {'home_path' : env.home_path}
#env.app_path = '%(domain_path)s/matthewdhowell.com' % {'domain_path' : env.domain_path}
env.git_origin = 'git@github.com:misterinterrupt/matthewdhowell.git'
env.user = 'misterinterrupt'

def virtualenv(command):
    """context for virtualenv"""
    workon = env.activate + '&&'
    run(workon + command)

def django_syncdb(path):
    """sync the django db via manage.py"""
    virtualenv('python %(path)s/manage.py syncdb' % {'path' : path})

def git_reset_checkout(path):
    run ('cd %(path)s; git reset --hard; git checkout master; git pull origin master; ' % {'path' : path})

def copy_passenger_wsgi(path):
    put('passenger_wsgi.py', '%(path)s/passenger_wsgi.py' % {'path' : path})

def install_requirements(path):
    virtualenv('pip install -r %(path)s/basic_requirements.txt' % {'path' : path})

def clone_repo_to_path(repo, path):
    run('git clone %(repo)s %(path)s' % {'repo': repo, 'path' : path})

def delete_path(path):
    """DANGER This Forces a Recursive ReMoval of the given path"""
    run('rm -drf %(path)s' % {'path': path})

# Restrict the function to the 'production' role
@roles('production')
def create_passenger_restart(path):
    """Creates directory called 'tmp' and inside, a passenger restart.txt file"""
    run('mkdir %(path)s/tmp; touch %(path)s/tmp/restart.txt' % {'path': path})

@roles('production')
def passenger_restart(path):
    """Restarts Passenger"""
    run('touch %(path)s/tmp/restart.txt' % {'path' : path})

@roles('production')
def get_version():
    run('cat /etc/issue')

@roles('production')
def production_deploy():
    git_reset_checkout(env.domain_path)
    django_syncdb(env.domain_path)
    copy_passenger_wsgi(env.domain_path)
    install_requirements(env.domain_path)
    passenger_restart(env.domain_path)

@roles('production')
def production_deploy_destructive():
    delete_path(env.domain_path)
    clone_repo_to_path(env.git_origin, env.domain_path)
    copy_passenger_wsgi(env.domain_path)
    create_passenger_restart(env.domain_path)
    install_requirements(env.domain_path)
