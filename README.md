# flaskweb
 flask is a web application frame work written in python
This is an example Flask app, ready to be deployed with a simplified Ansible playbook.

The included deploy playbook will:

Install system apt packages
Clone the repo and install Python requirements in a virtualenv
Configure ufw and systemd
Enable and start services
Check the url for the expected response
The deploy.yml playbook is modeled after the manual steps discussed in this digitalocean article using a Ubuntu ML instance.

Prerequisites
You'll need Ansible installed and SSH access to any hosts. Customize the hosts.ini file as needed.

pip install ansible
git clone https://github.com/johy9/flaskweb.git
cd flaskapp
Deploying the app
Run the deploy playbook.

ansible-playbook deploy.yml
Debugging
Test connection with the host. If needed, configure the ssh agent.

ansible webservers -m ping
ssh-add ~/.ssh/example_rsa
Rerun the playbook 

ansible-playbook deploy.yml -i host.ini
Check the logs on the host.ini

sudo ufw allow 5000  # to undo: sudo ufw delete allow 5000
source env/bin/activate
python app.py
open http://HOSTNAME:5000
If that doesn't work, try running the Flask app with app.run(debug=True)

netstat -plnt
Check all active connections.

netstat -a
If need be, kill any processes using a specific port.

sudo fuser -k 80/tcp
Check facts.
