from datetime import datetime
from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


users_programs = db.Table(
    'users_programs',
    db.Column(
        'user_id',
        db.Integer,
        db.ForeignKey('user.id'),
        primary_key=True),
    db.Column(
        'program_id',
        db.Integer,
        db.ForeignKey('program.id'),
        primary_key=True),
    db.Column(
        'timestamp',
        db.DateTime,
        index=True,
        default=datetime.utcnow))

programs_workouts = db.Table(
    'programs_workouts',
    db.Column(
        'program_id',
        db.Integer,
        db.ForeignKey('program.id'),
        primary_key=True),
    db.Column(
        'workout_id',
        db.Integer,
        db.ForeignKey('workout.id'),
        primary_key=True),
    db.Column(
        'week',
        db.Integer),
    db.Column(
        'day_of_week',
        db.Integer),
    db.Column(
        'am',
        db.Boolean),
    db.Column(
        'pm',
        db.Boolean))

workouts_exercises = db.Table(
    'workouts_exercises',
    db.Column(
        'workout_id',
        db.Integer,
        db.ForeignKey('workout.id'),
        primary_key=True),
    db.Column(
        'exercise_id',
        db.Integer,
        db.ForeignKey('exercise.id'),
        primary_key=True),
    db.Column(
        'sets',
        db.Integer),
    db.Column(
        'reps',
        db.Integer),
    db.Column(
        'rest',
        db.String(64)),
    db.Column(
        'duration',
        db.Integer),
    db.Column(
        'effort',
        db.Integer))


class User(UserMixin, db.Model):
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

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    goal = db.Column(db.String(140))
    description = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # Relationships
    programs_workouts = db.relationship(
        'Workout',
        secondary=programs_workouts,
        lazy='subquery',
        backref=db.backref(
            'programs',
            lazy=True))

    def __repr__(self):
        return '<Program {}>'.format(self.title)


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout_type = db.Column(db.String(64))
    # Relationships
    workouts_exercises = db.relationship(
        'Exercise',
        secondary=workouts_exercises,
        lazy='subquery',
        backref=db.backref(
            'workouts',
            lazy=True))

    def __repr__(self):
        return '<Workout {}>'.format(self.title)


class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise_title = db.Column(db.String(64))
    exercise_type = db.Column(db.String(64))

    def __repr__(self):
        return '<Exercise {}>'.format(self.title)
