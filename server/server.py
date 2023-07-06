from flask import Flask, jsonify
app = Flask(__name__)
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/home", methods=['GET'])

def return_home():
    return jsonify({
        'message': "You are the man!",
        'people':['Jack', 'Harry', 'Barry']
    })

if __name__ == '__main__':
    app.run(debug=True, port=8080)