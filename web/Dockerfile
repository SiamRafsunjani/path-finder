FROM python:3.9-slim
EXPOSE 5000
WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r ./requirements.txt

COPY . /app
CMD ["flask", "run", "--host", "0.0.0.0"]
