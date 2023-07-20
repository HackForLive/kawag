# Overview

The project aims at getting information about special double credit offer from Kaktus mobile operator. The information is available at website https://www.mujkaktus.cz/chces-pridat where the information is published in human readable format - no API available.

Mainly the application is targetted at android platform. However, could be build on desktop, Ubuntu 23.04 tested. 

# Setup

How to install and setup KAWAG project.

## Desktop (Ubuntu 23.04)

* Create python venv
    ```
    python3 -m venv venv
    ```

* Activate venv
    ```
    source ./venv/bin/activate
    ```

* Install requirements

    ```
    pip install -r requirements.txt
    ```


* Install google chromedriver for selenium - works,  mozilla has issues with snapd
## Android Setup

Official guide available at:
https://kivy.org/doc/stable/guide/packaging-android.html


### Build on Ubuntu

* package requirements
    ```
    sudo apt update
    sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
    ```
* buildozer android command for build, deploy to mobile
    ```
    buildozer android debug deploy run
    ```

### Debug on Ubuntu

```
buildozer -v android debug
adb install -r bin/*.apk
adb logcat -s "python"
```

### Auto Restart Service

https://github.com/kivy/python-for-android/pull/1374
https://github.com/kivy/python-for-android/pull/643
https://habr.com/ru/articles/694906/