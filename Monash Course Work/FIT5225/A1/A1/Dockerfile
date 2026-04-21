# --- 第一阶段：编译/安装环境 ---
FROM python:3.10-slim AS builder
WORKDIR /app

# 安装必要的构建工具
RUN apt-get update && apt-get install -y --no-install-recommends gcc python3-dev

COPY requirements.txt .
# 将包安装到指定目录
RUN pip install --user --no-cache-dir -r requirements.txt

# --- 第二阶段：最终运行环境 ---
FROM python:3.10-slim
WORKDIR /app

# 只安装运行 OpenCV 必需的极简库
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 从 builder 阶段把安装好的库考过来
COPY --from=builder /root/.local /root/.local
# 确保系统能找到这些库
ENV PATH=/root/.local/bin:$PATH

# 复制模型和代码
COPY model.pt .
COPY main.py .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
