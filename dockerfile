FROM python:3.7-slim
WORKDIR /app
COPY . /app/
RUN apt-get update && apt-get install -y fonts-dejavu-core \
    && pip install --upgrade pip \
    && pip install -r requirements.txt
CMD ["python", "bot.py"]