import re, requests

## Path ref ##
#https://en.wikipedia.org/wiki/List_of_PC_games_(A)

def crawling_two():
    basePath = "https://en.wikipedia.org"
    startPath = "/wiki/List_of_PC_games_(A)"
    listOfGameName = []

    ## Get base HTML ##
    resp = requests.get(f"{basePath}{startPath}")
    if not resp.ok :
        raise(Exception("404 Not found"))
    resp =resp.text

    ## Crawling list of page ##
    listOfAlpha = re.findall(r'(/wiki/List_of_PC_games_\()(A[A-Za-z]|[B-Zb-z])([A-Za-z]*\)")',resp)
    listOfAlpha = list(map(lambda x: x[0]+x[1]+x[2][:-1],listOfAlpha))
    # print(len(listOfAlpha))

    ## Crawling row of game in bade HTML ##
    listOfGame = re.findall(r'<tr>\n<td>(.*)\n</td>\n<td>(.*)\n</td>\n<td>(.*)\n</td>\n<td>(.*)\n</td>\n<td>(.*)\n</td>\n<td>(.*)\n</td>',resp)

    ## Crawling game name in base HTML ##
    for game in listOfGame:
        gameName = re.findall(r'<a .*><i>(.*)</i></a>|<i><a .*>(.*)</a></i>|<a .*>(.*)</a>|<i>(.*)</i>',game[0])
        if gameName:
            if gameName[0][0]:
                listOfGameName.append(gameName[0][0])
            elif gameName[0][1]:
                listOfGameName.append(gameName[0][1])
            elif gameName[0][2]:
                listOfGameName.append(gameName[0][2])
            elif gameName[0][3]:
                listOfGameName.append(gameName[0][3])

    ## Test one page ##
    # print(listOfGameName[:21])
    # for i in listOfGameName:
    #     print(i)
    #     print("--------")
    # exit()
    
    ## Crawling game name in other HTML ##
    for link in listOfAlpha:
        resp = requests.get(f"{basePath}{link}")
        if not resp.ok :
            raise(Exception("404 Not found"))
        resp =resp.text
        listOfGame = re.findall(r'<tr>\n<td>(.*)\n</td>\n<td>(.*)\n</td>\n<td>(.*)\n</td>\n<td>(.*)\n</td>\n<td>(.*)\n</td>\n<td>(.*)\n</td>',resp)

        for game in listOfGame:
            gameName = re.findall(r'<a .*><i>(.*)</i></a>|<i><a .*>(.*)</a></i>|<a .*>(.*)</a>|<i>(.*)</i>',game[0])
            if gameName:
                if gameName[0][0]:
                    listOfGameName.append(gameName[0][0])
                elif gameName[0][1]:
                    listOfGameName.append(gameName[0][1])
                elif gameName[0][2]:
                    listOfGameName.append(gameName[0][2])
                elif gameName[0][3]:
                    listOfGameName.append(gameName[0][3])

    ## Print result ##
    # for i in listOfGameName:
    #     print(i)
    #     print("--------")
    # print(len(listOfGameName))

    return listOfGameName


print("Start")
crawling_two()
print("End")