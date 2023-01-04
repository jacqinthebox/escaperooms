FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN apt-get update && apt-get install -y unixodbc unixodbc-dev
RUN pip install -r requirements.txt
RUN pip install pyodbc

# Copy the application code to the working directory
COPY . .

# Expose the application on port 5000
EXPOSE 5000

# Set the entry point to the Flask application
ENTRYPOINT ["python"]

# Set the command to start the Flask application
CMD ["app.py"]
