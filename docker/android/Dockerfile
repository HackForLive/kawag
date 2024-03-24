FROM ubuntu:latest

# Installation Directory
ENV INSTALL_PATH /app
# Set the working directory to /app
WORKDIR $INSTALL_PATH

# Copy the parent directory contents into the container at /app
COPY . $INSTALL_PATH


RUN apt update
RUN apt install -y python3 python3-pip python3-venv
RUN python3 -m venv venv
RUN . ./venv/bin/activate
RUN pip3 install buildozer Cython==0.29.33
RUN apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config \
                   zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

RUN echo "y" | buildozer -v android debug
RUN python3 ./maintenance/android_manifest_for_broadcast.py
RUN echo "y" | buildozer -v android debug
