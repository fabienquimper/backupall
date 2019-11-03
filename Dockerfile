FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
#COPY . .
COPY index.html .
COPY NexusUI.js .
COPY webserver.py .
EXPOSE 7000
#CMD [ "python", "./your-daemon-or-script.py" ]
CMD [ "python", "./webserver.py" ]
#CMD python -m http.server 7000
#CMD python ./webserver-dummy.py -l localhost -p 7000
#CMD [ "python", "./webserver-dummy.py -l localhost -p 7000" ]
#ENTRYPOINT ./webserver-dummy.py -l localhost -p 7000
#CMD [ "python", "./webserver-dummy.py" ]