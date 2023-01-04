from flask import Flask, render_template, request, jsonify
from chat import get_response

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

@app.post("/question")

def question():   
    text = request.get_json().get("message")
    a=0;b=0;bmi=0;v1=0;v2=0;v3=0
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
        message = {"answer": reponse,"bmi":bmi,"vong1":v1,"vong2":v2,"vong3":v3,"gen":gen}
        return jsonify(message)
    else :
        reponse = get_response(text)
        message = {"answer": reponse,"bmi":bmi,"vong1":v1,"vong2":v2,"vong3":v3,"gen":gen}
        return jsonify(message)     


if __name__ == "__main__":
    app.run(debug=True)
