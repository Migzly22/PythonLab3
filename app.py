#Main Application
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response


app = Flask(__name__)
CORS(app)

    
#@ is a design pattern in Python that allows a user to add new functionality
# to an existing object without modifying its structure.
#This function also generates the root page of the website.
@app.get("/")
def index_get():
    #Instead of returning hardcode HTML from the function, a HTML file can be 
    # rendered by the render_template() function.
    return render_template("base.html")


@app.post("/predict")
def predict():
    #Parses the incoming JSON request data and returns it.
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
