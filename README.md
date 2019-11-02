# Set-up

sudo apt install docker



# Docker group
sudo groupadd docker
sudo usermod -aG docker $USER

# Clean docker
sudo docker system prune

docker images -f dangling=true
docker images purge


# To do

# Server side
> Simple python server with OSC message (listening) ==> To check what is receiving
> Simple python client with OSC message to send on different interface


# Client
> Simple web interface to set different element and send it to a web server (SYNC ALL DATA IN THE SERVE)
