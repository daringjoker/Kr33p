import random
import string
import urllib
import sys

valid_chars=string.ascii_letters+string.digits+string.punctuation

def rand_str(n):
    return "".join(random.choices(valid_chars,k=n))

def encode(s):
   return urllib.parse.quote_plus(s.encode('utf-8'))

def decode(s):
    s=s.encode('utf-8')  
    return urllib.parse.unquote_to_bytes(s).decode('utf-8')

