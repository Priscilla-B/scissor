set -o errexit

flask db migrate
flask db upgrade

pip install -r requirements.txt