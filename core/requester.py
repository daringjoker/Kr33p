import urllib
import requests


def guess_scheme(url): #default is https if https is not possible only then http is used
    if not "http" in url:
        try:
            response=requests.get(url="https://"+url)
            return "https://"+url
        except requests.exceptions.SSLError:
            return "http://"+url
        

def enumerate_options(url):
    resp=urllib.request.urlopen(url)
    return resp.headers

print(enumerate_options("https://www.google.com"))