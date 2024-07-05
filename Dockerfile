FROM python:3.12

<<<<<<< HEAD
WORKDIR /src
=======
WORKDIR /app
>>>>>>> 25969c028fce6ef756b1ca3c6d2c658a0a2e276c

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY . .

ENV PYTHONPATH=/src

CMD [ "fastapi","run","app/main.py" ]