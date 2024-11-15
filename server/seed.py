from app import app
from models import db, Player

with app.app_context():
    Player.query.delete()

    player1 = Player(username="bob123", password_hash="49rfjfntj5")
    player2 = Player(username="mike12", password_hash="rifjek4w2")

    db.session.add_all([player1, player2])
    db.session.commit()
    print("Table seeded successfully!")

    