import string
import random
import requests

from .models import Url



def url_code_exists(url_code):
    url_obj = Url.query.filter_by(url_code=url_code).first()
    
    return url_obj != None

def generate_short_text(form, n):

    short_text =form.get('url_code')

    if not short_text:
        short_text = ''.join(random.choices(string.ascii_letters, k=n))
    
    while url_code_exists(short_text):
        short_text = ''.join(random.choices(string.ascii_letters, k=n))
    
    return short_text
    
def get_url_domain(form, request):
    domain = form.get('domain')
    if not domain:
        domain = f'{request.url_root}/r/'

    if domain[-1] != '/':
        domain += '/'
    return domain


def url_is_valid(url):
    response = requests.get(url)
    return response.status_code == 200

    
    
      
        
