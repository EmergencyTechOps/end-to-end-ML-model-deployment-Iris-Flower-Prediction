# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install flask pandas scikit-learn joblib

# Expose port
EXPOSE 5000

# Command to run app
CMD ["python", "app.py"]
