# Single-stage Production Container for Google Cloud Run
FROM python:3.10-slim
WORKDIR /app

# Install minimal OS dependencies for OpenCV CPU headless
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt ./backend/
# Install lightweight CPU-only PyTorch first to reduce container size and accelerate build
RUN pip install --no-cache-dir torch torchvision --extra-index-url https://download.pytorch.org/whl/cpu && \
    pip install --no-cache-dir -r ./backend/requirements.txt

# Copy backend application code (including pre-compiled static WebGIS dashboard)
COPY backend/ ./backend/

ENV PYTHONUNBUFFERED=1
ENV PORT=8080
ENV STREAM_FPS=28.5
ENV TZ=Asia/Ho_Chi_Minh

EXPOSE 8080

CMD ["sh", "-c", "uvicorn main:app --app-dir backend --host 0.0.0.0 --port ${PORT:-8080}"]
