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

    # Test Regular Expression ##

    listOfAlpha = re.findall(r'(/wiki/List_of_PC_games_\()(A[A-Za-z]|[B-Zb-z])([A-Za-z]*\)")',resp)
    listOfAlpha = list(map(lambda x: x[0]+x[1]+x[2][:-1],listOfAlpha))
    print(len(listOfAlpha))
    for link in listOfAlpha:
        print(link)

    listOfGame = re.findall(r'<tr>\n<td>(.*)\n</td>\n<td>(.*)\n</td>\n<td>(.*)\n</td>\n<td>(.*)\n</td>\n<td>(.*)\n</td>\n<td>(.*)\n</td>',resp)
    print(listOfGame[148])
    print(len(listOfGame))

print("Start")
crawling_two()
print("End")