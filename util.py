import urllib2, google, bs4, re, regex, time

def strip(q):
    """
    Args:
    q: query string
    
    Returns:
    A list of 10 pages, each stripped separately
    """
    r = google.search(q,num=15,start=0,stop=15)

    l = []
    for result in r:
        l.append(result)

    text = []
    for url in l:
        try:
            req = urllib2.Request(url)
            u = urllib2.urlopen(req)
            page = u.read()
            soup = bs4.BeautifulSoup(page,'html')
            raw = soup.get_text()
            
            reg = re.sub("[\t\n ]"," ",raw)
            text.append(reg)
        except:
            pass
    return text
    
def findNames(text):
    return re.findall(regex.name,text)

def findDates(text):
    allDates = []
    for date in re.findall(regex.date,text):
        allDates.append(date)
    for date in re.findall(regex.txtDate,text):
        allDates.append(date)
    return allDates

def getNames(query):
    ans = []
    vals = strip(query)
    for x in vals:
        ans+=findNames(x)
    return ans
    
def getDates(query):
    ans = []
    vals = strip(query)
    for x in vals:
        ans+=findDates(x)
    return ans
    
def getAnswer(results):
    if(results):
        return max(results,key=results.count)
    return 0


while True:
    print("Give me a query")
    result = getDates(raw_input())
    print getAnswer(result)
