Memrise Audio Generator
=======================

### Prerequisites

- python 3.6+
- `virtualenv`
- `pip`
- java jdk

### Getting Started

```bash
# create and source a new virtual environment
virtualenv -p $(which python3.6) venv
source venv/bin/activate
pip install -r requirements.txt
mkdir audio
```

### Actually Running It

```bash
# start a selenium server
java -jar -Dwebdriver.gecko.driver=./geckodriver_mac selenium-server-standalone-3.0.1.jar
```

```bash
# set constants correctly in main.py and then...
source venv/bin/activate
python3 main.py
```
