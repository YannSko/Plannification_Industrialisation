# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Set the entrypoint
ENTRYPOINT ["python"]
CMD ["scheduler.py"]
