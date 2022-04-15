FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1

COPY ./start.sh /start.sh
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY ./app ./app

RUN chmod +x start.sh

CMD ["./start.sh"]