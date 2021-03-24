''' input : a URL in clipboard or passed in arguments
    output : download all GIF image in the URL and save to ./result folder
    I used this script to automate the download for some favorite GIF images :D
'''
import requests
import bs4
import sys
import os
import pyperclip

print('Pass a URL as an argument for this python code. Otherwise, it will take the URL in your clipboard.')
if len(sys.argv) == 1 :
    print('Take the URL in clipboard...',end='')
    url = pyperclip.paste()
else :
    print('Take the URL passed in arguments',end='')
    url = sys.argv[1]
print(url)

myRequest = requests.get(url)
myRequest.raise_for_status()

os.makedirs('result', exist_ok=True)  

parsedHtml = bs4.BeautifulSoup(myRequest.text,'html.parser')
listGif = parsedHtml.select('img')
for i in listGif :
    if '.gif' in i.get('src') :
        gifUrl = i.get('src')
        print('Downloading', gifUrl)
        imageFile = open(os.path.join('result',os.path.basename(gifUrl)),'wb')
        gifRequest = requests.get(gifUrl)

        for i in gifRequest.iter_content(10000) :
            imageFile.write(i)
        imageFile.close()