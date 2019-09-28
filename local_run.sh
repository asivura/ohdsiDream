#!/usr/bin/env bash

echo "Building docker container..."
docker build -t  docker.synapse.org/syn20822908/dummy-model app

echo "Running train.sh with docker container..."
docker run -v $(pwd)/data/syn20685954/training:/train:ro \
           -v $(pwd)/scratch:/scratch:rw \
           -v $(pwd)/model:/model:rw docker.synapse.org/syn20822908/dummy-model \
           bash /app/train.sh

echo "Running infer.sh with docker container..."
docker run -v $(pwd)/data/syn20685954/evaluation:/infer:ro \
           -v $(pwd)/scratch:/scratch:rw \
           -v $(pwd)/output:/output:rw \
           -v $(pwd)/model:/model:rw \
           docker.synapse.org/syn20822908/dummy-model \
           bash /app/infer.sh