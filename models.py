from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='ongoing')

    def toggle_status(self):
        if self.status == "ongoing":
            self.status = "done"
        else:
            self.status = "ongoing"

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Task {self.name}>'
