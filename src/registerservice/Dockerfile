FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the working directory
# COPY src/registerservice/requirements.txt .
COPY requirements.txt .

# Install the dependencies
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update && apt-get install -y unixodbc unixodbc-dev
RUN pip install -r requirements.txt
RUN pip install pyodbc

RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN apt-get install -y libgssapi-krb5-2

# Copy the application code to the working directory
COPY app/ .

# Expose the application on port 5000
EXPOSE 5000

# Set the entry point to the Flask application
ENTRYPOINT ["python"]

# Set the command to start the Flask application
# CMD ["src/registerservice/app/main.py"]
CMD ["main.py"]