from bs4 import BeautifulSoup
import requests

source = requests.get('https://isitchristmas.today').text

soup = BeautifulSoup(source,'lxml')
message = soup.find(class_='big').text.replace('!','').lower()
is_is_Christmas = False
if message == 'no':
    is_is_Christmas = False
else:
    is_is_Christmas = True
print(is_is_Christmas)
#30:38