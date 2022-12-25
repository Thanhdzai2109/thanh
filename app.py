from flask import Flask, render_template, request, jsonify
from chat import get_response

app = Flask(__name__)


@app.get("/")
def index_get():
    return render_template("base.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    a = int(text[0])
    b= int(text[1]);
    Bmi= b/((a/100)*(a/100))
    if(Bmi<18.5):
            mess="thin"
    elif (Bmi>=23):
            mess="fat"     
    else: 
            mess="beauty" 
    reponse = get_response(mess)
    message = {"answer": reponse}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
