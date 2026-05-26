# 1. Start with an official, lightweight Python environment
FROM python:3.11-slim

# 2. Set the folder inside the container where our app will live
WORKDIR /app

# 3. Copy our list of packages into the container
# (We will create this requirements file next!)
COPY requirements.txt .

# 4. Install the Python packages inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of our application code into the container
COPY . .

# 6. Expose the port that FastAPI runs on
EXPOSE 8000

# 7. The exact command to run our app automatically when the container starts
CMD ["uvicorn", "cloud_app:app", "--host", "0.0.0.0", "--port", "8000"]