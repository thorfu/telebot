FROM python:3.7-slim
WORKDIR /app
COPY . /app/
RUN apt-get update
RUN apt-get install -y fonts-dejavu-core
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]