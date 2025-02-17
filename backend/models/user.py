from database import db

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column("user_id", db.Integer, primary_key = True)
    user_name = db.Column("user_name", db.String(255), nullable = False)
    user_password = db.Column("user_password", db.String(255), nullable = False)
    user_email = db.Column("user_email", db.String(255), unique = True, nullable = False)