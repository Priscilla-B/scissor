set -o errexit

pip install -r requirements.txt

flask db stamp head
flask db migrate
flask db upgrade
