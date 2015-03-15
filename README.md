to setup:

clone this dir and change into it.

virtualenv --python=pypy venv

source venv/bin/activate

pip install -r requirements.txt

crossbar start

python chattr.py in one window

python main.py in another
