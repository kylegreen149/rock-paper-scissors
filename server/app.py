import ipdb
from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Player

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'

migrate = Migrate(app, db)

db.init_app(app)

@app.get("/players")
def get_all_players():
    players = Player.query.all()
    response_body =[player.to_dict(only=("id", "username")) for player in players]
    return make_response(response_body, 200)
    

if __name__ == "__main__":
    app.run(port=5555, debug=True)