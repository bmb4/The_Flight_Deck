FROM python:3.9
ENV HOME /root
WORKDIR /root
COPY . .
RUN pip install -r requirements.txt
EXPOSE $PORT
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
RUN chmod +x /wait
CMD /wait
CMD [ "python3", "-u", "main.py" , $PORT]