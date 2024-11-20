# Overview

The project aims at getting information about special double credit offer from Kaktus mobile operator. The information is available at website https://www.mujkaktus.cz/chces-pridat where the information is published in human readable format - no API available.

Mainly the application is targetted at android platform. However, could be build on desktop, limited to Linux and WSL due to buildozer(p4a). 

# Setup

How to install and setup KAWAG project.

## Ubuntu Setup (Ubuntu 23.04)


### Desktop Application
* Bootstrap python venv
    ```
    python3 -m venv venv
    source ./venv/bin/activate
    pip install -r requirements.txt
    ```

* Run Kivy app
    ```
    python ./src/main.py
    ```

### Android Application

Build is using buildozer and python for android

* Install
* Bootstrap python venv
    ```
    sudo apt update
    sudo apt install python3 python3-pip python3-venv
    python3 -m venv venv
    source ./venv/bin/activate
    pip3 install setuptools buildozer Cython==3.0.11
    ```
* package requirements
    ```
    sudo apt update
    sudo apt install -y git zip unzip openjdk-17-jdk python3-pip  python3-venv autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo6 cmake libffi-dev libssl-dev
    ```
* buildozer command for local android debug build
    ```
    buildozer -v android debug
    ```
* apply android manifest change (To setup broadcast and receiver written in plain java)
    ```
    python ./maintenance/android_manifest_for_broadcast.py
    ```
* buildozer command for deploying android local application build
    ```
    buildozer -v android debug deploy run logcat
    ```

#### Debug on Ubuntu

```
adb install -r bin/*.apk
adb logcat -s "python"
```

## WSL 2 Windows 11 Setup

* Install WSL 2 (Ubuntu) on Windows 11
* Install USB support on WSL 2 [usbipd-win](https://github.com/dorssel/usbipd-win).
    
    On WSL windows part attach USB device:
    ```
    usbipd list
    usbipd attach --wsl --busid 1-3
    ```
    In WSL Ubuntu (no longer needed any setup)
* Install buildozer (https://github.com/kivy/kivy/wiki/Using-Buildozer-on-windows-10-using-WSL)
    ```
    python -m venv venv
    . ./venv/bin/activate
    pip install buildozer
    pip install Cython==0.29.33
    buildozer -v android debug
    ```
* ~~Setup udev rules for adb~~
    ```
    sudo vim /etc/udev/rules.d/51-android.rules
    SUBSYSTEM=="usb", ATTR{product}=="moto g32", ATTR{serial}=="ZY22G2TM9G", MODE="0666", GROUP="plugdev"
    sudo udevadm control --reload-rules && sudo udevadm trigger
    ```

## Docker

### Android

```
docker build -t test -f .\docker\android\Dockerfile .
```