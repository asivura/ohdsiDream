# EHR DREAM Challenge. ohdsiDream Team
More information is available here: 
https://forums.ohdsi.org/t/ehr-dream-challenge-patient-mortality/8028/27

# Installation
## Download Synthetic Data

Install Python3 and pip (in case you don't have it)

https://wiki.python.org/moin/BeginnersGuide/Download

https://pip.pypa.io/en/stable/installing/

Install python dependencies:
```bash
cd <path-to-repo-directory>/data
pip install -r requirements.txt
```
Download and uncompress synthetic data:
```bash
cd <path-to-repo-directory>/data
python download-synthetic-data.py \
       --synapse_username  <your-synapse-login>  \
       --synapse_password <your-synapse-password>
```
```download-synthetic-data.py``` downloads data from synapse and uncompresses it and creates directories for Docker volumes. You should run it only once on your machine.

Data description is available here https://www.synapse.org/#!Synapse:syn18405991/wiki/595493

## Install docker on your machine
For Mac: https://docs.docker.com/docker-for-mac/install/

For Windows https://docs.docker.com/docker-for-windows/install/


## Train and evaluate model on your machine using synthetic data

**Note:** Currenty we are training dummy model to make sure everything works correctly and we can do submissions for the challenge. 

Information about requiered docker container and submission is avalable here: https://www.synapse.org/#!Synapse:syn18405991/wiki/595495

### Build and run docker container on your machine
You can build docker container with this command:
```bash
cd <path-to-repo-directory>
docker build -t docker.synapse.org/syn20822908/dummy-model app
```
You can train the model with this command:
```bash
cd <path-to-repo-directory>
docker run -v $(pwd)/data/syn20685954/training:/train:ro \
           -v $(pwd)/data/scratch:/scratch:rw \
           -v $(pwd)/data/model:/model:rw \
           docker.synapse.org/syn20822908/dummy-model \
           bash /app/train.sh
```
You can evaluate the model and create file with predictions after train it with this command:
```bash
cd <path-to-repo-directory>
docker run -v $(pwd)/data/syn20685954/evaluation:/infer:ro \
           -v $(pwd)/data/scratch:/scratch:rw \
           -v $(pwd)/data/output:/output:rw \
           -v $(pwd)/data/model:/model:rw \
           docker.synapse.org/syn20822908/dummy-model \
           bash /app/infer.sh
```
**Note:** Whenever you make any changes in the code in "app" directory you should re-build docker container again. You can use a script ```local_run.sh``` to run "build", "train" and "evaluate" as a single command. 

All docker volumes are available in "data" directory after run

## Upload Docker Image to synapse
Make sure everything works correctly on your machine.

Answer the questions after the following command:
```bash
docker login docker.synapse.org
```
You may now push your docker image to synapse
```bash
docker push docker.synapse.org/syn20822908/dummy-model
```

Verify the Docker image was successfully pushed(optional):

https://www.synapse.org/#!Synapse:syn20822908/docker

Submit docker image using button in the bottom of this page:

1. Open https://www.synapse.org/#!Synapse:syn20822908/docker/
2. Select docker.synapse.org/syn20822908/dummy-model
3. In right upper conner select "Docker repository tools"
4. Select "Submit Docker Repository to Challenge"
5. Select tag
6. Select "EHR DREAM Challenge Fast Lane"
 