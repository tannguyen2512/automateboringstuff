import requests
import bs4

userName =  input('Input a Github username: ')

githubUserHome = 'https://github.com/{}'.format(userName)
myRequest = requests.get(githubUserHome)
myRequest.raise_for_status()

# parse the HTML
parseHtml = bs4.BeautifulSoup(myRequest.text,'html.parser')

# solution 1: using select, get
# imgTagList = parseHtml.select('img.color-bg-primary.border.width-full.avatar-user.avatar')

# for i in imgTagList :
#     print('Link to user profile image: ',i.get('src'))

# solution 2: using find
imgTagList = parseHtml.find('img', attrs={'class' : "avatar avatar-user width-full border color-bg-primary"})['src']
print('Link to user profile image: ',imgTagList)
