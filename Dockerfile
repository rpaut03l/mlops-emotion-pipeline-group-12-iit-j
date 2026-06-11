FROM python:3.11-slim
ARG HF_MODEL_NAME=G25AIT2134/distilbert-emotion
ENV HF_MODEL_NAME=${HF_MODEL_NAME}
ENV HF_TOKEN=${HF_TOKEN}
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu \
 && pip install --no-cache-dir transformers huggingface_hub
COPY src/inference.py ./src/inference.py
ENTRYPOINT ["python", "src/inference.py"]
