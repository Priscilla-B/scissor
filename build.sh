set -o errexit

pip install -r requirements.txt

flask db migrate
flask db upgrade
