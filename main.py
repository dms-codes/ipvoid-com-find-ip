import requests 
from bs4 import BeautifulSoup as bs

def get_ipaddr(hostname):
    serviceurl = "https://www.ipvoid.com/find-website-ip/"
    payload = {
               'website':hostname,
               'websiteAddr':hostname,
              }
    html = requests.post(serviceurl, data=payload).content
    soup = bs(html,'html.parser')
    textarea = soup.find('textarea').text
    res = []
    for r in textarea.split('\n'):
        res.append(r.split(' ')[0])
    return res
    
if __name__ == '__main__':
    print(get_ipaddr('www.google.com'))
