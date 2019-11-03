# Run simple script
#sudo docker run -it --rm --name running-backup-server backup-server

# Run expose server
sudo docker run --rm -it --name running-backup-server -p 80:7000 -p 8000:8000 -p 8001:8001 -p 8002:8002 -p 8003:8003 backup-server
echo "Server is running on http://localhost:80"
echo "OSC client are ready on port 8000 (master) 8001 (light slave) 8002 (audio slave) 8003 (video slave)"
#sudo docker run -it --rm --name backupserver-running backupserver
#docker run fab .
#docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python your-daemon-or-script.pyx