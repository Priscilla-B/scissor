import string
import random

from .models import Url

class UrlHelpersMixin(object):

    def url_code_exists(self, url_code):
        url_obj = Url.query.filter_by(url_code=url_code).first()
        
        return url_obj != None

    def generate_short_text(self, request, n):

        short_text = request.get_json().get('custom_short_text')

        if not short_text:
            short_text = ''.join(random.choices(string.ascii_letters, k=n))
        
        while self.url_code_exists(short_text):
            short_text = ''.join(random.choices(string.ascii_letters, k=n))
        
        return short_text
    
    def get_url_domain(self, request):
        domain = request.get_json().get('custom_domain')
        if not domain:
            domain = request.url_root

        if domain[-1] != '/':
            domain += '/'
        return domain
    
    
    
      
        
