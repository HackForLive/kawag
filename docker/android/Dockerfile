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
# setuptools contains distutils
RUN . ./venv/bin/activate && pip3 install Cython==0.29.33 buildozer setuptools
RUN apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config \
                   zlib1g-dev libncurses5-dev libncursesw5-dev cmake libffi-dev libssl-dev

# to run lsusb
RUN apt install usbutils

RUN  . ./venv/bin/activate && echo "y" | buildozer -v android debug
RUN python3 ./maintenance/android_manifest_for_broadcast.py
RUN  . ./venv/bin/activate && echo "y" | buildozer -v android debug
