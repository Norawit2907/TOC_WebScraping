import re, requests

## Path ref ##
#https://en.wikipedia.org/wiki/List_of_PC_games_(A)

def crawling_two():
    basePath = "https://en.wikipedia.org"
    startPath = "/wiki/List_of_PC_games_(A)"

    resp = requests.get(f"{basePath}{startPath}")
    if not resp.ok :
        raise(Exception("404 Not found"))
    resp =resp.text

    ## Test Regular Expression ##
    testStr = 'dsdsdsdss<a href="/wiki/List_of_PC_games_(dsdsd)"dsdsdsdsd'
    lst = re.findall(r'(/wiki/List_of_PC_games_\()(A[A-Za-z]|[B-Zb-z])([A-Za-z]*\)")',testStr)
    print(len(lst))
    print(lst)

    # listOfAlpha = re.findall(r'(/wiki/List_of_PC_games_\()(A[A-Za-z]+|[B-Zb-z])([A-Za-z]*\)")',resp)
    # print(len(listOfAlpha))
    # for link in listOfAlpha:
    #     print(link[:-1])
    

print("Start")
crawling_two()
print("End")