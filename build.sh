set -o errexit

pip install -r requirements.txt

# flask db stamp head
db revision --rev-id 2c811f90cb41
flask db migrate
flask db upgrade
