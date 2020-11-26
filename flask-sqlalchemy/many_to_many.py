from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path


app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = str(BASE_DIR / "many_to_many.sqlite")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + DB_PATH
app.config["SQLALCHEMY_COMMIT_ON_SUBMIT"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Project(db.Model):
    # Many
    __tablename__ = "amamov_project"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))

    developers = db.relationship(
        "User",
        backref="project",
        lazy="dynamic",
        secondary="user_project",
    )

    def __repr__(self):
        return f"<Project {self.title}>"


class User(db.Model):
    # Many
    __tablename__ = "amamov_user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))

    projects = db.relationship(
        "Project",
        backref="developer",
        lazy="dynamic",
        secondary="user_project",
    )

    def __repr__(self):
        return f"<User {self.username}>"


db.Table(
    "user_project",
    db.Column("user_id", db.Integer, db.ForeignKey("amamov_user.id")),
    db.Column("project_id", db.Integer, db.ForeignKey("amamov_project.id")),
)


db.create_all()

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)


"""
# amamov : p1, p2 / yua : p2, p3, / joy : p1, p2, p3 / wow : p1, p3
# p1 : amamov, joy, wow / p2 : amamov, yua, joy / p3 : yua, joy, wow

amamov = User(username = 'amamov')
joy = User(username = 'joy')
yua = User(username = 'yua')

p1 = Project(title = 'p1')
p2 = Project(title = 'p2')
p3 = Project(title = 'p3')
p4 = Project(title = 'p4')

db.session.add_all([amamov, joy, yua, p1, p2, p3, p4])
db.session.commit()

p1 = Project.query.filter(Project.title == 'p1').first()
p2 = Project.query.filter(Project.title == 'p2').first()
p3 = Project.query.filter(Project.title == 'p3').first()

amamov = User.query.filter(User.username == 'amamov').first()
joy = User.query.filter(User.username == 'joy').first()
yua = User.query.filter(User.username == 'yua').first() 

wow = User(username = 'wow')
db.session.add(wow)

p1.developers.append(amamov)
p1.developers.append(joy)
p1.developers.append(wow)
p2.developers.append(amamov)
p2.developers.append(yua)
p2.developers.append(joy)
p3.developers.append(yua)
p3.developers.append(joy)

wow.projects.append(p3)

p3.developers.all()
[<User yua>, <User joy>, <User wow>]

amamov.projects.all()
[<Project p1>, <Project p2>]

db.session.commit()

"""
