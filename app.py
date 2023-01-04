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
@app.post("/question")
def question():   
    text = request.get_json().get("message")
    a=0;b=0;bmi=0
    listNumber = full_number(text)
    if len(listNumber) >0:
        if len(listNumber) >1:
            a=listNumber[0]
            b=listNumber[1]
        else:
            mess="none"
            reponse = get_response(mess)
            message = {"answer": reponse}
            return jsonify(message)

        bmi=b/(a/100)*(a/100)
        if bmi<18.5:
            mess="thin"
        elif bmi > 24.9:
            mess="fat"
        else:
            mess="beauty"
        reponse = get_response(mess)
        message = {"answer": reponse}
        return jsonify(message)
    else :
        reponse = get_response(text)
        message = {"answer": reponse}
        return jsonify(message)     


if __name__ == "__main__":
    app.run(debug=True)
