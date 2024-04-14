FROM python:3.10.13-slim-bookworm 

WORKDIR /auto-reports

RUN apt-get update
RUN apt-get install -y git

ENV VIRTUAL_ENV=/workspace.venv \
    PATH="/workspace/.venv/bin:$PATH"

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "./app/app.py"]
