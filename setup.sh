python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

python manage.py runserver 2222 &

open http://127.0.0.1:2222/

read -p "Press any key to continue..."
