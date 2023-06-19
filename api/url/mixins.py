import string
import random


class UrlHelpersMixin(object):

    def generate_short_text(self, request, n):

        short_text = request.get_json().get('custom_short_text')

        if not short_text:
            short_text = ''.join(random.choices(string.ascii_letters, k=n))
        return short_text
    
    def get_url_domain(self, request):
        domain = request.get_json().get('custom_domain')
        if not domain:
            domain = request.url_root

        return domain
    
      
        
