FROM rocker/rstudio:latest

RUN echo deb http://ftp.de.debian.org/debian testing main >> /etc/apt/sources.list
RUN echo 'APT::Default-Release "stable";' | tee -a /etc/apt/apt.conf.d/00local
RUN apt-get update && apt-get install -y default-jdk \
                                         default-jre \
                                         libxml2-dev \
                                         libgit2-dev \
                                         libmagick++-dev \
                                         python3 \
                                         python3-pip \
                                         python-dev
RUN pip3 install numpy \
                 pandas \
                 scipy \
                 h5py \
                 scikit-learn \
                 tensorflow \
                 keras \
                 torch

## Install OHDSI R packages
RUN mkdir -p /opt/software/setup/R
ADD install_packages.r /opt/software/setup/R/
RUN Rscript /opt/software/setup/R/install_packages.r


# Move to the app folder
RUN mkdir /app
WORKDIR /app

# Copy our python program for training and inference
COPY ./src/*.py ./src/*.sh ./

# Add executable permission to Bash scripts
RUN chmod +x train.sh infer.sh