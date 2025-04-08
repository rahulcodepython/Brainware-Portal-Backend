FROM python:3.13.1-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

RUN pip install gunicorn

# Copy project files
COPY . .

EXPOSE 8000

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application" ]
