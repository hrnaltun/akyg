# İmaj dosyasını al
FROM python:3.11

# Çalışma dizinini belirle
WORKDIR /usr/src/app

# Ortam değişkenlerini ayarla
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Bağımlılıkları yükle
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Projeyi kopyala
COPY . /usr/src/app/

