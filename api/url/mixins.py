import string
import random


class UrlHelpersMixin(object):

    def generate_short_url(self, n, request):
        random_code = ''.join(random.choices(string.ascii_letters, k=n))
        short_url = request.url_root + random_code
        return short_url