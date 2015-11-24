import urllib2, google, bs4, re

def strip(q):
    """
    Args:
    q: query string
    
    Returns:
    A list of 10 pages, each stripped separately
    """
    r = google.search(q,num=10,start=0,stop=10)

    l = []
    for result in r:
        l.append(result)

    text = []
    for url in l:
        hdr = {
            'User-Agent': 'Mozilla',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-us',
        }
        req = urllib2.Request(url,headers=hdr)
        u = urllib2.urlopen(req)
        page = u.read()
        soup = bs4.BeautifulSoup(page,'html')
        raw = soup.get_text()
        text.append(re.sub("[\t\n ]"," ",raw))
    return text

#while True:
#    print strip(raw_input())
