from datetime import datetime
from app import db

users_programs = db.Table(
    'users_programs',
    db.Column(
        'program_id',
        db.Integer,
        db.ForeignKey('program.id'),
        primary_key=True),
    db.Column(
        'user_id',
        db.Integer,
        db.ForeignKey('user.id'),
        primary_key=True))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # Relationships
    users_programs = db.relationship(
        'Program',
        secondary=users_programs,
        lazy='subquery',
        backref=db.backref(
            'users',
            lazy=True))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    goal = db.Column(db.String(140))
    description = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Program {}>'.format(self.title)
