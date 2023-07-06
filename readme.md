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
    > kivy issue with python 3.11 fixed! (https://github.com/kivy/kivy/issues/8042)

    ```
    pip3 install -r requirements.txt
    ```

* Install google chromedriver for selenium - works,  mozilla has issues with snapd
## 1. Android Setup

Guide:
https://kivy.org/doc/stable/guide/packaging-android.html

Python for android: 
https://python-for-android.readthedocs.io/en/latest/quickstart/


### Debug

```
buildozer -v android debug
adb install -r bin/*.apk
adb logcat -s "python"
```