#! python 3
import webbrowser
import sys
import pyperclip

# open google map for a given address
if len(sys.argv) > 1:
    address = '+'.join(sys.argv[1:])
else:
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)
print(address)
print('https://www.google.com/maps/place/' + address)