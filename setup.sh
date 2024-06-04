python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

python manage.py runserver 222 &

xdg-open http://127.0.0.1:222/

read -p "Press any key to continue..."