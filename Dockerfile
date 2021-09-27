FROM python:3.9
ENV HOME /root
WORKDIR /root
COPY . .
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD python3 main.py $PORT
