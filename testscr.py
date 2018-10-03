# base imports
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

# functions:
def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    '''
    Returns TRUE if the response seems to be HTML, false otherwise.
    '''
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 and content_type is not None and content_type.find('html') > -1)

def log_error(e):
    '''
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    '''
    print(e)

# main script
request = input('Enter URL: ')
response = simple_get(request)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if response is not None:
    html = BeautifulSoup(response, 'html.parser')
    names = set()
    for li in html.select('li'):
        if li.value in numbers:
            if len(name) > 0:
                names.add(name.strip())
    print(list(names))
