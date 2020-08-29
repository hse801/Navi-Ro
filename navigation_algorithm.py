#  ִܰ    ˰
# reference : http://navercast.naver.com/contents.nhn?rid=2871&amp;contents_id=85293
import copy

#                          ش

departure = input('출발 지점을 입력하세요: ')
destination = input('도착 지점을 입력하세요: ')
print("-----------[", departure, "->", destination, "]----------")

#                  ǹ                ǹ          ִ   Ÿ      Ÿ     ǥ        .

landscape = {
    'home': {'hairShop': 5, 'superMarket': 10, 'EnglishAcademy': 9},
    'hairShop': {'home': 5, 'superMarket': 3, 'bank': 11},
    'superMarket': {'hairShop': 3, 'home': 10, 'EnglishAcademy': 7, 'restaurant': 3},
    'EnglishAcademy': {'home': 9, 'superMarket': 7, 'school': 12},
    'restaurant': {'superMarket': 3, 'bank': 4},
    'bank': {'hairShop': 11, 'restaurant': 4, 'EnglishAcademy': 7, 'school': 2},
    'school': {'bank': 2, 'EnglishAcademy': 12}
}

routing = {}
for place in landscape.keys():
    routing[place] = {'shortestDist': 0, 'route': [], 'visited': 0}


#

def visitPlace(visit):
    routing[visit]['visited'] = 1
    for toGo, betweenDist in landscape[visit].items():
        toDist = routing[visit]['shortestDist'] + betweenDist
        if (routing[toGo]['shortestDist'] >= toDist) or not routing[toGo]['route']:
            routing[toGo]['shortestDist'] = toDist
            routing[toGo]['route'] = copy.deepcopy(routing[visit]['route'])
            routing[toGo]['route'].append(visit)


#                   ̾     ǹ          ִ   Ÿ           ǥ õ               ׷          ǹ         ĭ        Ƶд .    ⼭    ĭ           Ѵ븦    Ѵ .

visitPlace(departure)

"""
    Ÿ         ª    ǹ          ǹ          湮 ϰ   湮    ǹ          ĥ        Ѵ .  ̶   湮     ε    ĥ Ѵ . 
      ο   ǹ     湮 ϸ      ǹ     ̾     ǹ          Ÿ          ٲ۴ .   ,         ̹   ִ   Ÿ             ٸ   Ÿ                           ٲٰų       Ѵ .
    ׷           ǹ       湮            ,             ݺ  Ѵ .
"""
while 1:
    #
    minDist = max(routing.values(), key=lambda x: x['shortestDist'])['shortestDist']
    toVisit = ''
    for name, search in routing.items():
        if 0 < search['shortestDist'] <= minDist and not search['visited']:
            minDist = search['shortestDist']
            toVisit = name
    #
    if toVisit == '':
        break
    #
    visitPlace(toVisit)

    print("[" + toVisit + "]")
    print("Dist :", minDist)

print("\n", "[", departure, "->", destination, "]")
print("Route : ", routing[destination]['route'])
print("ShortestDistance : ", routing[destination]['shortestDist'])