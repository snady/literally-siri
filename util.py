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
        hdr = {'Accept','User-Agent': 'Mozilla/5.0'}
        req = urllib2.Request(url,headers=hdr)
        u = urllib2.urlopen(req)
        page = u.read()
        soup = bs4.BeautifulSoup(page,'html')
        raw = soup.get_text()
        text.append(re.sub("[\t\n ]"," ",raw))
    return text 
