import requests
from bs4 import BeautifulSoup
import urlparse

url = "https://www.amazon.com/dp/B010U3XVMU/ref=twister_B011TUYQOU?_encoding=UTF8&psc=1&tag=gdext-20"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

# This will look for a meta tag with the og:image property
og_image = (soup.find('meta', property='og:image') or
                    soup.find('meta', attrs={'name': 'og:image'}))
if og_image and og_image['content']:
    print og_image['content']
    print ''

# This will look for a link tag with a rel attribute set to 'image_src'
thumbnail_spec = soup.find('link', rel='image_src')
if thumbnail_spec and thumbnail_spec['href']:
    print thumbnail_spec['href']
    print ''

def image_url(url):
    result=requests.get(url)
    b_soup=BeautifulSoup.BeautifulSoup(result.text)
    images=[]
    image = """<img src="%s"><br />"""
    for img in soup.findAll("img", src=True):
        print image % urlparse.urljoin(url, img["src"])
    return images

