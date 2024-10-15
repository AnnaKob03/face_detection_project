# используем базовый образ Python версии 3.12 на основе slim
FROM python:3.12-slim 
# обновление пакетов и установка зависимостей для opencv
RUN apt-get update && apt-get install -y \ 
    libopencv-dev \
    python3-opencv \
    && rm -rf /var/lib/apt/lists/*
# обнавление пакетов и установка зависимостей для opencv
COPY requirements.txt /app/requirements.txt 
# установка зависимостей python
RUN pip install --no-cache-dir -r /app/requirements.txt 
# копирование файлов в контейнер
COPY . /app
# установка директории внутри контейнера 
WORKDIR /app
# команда запуска скрипта при старте  
CMD ["python", "face_detection.py"] 
