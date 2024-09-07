import re, requests

#https://store.steampowered.com/search/?sort_by=Released_DESC&os=win (infinite scroll problem)
#https://www.eurogamer.net/reviews

def crawling():
    #start->
    listOfLink = []
    starturl = '/archive/2024/09'
    path = "https://www.eurogamer.net"

    resp = requests.get(f"{path}{starturl}")
    resp = resp.text

    testStr = 'dhaslkdjasldjsdj<a href="https://www.eurogamer.net/sd-asda-review-das-dsa">sdddasdsadsaddsdsadas'

    #regular expression
    listOfmonth = re.findall(r'<a href="/archive/[0-9]*/[0-9]*"', resp)

    # resp = requests.get(f"{path}{listOfmonth[0][9:-1]}")
    # resp = resp.text
    # lst = re.findall(r'href="https://www.eurogamer.net/.*-review.*"',resp)
    # for l in lst:
    #     print(l)

    print(len(listOfmonth))
    for link in listOfmonth:
        resp = requests.get(f"{path}{link[9:-1]}")
        resp = resp.text
        lst = re.findall(r'href="https://www.eurogamer.net/.*-review"',resp)
        listOfLink.extend(lst)
        print(link, "success", len(lst))
    
    print(len(listOfLink))
    for link in listOfLink:
        print(link)

    # lst = re.findall(r'<a href="https://www.eurogamer.net/.*-review.*">',testStr)
    # print(lst)

print("Start")
crawling()
print("End")