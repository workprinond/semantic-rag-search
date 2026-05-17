
FROM python:3.10-slim AS builder

WORKDIR /app


RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    wget \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .


RUN pip install --no-cache-dir --user -r requirements.txt


FROM python:3.10-slim

WORKDIR /app


RUN apt-get update && apt-get install -y \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*


COPY --from=builder /root/.local /root/.local


ENV PATH=/root/.local/bin:$PATH


COPY . .


RUN mkdir -p data


EXPOSE 8000


ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app


CMD ["python", "main.py"]
