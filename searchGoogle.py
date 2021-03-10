#! python 3
# searchPypi.py - Open several search results
import requests
import sys
import bs4
import webbrowser

print('Searching...')
domain = 'https://google.com/'
searchEngine = domain + 'search?q='
searchURL = searchEngine + ' '.join(sys.argv[1:])
print(searchURL)
myRequest = requests.get(searchURL)
myRequest.raise_for_status()

# Retrieve top search result links.
# parsedHTML = bs4.BeautifulSoup(myRequest.text, 'html.parser')
parsedHTML = bs4.BeautifulSoup(myRequest.content, 'html.parser')
linkSearchResults = parsedHTML.select('.kCrYT > a')

# Open a browser tab for each result.
tabLimit = min(8, len(linkSearchResults))
for i in range(tabLimit):
    urlToOpen = domain + linkSearchResults[i].get('href')
    print('Opening ', urlToOpen)
    webbrowser.open(urlToOpen)