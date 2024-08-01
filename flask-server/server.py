from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/home")
def home():
    available_Buddy=[{"b1":{"name","id"}}]
    
    return available_Buddy
