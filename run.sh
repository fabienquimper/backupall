# Run simple script
#sudo docker run -it --rm --name running-backup-server backup-server

# Run expose server
sudo docker run --rm -it --name running-backup-server -p 80:7000 backup-server
echo "Server is running on http://localhost:80"
#sudo docker run -it --rm --name backupserver-running backupserver
#docker run fab .
#docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python your-daemon-or-script.pyx