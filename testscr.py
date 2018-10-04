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

def parse_response(url_resp):
    '''
    Returns parsed reponse of the page.
    '''
    html = BeautifulSoup(url_resp, 'html.parser')
    definitions = []
    for li in html.select('li'):
        li_val = li.get('value')
        if li_val in numbers:
            # print(li_val)
            li_text_spans = li.find_all('span',recursive=False)
            st = [li_text_span.text.strip() for li_text_span in li_text_spans]
            # print((" ".join(st)))
            definitions.append(" ".join(st))
    return definitions

# main script
request = input('Enter URL: ')
response = simple_get(request)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = [str(n) for n in numbers]
# print(numbers)

if response is not None:
    print(parse_response(response))
