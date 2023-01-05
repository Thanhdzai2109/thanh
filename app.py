from flask import Flask, render_template, request, jsonify
from chat import get_response
import json
import random
app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("base.html")
def contains_number(string):
    for i in range(10):
        if str(i) in list(string):
            return True
    return False
def full_number(string):
    a=string.split()
    b=[]
    for i in a:
        if(contains_number(i)):
            b.append(int(i))
    return b

def gender(string):
    for i in string.split():
        if(i=="Nam" or i=="nam"):
            return "Nam"
        if(i=="Nữ" or i=="nữ" or i== "nu" or i=="Nu"):
            return "Nữ"
    return "none"
def getSkin(string):
    with open("skin.json",encoding="utf-8") as skin_file:
        data=json.load(skin_file)
        res=[]
        for skin in data['skins']:
            if string in skin["tag"]:
                res.append(skin['patterns'])
                res.append(random.choice(skin['responses']))
                return res
        res.append("Tôi không hiểu tình trạng da của bạn ...")
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

    return [skin[id]["tag"],skin[id]["patterns"],skin[id]["responses"]]

@app.post("/question")

def question():   
    text = request.get_json().get("message")
    a=0;b=0;bmi=0;v1=0;v2=0;v3=0;skinMess=[];l=0
    gen=gender(text)
    listNumber = full_number(text)
    

    if len(listNumber) >0:
        if len(listNumber) >1:
            a=listNumber[0]
            b=listNumber[1]
            if gen=="none":
                mess="none"
                reponse = get_response(mess)
                message = {"answer": reponse}
                return jsonify(message)
            elif gen=="Nam":
                v2=round(a*0.45,2)
                v1=round(v2/0.7,2)
                v3=round(v2/0.83,2)
            else:
                v1=round(a/2 +2,2)
                v2=round(a/2-22,2)
                v3=round(v2/0.68,2)
        else:
            mess="none"
            reponse = get_response(mess)
            message = {"answer": reponse}
            return jsonify(message)

        bmi=b/((a/100)*(a/100))
        bmi=round(bmi,2)
        if bmi<18.5:
            mess="thin"
        elif bmi > 24.9:
            mess="fat"
        else:
            mess="beauty"

        
        reponse = get_response(mess)
        message = {"answer": reponse,"bmi":bmi,"vong1":v1,"vong2":v2,"vong3":v3,"skinMess":skinMess,"lenSkin":l}
        return jsonify(message)
    else :
        skinMess=getSkin(text)
        pSkin=pointSkin(text)
        l=len(pSkin)
        reponse = get_response(text)

        message = {"answer": reponse,"bmi":bmi,"vong1":v1,"vong2":v2,"vong3":v3,"skinMess":skinMess,"pointSkin":pSkin,"lenSkin":l}
        return jsonify(message)     


if __name__ == "__main__":
    app.run(debug=True)
