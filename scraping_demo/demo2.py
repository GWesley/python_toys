import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
import itertools

def download(url, num_retries=2, user_agent='wswp'):
    print('Downloading:', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        html = urllib.request.urlopen(request).read()
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries - 1)
    return html

def crawl_site(url, max_errors=5):
    for page in itertools.count(1):
        pg_url = '{}{}'.format(url,page)
        html = download(pg_url)
        if  html is None:
            number_error += 1
            if  number_error == max_errors:
                break
        else:
            number_error = 0
            print('= Downloaded:', url)
crawl_site("http://example.webscraping.com/places/default/view/-")