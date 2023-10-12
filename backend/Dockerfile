FROM python:3.8-slim
WORKDIR /code

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

COPY ./entrypoint.sh .
ENTRYPOINT ["sh", "/code/entrypoint.sh"]
