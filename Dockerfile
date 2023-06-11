FROM python:3.10

ENV PATH="/home/machine/.local/bin:${PATH}"

RUN groupadd -r machine && useradd -m -r -g machine machine

RUN apt-get update && apt-get install -y \
    nmap \
    avahi-utils \
    && rm -rf /var/lib/apt/lists/*

COPY --chown=machine:machine sentinel /app/sentinel

USER machine

WORKDIR /app/sentinel

RUN pip install --user --upgrade pip
RUN pip install --user -r requirements.txt --no-cache-dir

CMD ["python", "main.py"]
