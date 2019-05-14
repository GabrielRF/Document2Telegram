FROM python:3.7-alpine

RUN pip install pytelegrambotapi
RUN pip install inotify

ADD doc2tg.py / 

CMD [ "python", "./doc2tg.py" ]
