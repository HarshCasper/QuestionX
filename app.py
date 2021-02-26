from flask import Flask
from flask import jsonify
 
app = Flask(__name__)

@app.route("/")
def route():
    return jsonify({'message' : 'QuestionX server'})
    
@app.route("/signup")
def signup():
    return jsonify({'message' : 'signup'})

@app.route("/login")
def login():
    return jsonify({'message' : 'login'})

@app.route("/pdf-upload")
def pdf_upload():
    return jsonify({'message' : 'pdf-upload'})

@app.errorhandler(404)
def not_found(e):
    return jsonify({'message' : 'not-found'}), 404  

if __name__ == "__main__":
    app.run()

