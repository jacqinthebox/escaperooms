from flask import Flask, render_template, request, make_response, redirect, url_for, session, jsonify
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, String, Integer
import bcrypt
import pyodbc
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.secret_key = 'secret key'


def create_database():
    server = 'sqledge'
    database = 'master'
    username = 'sa'
    password = '123Tralala^'
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

    # Create the database
    cursor = conn.cursor()
    conn.autocommit = True
    # cursor.execute("CREATE DATABASE mydatabase")
    cursor.execute(
        "if not exists (select * from sys.databases where name = 'mydatabase') begin create database mydatabase end")
    cursor.close()


create_database()

engine = create_engine('mssql+pyodbc://sa:123Tralala^@sqledge/mydatabase?driver=ODBC+Driver+17+for+SQL+Server')
# Create the base class for our models
Base = declarative_base()


class Team(Base):
    __tablename__ = 'Teams'
    Id = Column(Integer, primary_key=True)
    TeamName = Column(String(80), nullable=False)
    ContactName = Column(String(80), nullable=False)
    Email = Column(String(80), nullable=False)
    PasswordHash = Column(String(128), nullable=False)

    def __repr__(self):
        return f'<Team {self.TeamName}>'


# Create the Teams table
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a session
db_session = Session()

teams = db_session.query(Team).all()


def hash_password(password):
    # generate a salt and use it to hash the password
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    return password_hash


def verify_password(password, password_hash):
    try:

        return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))
    except ValueError:
        print("Invalid password hash")
        return False
    except TypeError:
        print("Password is not a string")
        return False
    except UnicodeEncodeError:
        print("Password is not a Unicode string")
        return False


def retrieve_password_hash_for_user(email):
    team = db_session.query(Team).filter_by(Email=email).first()
    if team:
        # return the user's password hash
        return team.PasswordHash

    else:
        # return None if the user was not found
        return None


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    team_name = data['TeamName']
    password = data['Password']
    contact_name = data['ContactName']
    email = data['Email']

    # Get the username and password from the form submission

    team = db_session.query(Team).filter_by(TeamName=team_name).first()
    registered_mail = db_session.query(Team).filter_by(Email=email).first()
    # Check if the username is already taken
    if team in teams:
        return jsonify({'message': 'Team already registered! Yikes.'}), 409
    elif registered_mail in teams:
        return jsonify({'message': 'That email is already registered! Yikes'}), 409
    else:
        password_hash = hash_password(password)
        new_team = Team(TeamName=team_name, ContactName=contact_name, Email=email, PasswordHash=password_hash)
        db_session.add(new_team)
        db_session.commit()
        return jsonify({'message': 'Team has been added to the database'}), 200


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the username and password from the form submission

        data = request.get_json()
        email = data['email']
        password = data['password']
        stored_password_hash = retrieve_password_hash_for_user(email)

        if stored_password_hash and verify_password(password, stored_password_hash):
            team = db_session.query(Team).filter_by(Email=email).first()
            if team is None:
                return 'Team not found', 404
            return jsonify({'message': 'Login successful!', 'teamName': team.TeamName}), 200
        else:
            return jsonify({'message': 'Wrong password!'}), 400
    else:
        return jsonify({'message': 'The API is working'}), 200


@app.route('/')
def index():
    # Check if the user is logged in
    if 'email' in request.cookies:
        email = request.cookies.get('email')
        team = request.cookies.get('team')
        return render_template('index.html', team=team)
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # Create a response object and delete the username cookie
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('email')
    response.delete_cookie('team')
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=True, port=5001)
