FROM python:3.8-slim

# Install the FastAPI and uvicorn dependencies
RUN pip install fastapi uvicorn

# Add your FastAPI app code
ADD main.py /app/main.py

# Set the working directory to the app directory
WORKDIR /app

# Run the app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
