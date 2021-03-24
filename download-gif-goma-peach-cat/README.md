# Download animated GIF of Peach cat and Goma
Peach cat and Goma are such adorable characters. 

I love them so much that I want to collect their animated stickers.

However, the stickers are released in many smaller packS, and are only available on LINE / Kakao chat WITH SOME COST.

So I decide to write some code to collect them from some sources online.

(Sorry the author of the two lovely cats :3)

## The code has 3 parts :
### - download-gif.py: 
This piece of code will download all the GIF images appearing in the URL either on your clipboard or passed into argument. 

I found that there are some GIF on https://www.ilikesticker.com/Store/en. 

By searching "peach cat" on this page, it leads to some sticker pack, with animated GIF on the page. 

Just copy the URL to clipboard, and run the python code.

### - goma-peach-gif.py: 
The code will download zip file of sticker packs from LINE, unzip, convert the animated PNG to GIF

According to an online reference, you can download the sticker pack by using a template of URL, as long as you know the ID of the pack.

So I checked https://store.line.me/stickershop and find out the StickerID of packs that are not downloaded yet with the previous code.

Then I automate the downloaded of these packs, unzip them, and convert the animated PNG to GIF (apng2gif)

### - unzip-apng-to-gif.sh:
The shell script that will be called by goma-peach-gif.py to execute the unzip, and convert using apng2gif

