sudo apt-get update
sudo apt install python3-pip
sudo apt install docker.io -y
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-Linux-x86_64" -o /usr/local/bin/docker-compose 
sudo chmod +x /usr/local/bin/docker-compose 
sudo chmod 777 /var/run/docker.sock
pip install -r requirements.txt 