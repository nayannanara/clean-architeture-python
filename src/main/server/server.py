from flask import Flask
from src.main.routes.routes import route as user_route

app = Flask(__name__)

app.register_blueprint(user_route)
