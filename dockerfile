FROM python:3.9-bullseye

# Copy source
WORKDIR /app
COPY . .

# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./flask_app.py" ]