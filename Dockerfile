FROM python:3
#RUN pip install python-osc
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
#COPY . .
COPY index.html .
COPY NexusUI.js
EXPOSE 7000
#CMD [ "python", "./your-daemon-or-script.py" ]
#CMD [ "python", "./webserver.py" ]
#CMD python -m http.server 7000
CMD python ./webserver-dummy.py -l localhost -p 7000