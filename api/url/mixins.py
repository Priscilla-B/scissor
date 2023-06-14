import string
import random


class UrlHelpersMixin(object):

    def generate_short_url(self, n):
        short_url = ''.join(random.choices(string.ascii_letters, k=n))
        return short_url