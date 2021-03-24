import requests
import os

# this is a url template to download animated sticker on LINE, based on the StickerID
# Reference: https://www.line-stickers.com/how-to-get-line-sticker-with-gif-animation-png-transparent/
urlExample = 'http://dl.stickershop.LINE.naver.jp/products/0/0/1/StickerID/iphone/stickerpack@2x.zip'
urlTemplate = urlExample.replace('StickerID','{}')

stickerIDsDict = {
    'peach-cat-and-goma' : 14412394,
    'peach-cat-4' : 8941816,
    'peach-cat-5' : 10238801,
    'peach-cat-6' : 11044637,
    'peach-cat-7' : 11725797,
    'peach-cat-8' : 12453793,
    'peach-cat-9' : 13027817,
    'peach-cat-10' : 13560596,
    'peach-cat-11' : 13992900
}

# create a result folder
os.makedirs('./result',exist_ok=True)
os.makedirs('./result/gif',exist_ok=True)

for i in stickerIDsDict :
    url = urlTemplate.format(stickerIDsDict[i])
    print('Downloading {} ...'.format(url))

    myRequest = requests.get(url)
    myRequest.raise_for_status()
    gifFileName = os.path.join('./result',i+'.zip')
    print('Saving to {}'.format(gifFileName))
    gifFile = open(gifFileName,'wb')
    for chunk in myRequest.iter_content(10000) :
        gifFile.write(chunk)
    gifFile.close()
os.system('bash unzip-apng-to-gif.sh')