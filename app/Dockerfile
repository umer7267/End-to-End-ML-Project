FROM python:3.14

WORKDIR /workspace

# Copy requirements.txt from the root build context
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy only the app directory into the container
COPY app ./app

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]