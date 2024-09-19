import re, requests

## Not in used ##

## Path ref ##
#https://www.eurogamer.net/archive/YYYY/MM
#https://www.eurogamer.net/reviews

def crawling_one():
    listOfLink = []
    basePath = "https://www.eurogamer.net"
    startPath = '/archive/2024/09'

    resp = requests.get(f"{basePath}{startPath}")
    if not resp.ok :
        raise(Exception("404 Not found"))
    resp = resp.text

    ## Test Regular Expression ##
    # testStr = 'dhaslkdjasldjsdj<a href="https://www.eurogamer.net/sd-asda-review-das-dsa">sdddasdsadsaddsdsadas'
    # lst = re.findall(r'<a href="https://www.eurogamer.net/.*-review.*">',testStr)
    # print(lst)

    listOfMonth = re.findall(r'<a href="/archive/[0-9]*/[0-9]*"', resp)
    print(len(listOfMonth))

    ## Test Only One Page ##
    # resp = requests.get(f"{basePath}{listOfMonth[0][9:-1]}")
    # resp = resp.text
    # lst = re.findall(r'href="https://www.eurogamer.net/.*-review.*"',resp)
    # for l in lst:
    #     print(l)

    for link in listOfMonth:
        resp = requests.get(f"{basePath}{link[9:-1]}")
        if not resp.ok :
            raise(Exception("404 Not found"))
        resp = resp.text
        lst = re.findall(r'href="https://www.eurogamer.net/(?!digitalfoundry).*-review"',resp)
        listOfLink.extend(lst)
        print(link, "success", len(lst))
        if len(listOfLink) > 400:
            break
    
    print(len(listOfLink))
    for link in listOfLink:
        print(link)

print("Start")
crawling_one()
print("End")