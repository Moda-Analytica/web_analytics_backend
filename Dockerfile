FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./start.sh /start.sh
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY ./app ./

RUN chmod +x /app/start.sh

CMD ["./start.sh"]