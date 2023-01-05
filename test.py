import json
import random
def gender(string):
    for i in string.split():
        if(i=="Nam" or i=="nam"):
            return "Nam"
        if(i=="Nữ" or i=="nữ" or i== "nu" or i=="Nu"):
            return "Nữ"
    return "none"

def math(string):
    if gender(string) == "Nam":
        return 170/0.7
    else:
        return 170
def getSkin(string):
    with open("skin.json",encoding="utf-8") as skin_file:
        data=json.load(skin_file)
        res=[]
        for skin in data['skins']:
            if string in skin["tag"]:
                res.append(skin['tag'])
                res.append(skin['patterns'])
                res.append(random.choice(skin['responses']))
                return res
        res.append(["none"])
        res.append("Tôi không hiểu...")
        return res
def printSkin():
    with open("skin.json",encoding="utf-8") as skin_file:
        data=json.load(skin_file)
        tag=[]
        for skin in data['skins']:
            tag=(skin["tag"])
        if "da" in tag:
            return "ok"
        return "none"

def pointSkin(string):
    point=0
    listTong=[]
    tc=string.split(",")
    tc.pop()
    with open("skin.json",encoding="utf-8") as skin_file:
        data=json.load(skin_file)
        skin=data["skins"]
        for sk in skin:
            tong=0
            for p in sk["point"]:
                tong+=p
        for t in tc:
            for sk in skin:
                for s in sk["patterns"]:
                    if t==s:
                        index=sk["patterns"].index(s)
                        point+=sk["point"][index]
        
        listTong.append(point)
        m=max(listTong)
        id=listTong.index(m)

    return ([skin[id]["tag"],skin[id]["patterns"],skin[id]["responses"]])


print(pointSkin("Căng,Bong tróc,"))
# print(getSkin("da kh"))
# print(printSkin())
# print(math("Nam 170 65"))