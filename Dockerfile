FROM python:3.12.3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

# Expose the port server is running on
EXPOSE 8000

# Start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
