#! python 3
# searchPypi.py - Open several search results
import requests
import sys
import bs4
import webbrowser

domain = 'https://google.com/'
maxTabOpened = 5

def requestSearchEngine(argv) :
    searchUrl = domain + 'search?q=' + ' '.join(argv[1:])
    myRequest = requests.get(searchUrl)
    return myRequest


def parseRequest(someRequest) :
    parsedHTML = bs4.BeautifulSoup(myRequest.content, 'html.parser')
    listResultUrl = parsedHTML.select('.kCrYT > a')
    return listResultUrl

def openResultUrl(someListResult) :
    for i in range(min(maxTabOpened, len(someListResult))):
        urlToOpen = domain + someListResult[i].get('href')
        print('Opening ', urlToOpen)
        webbrowser.open(urlToOpen)


print('Searching...')
myRequest = requestSearchEngine(sys.argv)
myRequest.raise_for_status()
listResult = parseRequest(myRequest)
openResultUrl(listResult)