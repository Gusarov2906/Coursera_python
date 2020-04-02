# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def scrap(url,i, count_val, position_val):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    sum = 0
    count = 0
    pos = 0
    href =""
# Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
    # Look at the parts of a tag
        pos += 1
        if pos == position_val:
            if i != count_val:
                href = tag.get('href', None)
                print("Retrieving: {}".format(href))
                i += 1
                scrap(href,i,count_val,position_val)
                break
    #print('Contents:', tag.contents[0])

url = input('Enter - ')
i = 0
count = int(input("Enter count: "))
position = int(input("Enter position: "))
scrap(url,i,count,position)
