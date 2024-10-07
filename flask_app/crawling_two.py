import re, requests

## Path ref ##
#https://en.wikipedia.org/wiki/List_of_PC_games_(A)

## Return format ##
# List of Tuple
# [(<Game name>, <Starter alphabet>, <Release date>),...]
# <Game name>        : str
# <Starter alphabet> : str
# <Release date>     : tuple of int format => (YYYY,MM,DD)

def crawl_pic(link):
    basePath = "https://en.wikipedia.org"
    # print(link)
    resp = requests.get(f"{basePath}{link}",timeout=60)
    if not resp.ok :
        return ''
    resp =resp.text
    pic = re.findall(r'<td colspan="2" class="infobox-image">.*<img src="(\S*.jpg)".*>.*</td>|<td colspan="2" class="infobox-image">.*<img src="(\S*.png)".*>.*</td>',resp)
    if not pic:
        return ''
    elif pic[0][0]:
        return pic[0][0]
    elif pic[0][1]:
        return pic[0][1]

def crawling_two():
    basePath = "https://en.wikipedia.org"
    startPath = "/wiki/List_of_PC_games_(A)"
    listOfGameName = []
    maximum_data = 450

    ## Get base HTML ##
    resp = requests.get(f"{basePath}{startPath}",timeout=60)
    if not resp.ok :
        raise(Exception("404 Not found"))
    resp =resp.text

    ## Crawling list of page ##
    listOfAlpha = re.findall(r'(/wiki/List_of_PC_games_\()(A[A-Za-z]|[B-Zb-z])([A-Za-z]*\)")',resp)
    listOfAlpha = list(map(lambda x: x[0]+x[1]+x[2][:-1],listOfAlpha))
    # print(len(listOfAlpha))

    ## Crawling row of game in bade HTML ##
    listOfGame = re.findall(r'<tr>\n<td>(.*)\n</td>\n<td>(.*)\n</td>\n<td>(.*)\n</td>\n<td>(.*)\n</td>\n<td>(.*)\n</td>\n<td>(.*)\n</td>',resp)

    ## Crawling game name and release date in base HTML ##
    for game in listOfGame:
        gameName = re.findall(r'<a .*><i>(.*)</i></a>|<i><a .*>(.*)</a></i>|<a .*>(.*)</a>',game[0])
        gameDate = re.findall(r'<span data-sort-value="([0-9]{12})-([0-2][0-9])-([0-3][0-9])-[0-9]{4}"',game[5])
        if gameName and gameDate:
            gameDate = (int(gameDate[0][0]),int(gameDate[0][1]),int(gameDate[0][2]),)
            if gameName[0][0]:
                gamelink = re.findall(r'<a.*href="(/wiki/\S*)" .*><i>.*</i></a>',game[0])
                if not gamelink:
                    continue
                elif gamelink[0]:
                    picLink = crawl_pic(gamelink[0])
                if picLink == "":
                    continue
                # print("case0 ",gameName[0][0],picLink)
                listOfGameName.append((gameName[0][0],gameDate,picLink))
            elif gameName[0][1]:
                gamelink = re.findall(r'<i><a.*href="(/wiki/\S*)" .*>.*</a></i>',game[0])
                if not gamelink:
                    continue
                elif gamelink[0]:
                    picLink = crawl_pic(gamelink[0])
                if picLink == "":
                    continue
                # print("case1 ",gameName[0][1],picLink)
                listOfGameName.append((gameName[0][1],gameDate,picLink))
            elif gameName[0][2]:
                gamelink = re.findall(r'<a.*href="(/wiki/\S*)" .*>.*</a>',game[0])
                if not gamelink:
                    continue
                elif gamelink[0]:
                    picLink = crawl_pic(gamelink[0])
                if picLink == "":
                    continue
                # print("case2 ",gameName[0][2],picLink)
                listOfGameName.append((gameName[0][2],gameDate,picLink))
        print(len(listOfGameName))
    if len(listOfGameName) >= maximum_data:
        return listOfGameName

    # Test one page ##
    # print(listOfGameName[:21])
    # for i in listOfGameName:
    #     print(i)
    #     print("--------")
    # print(len(listOfGameName))
    # exit()
    
    # Crawling game name and release date in other HTML ##
    for link in listOfAlpha:
        resp = requests.get(f"{basePath}{link}",timeout=60)
        if not resp.ok :
            raise(Exception("404 Not found"))
        resp =resp.text

        ## Get Alphabet of the page ##
        header = re.findall(r'<span class="mw-page-title-main">List of PC games \(([A-Za-z]+)\)</span>',resp)
        # print(header)

        listOfGame = re.findall(r'<tr>\n<td>(.*)\n</td>\n<td>.*\n</td>\n<td>.*\n</td>\n<td>.*\n</td>\n<td>.*\n</td>\n<td>(.*)\n</td>',resp)

        for game in listOfGame:
            gameName = re.findall(r'<a .*><i>(.*)</i></a>|<i><a .*>(.*)</a></i>|<a .*>(.*)</a>',game[0])
            gameDate = re.findall(r'<span data-sort-value="([0-9]{12})-([0-2][0-9])-([0-3][0-9])-[0-9]{4}"',game[1])
            if gameName and gameDate:
                gameDate = (int(gameDate[0][0]),int(gameDate[0][1]),int(gameDate[0][2]),)
                if gameName[0][0]:
                    gamelink = re.findall(r'<a.*href="(/wiki/\S*)" .*><i>.*</i></a>',game[0])
                    if not gamelink:
                        continue
                    elif gamelink[0]:
                        picLink = crawl_pic(gamelink[0])
                    if picLink == "":
                        continue
                    # print("case0 ",gameName[0][0],picLink)
                    listOfGameName.append((gameName[0][0],gameDate,picLink))
                elif gameName[0][1]:
                    gamelink = re.findall(r'<i><a.*href="(/wiki/\S*)" .*>.*</a></i>',game[0])
                    if not gamelink:
                        continue
                    elif gamelink[0]:
                        picLink = crawl_pic(gamelink[0])
                    if picLink == "":
                        continue
                    # print("case1 ",gameName[0][1],picLink)
                    listOfGameName.append((gameName[0][1],gameDate,picLink))
                elif gameName[0][2]:
                    gamelink = re.findall(r'<a.*href="(/wiki/\S*)" .*>.*</a>',game[0])
                    if not gamelink:
                        continue
                    elif gamelink[0]:
                        picLink = crawl_pic(gamelink[0])
                    if picLink == "":
                        continue
                    # print("case2 ",gameName[0][2],picLink)
                    listOfGameName.append((gameName[0][2],gameDate,picLink))
            print(len(listOfGameName))
        if len(listOfGameName) >= maximum_data:
            return listOfGameName

    ## Print result ##
    # for i in listOfGameName:
    #     print(i)
    #     print("--------")
    print(len(listOfGameName), "DONE")

    return listOfGameName

# print("Start")
# crawling_two()
# print("End")
