# Setup

* Create python venv
    ```
    python3 -m venv kivy_venv
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

Build