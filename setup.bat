@echo off

python -m venv venv

call venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt

start python manage.py runserver 2222
start http://127.0.0.1:2222/

pause
