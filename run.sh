# Run simple script
#sudo docker run -it --rm --name running-backup-server backup-server

# Run expose server
#HOSTIP=`ip -4 addr show scope global dev eth0 | grep inet | awk '{print \$2}' | cut -d / -f 1`
#HOSTIP=`ifconfig wlo1 | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'`
HOSTIP=`ifconfig docker0 | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'`
#HOSTIP=172.17.0.1
echo "Your IP is: ${HOSTIP}"
sudo docker run --add-host=docker:$HOSTIP --rm -it --name running-backup-server -p 80:7000 -p 8000:8000 -p 8001:8001 -p 8002:8002 -p 8003:8003 backup-server
echo "Server is running on http://localhost:80"
echo "OSC client are ready on port 8000 (master) 8001 (light slave) 8002 (audio slave) 8003 (video slave)"
#sudo docker run -it --rm --name backupserver-running backupserver
#docker run fab .
#docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python your-daemon-or-script.pyx