import json
import ssl
import urllib.request, urllib.parse, urllib.error

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input("Enter url: ")
    if len(url) < 1:
        break;
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read();
    print('Retrieved', len(data), 'characters')
    #print(data.decode())
    info = json.loads(data)
    print('\nUser count:', len(info["comments"]))

    sum = 0;
    for item in info["comments"]:
        #print('Name', item['name'])
        #print('Count', item['count'])
        sum+=item['count']
    print("Sum: ",sum)
