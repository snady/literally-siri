import urllib2, google, bs4, re, regex, time

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
        try:
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
            unicodeVer = re.sub("[\t\n ]"," ",raw)
            unicodeVer.encode('utf8')
            str(unicodeVer)
            print type(unicodeVer)
            unicodeVer+= "123-456-7890"
            text.append(unicodeVer)
        except:
            pass
    return text


def findNumbers(text):
    print  re.findall(regex.number,text)
    
def getNumQuery(query):
    ans = []
    vals = strip(query)
    for x in vals:
        print type(x)
#        time.sleep(1)
        ans+=findNumbers(x)
    return ans

while True:
    print("Give me a query")
    print getNumQuery(raw_input())
