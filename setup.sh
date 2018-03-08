#!/bin/bash

sudo apt-get update
sudo apt-get install python-picamera
sudo apt-get install apache2 -y

cd ~
git clone https://github.com/ThyCowLord/Cascade
cd Cascade
yes | sudo cp index.html ~/var/www/html/index.html
yes | sudo cp rc.local /etc/rc.local
sudo chmod a+x /etc/rc.local

sudo update-rc.d apache2 defaults

echo 'Setup complete! Do not delete these files!'
