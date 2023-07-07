# Dockerfile

# Use a base image with Python and Django installed
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the Django project code to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entrypoint script to the container
COPY entrypoint.sh /app/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Expose the port on which your Django app will run
EXPOSE 8000

# Set the entrypoint to run the script
ENTRYPOINT ["/app/entrypoint.sh"]
