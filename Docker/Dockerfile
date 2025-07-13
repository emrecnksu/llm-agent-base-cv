# Python:3.12 tabanlı bir sistem oluşturur
FROM python:3.12

# Sistem bağımlılıkları
RUN apt-get update && apt-get install -y \
    build-essential \
    libpango1.0-0 \
    libpangoft2-1.0-0 \
    libpangocairo-1.0-0 \
    libcairo2 \
    libffi-dev \
    libssl-dev \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Çalışma dizinini ayarla
WORKDIR /app

# Bağımlılık dosyalarını kopyala
COPY requirements.txt .

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Başlangıç dosyasını kopyala
COPY Docker/start-container /usr/local/bin/start-container
RUN chmod +x /usr/local/bin/start-container && sed -i 's/\r$//' /usr/local/bin/start-container

# 8000 portunu aç
EXPOSE 8000

ENTRYPOINT ["start-container"]
