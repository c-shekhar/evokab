# IMPORTS
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

# FUNCTIONS:
def simpleGet(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if isGoodResponse(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        logError('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def isGoodResponse(resp): # checks if response is an HTML doc
    contentType = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)

def logError(e):
    print(e)

# MAIN SCRIPT:

dictURL = 'https://dictionary.com/browse/' # default online dictionary

defaultFile = 'vocab.ex'
vocab = open(defaultFile, 'r')

vocabList = vocab.read().split('\n')

print(vocabList)

vocab.close()
