py -m venv ./venv
pip freeze > requirements.txt
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

python src/main.py