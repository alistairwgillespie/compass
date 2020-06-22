from app import app, db
from app.models import User, Program, Workout, Exercise


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Program': Program,
        'Workout': Workout,
        'Exercise': Exercise}
