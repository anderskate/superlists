Maintenance of the new site
================================ 
## Required packages:
* nginx
* Python 3.6
* virtualenv + pip * Git

For example, in Ubuntu:
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get install nginx git python36 python3.6-venv

## Configuration for Nginx virtual host

* in 'nginx.template.conf' file
* change SITENAME, for example, to staging.my-domain.com  

## Systemd Service

* in 'gunicorn-systemd.template.service' file
* change SITENAME, for example, to staging.my-domain.com

## Folder structure

    /home/username 

    └── sites

         └── SITENAME
                
                ├── database
        
                ├── source
        
                ├── static
        
                └── virtualenv

