# ---  ---
FROM python:3.10-slim AS builder
WORKDIR /app

# 
RUN apt-get update && apt-get install -y --no-install-recommends gcc python3-dev

COPY requirements.txt .
# 
RUN pip install --user --no-cache-dir -r requirements.txt

# ---  ---
FROM python:3.10-slim
WORKDIR /app

# 
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    libxcb1 \
    && rm -rf /var/lib/apt/lists/*

# 
COPY --from=builder /root/.local /root/.local
# 
ENV PATH=/root/.local/bin:$PATH

# 
COPY model.pt .
COPY main.py .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
