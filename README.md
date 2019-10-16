Install Python PIP

    sudo apt-get install python-pip

Install virtualenvwrapper

    sudo pip3 install virtualenvwrapper
    sudo pip3 install --upgrade virtualenv


Create www directory where project sites and environment dir

    mkdir /var/www && mkdir /var/envs && mkdir /var/envs/bin


Add these to your bashrc virutualenvwrapper work

    export WORKON_HOME=/var/envs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    export PROJECT_HOME=/var/www
    export VIRTUALENVWRAPPER_HOOK_DIR=/var/envs/bin
    source /usr/local/bin/virtualenvwrapper.sh

Create virtualenv

    cd /var/envs && mkvirtualenv --python=/usr/bin/python3 link
    
Install requirements for a project.

    cd /var/www/link && pip install -r requirements.txt

##Database creation
###For psql

    sudo su - postgres
    psql
    CREATE DATABASE link;
    CREATE USER link_user WITH password 'root';
    GRANT ALL privileges ON DATABASE link TO link_user;
    
Running migrations

    python3 manage.py migrate


##Run project

    python3 manage.py runserver