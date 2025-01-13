FROM python:3.12

RUN apt-get update && apt-get install -y libaio1 wget unzip && rm -rf /var/lib/apt/lists/*

ENV TZ=America/Sao_Paulo

RUN wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip && \
    unzip instantclient-basiclite-linuxx64.zip -d /usr/lib/oracle && \
    rm instantclient-basiclite-linuxx64.zip && \
    echo "/usr/lib/oracle/instantclient_21_1" > /etc/ld.so.conf.d/oracle-instantclient.conf && \
    ldconfig

WORKDIR /app
RUN mkdir -p /app && chmod -R 777 /app

COPY requirements.txt .
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV LD_LIBRARY_PATH=/usr/lib/oracle/instantclient_21_1:$LD_LIBRARY_PATH

CMD ["python", "main.py"]
