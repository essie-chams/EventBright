from flask import  render_template
from user import  User
from event import Event
from app import app


users = User()
eve = Event()

@app.route('/')

def index():
    return render_template('index.html')


@app.route('/Create/')

def create():
    return render_template('create.html')

@app.route('/events/')

def events():
    return render_template('events.html')

@app.route('/login/')

def login():
    return render_template('login.html')

@app.route('/rsvp/')

def rsvp():
    return render_template('rsvp.html')


if __name__ == '__main__':
    app.run()