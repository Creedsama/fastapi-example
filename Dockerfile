# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.11.5

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

# Install pip requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
