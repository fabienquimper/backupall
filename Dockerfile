FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
#COPY . .
COPY index.html .
COPY NexusUI.js .
COPY main.py .
COPY osc_communication.py .
COPY webserver.py .
COPY player.py .
COPY geocyclab-datas.csv .
COPY dataobj.py .
COPY datajson.py .
#7000 is the webserver
#8000 is for OSC for MASTER
#8001 is for OSC for LIGTH SLAVE
#8002 is for OSC for AUDIO SLAVE
#8003 is for OSC for VIDEO SLAVE
EXPOSE 7000 8000 8001 8002 8003
#CMD [ "python", "./your-daemon-or-script.py" ]
CMD [ "python", "./main.py" ]
#CMD python -m http.server 7000
#CMD python ./webserver-dummy.py -l localhost -p 7000
#CMD [ "python", "./webserver-dummy.py -l localhost -p 7000" ]
#ENTRYPOINT ./webserver-dummy.py -l localhost -p 7000
#CMD [ "python", "./webserver-dummy.py" ]