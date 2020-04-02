import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

serviceurl = 'http://py4e-data.dr-chuck.net/comments_345393.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = serviceurl
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
sum = 0
n = 0
tree = ET.fromstring(data)
list = tree.findall('comments/comment')
for item in list:
    sum += int(item.find('count').text)
    n += 1
print(f'Count: {n}')
print(f'Sum: {sum}')
