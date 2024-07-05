FROM python:3.12


WORKDIR /src

WORKDIR /app


COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY . .

ENV PYTHONPATH=/src

CMD [ "fastapi","run","app/main.py" ]