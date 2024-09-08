import re, requests

## Path ref ##
#https://www.eurogamer.net/archive/YYYY/MM
#https://www.eurogamer.net/reviews

def crawling():
    listOfLink = []
    startPath = '/archive/2024/09'
    basePath = "https://www.eurogamer.net"

    resp = requests.get(f"{basePath}{startPath}")
    resp = resp.text

    ## Test Regular Expression ##
    # testStr = 'dhaslkdjasldjsdj<a href="https://www.eurogamer.net/sd-asda-review-das-dsa">sdddasdsadsaddsdsadas'
    # lst = re.findall(r'<a href="https://www.eurogamer.net/.*-review.*">',testStr)
    # print(lst)

    listOfmonth = re.findall(r'<a href="/archive/[0-9]*/[0-9]*"', resp)
    print(len(listOfmonth))

    ## Test Only One Page ##
    # resp = requests.get(f"{basePath}{listOfmonth[0][9:-1]}")
    # resp = resp.text
    # lst = re.findall(r'href="https://www.eurogamer.net/.*-review.*"',resp)
    # for l in lst:
    #     print(l)

    for link in listOfmonth:
        resp = requests.get(f"{basePath}{link[9:-1]}")
        resp = resp.text
        lst = re.findall(r'href="https://www.eurogamer.net/.*-review"',resp) #digitalfoudry should not exist
        listOfLink.extend(lst)
        print(link, "success", len(lst))
        if len(listOfLink) > 400:
            break
    
    print(len(listOfLink))
    for link in listOfLink:
        print(link)


print("Start")
crawling()
print("End")