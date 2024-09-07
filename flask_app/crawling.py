import re, requests

#https://store.steampowered.com/search/?sort_by=Released_DESC&os=win (infinite scroll problem)
#https://www.eurogamer.net/reviews

def crawling():
    #start->
    resp = requests.get("https://www.eurogamer.net/archive/2024/09")
    resp = resp.text

    testStr = 'dhaslkdjasldjsdjhref="/archive/24747/572"dasdsadsaddsdsadas'

    #regular expression
    listOfLink = re.findall(r'href="/archive/[0-9]*/[0-9]*"', resp)
    print(len(listOfLink))
    for link in listOfLink:
        print(link)

print("Start")
crawling()
print("End")