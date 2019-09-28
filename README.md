**EHR DREAM Challenge**
> To be updated ...


docker run -v $(pwd)/data/syn20685954/training:/train:ro \
-v $(pwd)/scratch:/scratch:rw \
-v $(pwd)/model:/model:rw \
docker.synapse.org/syn20822908/dummy-model \
bash /app/train.sh


docker run -v $(pwd)/data/syn20685954/evaluation:/infer:ro \
-v $(pwd)/scratch:/scratch:rw \
-v $(pwd)/output:/output:rw \
-v $(pwd)/model:/model:rw \
docker.synapse.org/syn20822908/dummy-model \
bash /app/infer.sh

docker login docker.synapse.org

docker push docker.synapse.org/syn20822908/dummy-model

https://www.synapse.org/#!Synapse:syn20822908/docker