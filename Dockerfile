FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/ ./src/

CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0"]