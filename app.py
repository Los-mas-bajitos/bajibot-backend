import sys
from datetime import timedelta

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from chatbot.chatbot import recipes, common_message, recommendations
from config.db import db
from config.utilz import analysis
from user.user_controller import users

print(sys.path)
app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SECRET_KEY'] = '97017582b69247b8a8a88491e108c1ca'
app.config['JWT_SECRET_KEY'] = '9aa6fe2ac33742958ef600ffea2230fc'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=2)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=1)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fb_users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt = JWTManager(app)

db.init_app(app)
app.register_blueprint(users)


@app.route('/chat', methods=['POST'])
def index():
    user_input = request.json.get('message')
    if user_input:
        response = analysis(user_input)
        if response == 'recipes':
            return chat()
        elif response == 'recommendations':
            return chat_recommendations()
        else:
            return chat_common_message()
    else:
        return jsonify({"error": "No message provided"}), 400


@app.route('/recipes', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if user_input:
        response = recipes(user_input)
        return jsonify({"response": response})
    else:
        return jsonify({"error": "No message provided"}), 400


@app.route('/recommendations', methods=['POST'])
def chat_recommendations():
    user_input = request.json.get('message')
    if user_input:
        response = recommendations(user_input)
        return jsonify({"response": response})
    else:
        return jsonify({"error": "No message provided"}), 400


@app.route('/common_message', methods=['POST'])
def chat_common_message():
    user_input = request.json.get('message')
    if user_input:
        response = common_message(user_input)
        return jsonify({"response": response})
    else:
        return jsonify({"error": "No message provided"}), 400


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
