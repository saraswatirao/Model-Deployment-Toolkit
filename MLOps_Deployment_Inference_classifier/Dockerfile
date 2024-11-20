# Use the official Python image with the specified version
FROM python:3.7.16

# Set the working directory in the container
WORKDIR /app

# Copy the local directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the specified port
EXPOSE $PORT

# Command to run the application
CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:$PORT", "clientApp:app"]
