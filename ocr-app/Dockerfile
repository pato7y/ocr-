# Use official Python image
FROM python:3.13

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Tesseract OCR
RUN apt-get update && apt-get install -y tesseract-ocr

# Copy the application files
COPY app/ .

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
