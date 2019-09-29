FROM python:3.6

# Install dependencies
RUN pip install pandas \
  numpy

# Move to the app folder
RUN mkdir /app
WORKDIR /app

# Copy our python program for training and inference
COPY ./*.py ./*.sh ./

# Add executable permission to Bash scripts
RUN chmod +x train.sh infer.sh