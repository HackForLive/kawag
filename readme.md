# Setup

* Create python venv
    ```
    python3 -m venv venv
    ```

* Activate venv
    ```
    source ./kivy_venv/bin/activate
    ```

* Install requirements
    > kivy quick fix with python 3.11 (https://github.com/kivy/kivy/issues/8042)

    ```
    python -m pip install kivy --pre --no-deps --index-url https://kivy.org/downloads/simple/
    python -m pip install "kivy[base]" --pre --extra-index-url https://kivy.org/downloads/simple/
    ```

    ```
    pip3 install -r requirements.txt
    ```

* Install google chromedriver for selenium
    ```
    https://github.com/mozilla/geckodriver/releases/download/v0.32.2/geckodriver-v0.32.2-linux64.tar.gz
    tar -xf geckodriver-v0.32.2-linux64.tar.gz
    sudo mv geckodriver /usr/bin/geckodriver
    ```
## 1. Android Setup

Guide:
https://kivy.org/doc/stable/guide/packaging-android.html

Python for android: 
https://python-for-android.readthedocs.io/en/latest/quickstart/

```
p4a apk --private $HOME/git/kawag --package=org.kawag --name "KAWAG" --version 0.1 --bootstrap=sdl2 --requirements=python3,kivy --sdk-dir '/home/michael/Android/Sdk/platforms/android-33' --ndk-dir '/home/michael/Android/Sdk/ndk/25.2.9519653' --android-api '33' --ndk-api '31'
```

### Debug

```
buildozer -v android debug
adb install -r bin/*.apk
adb logcat -s "python"
```