from flask import Flask, request, session, redirect, url_for, render_template, flash
import psycopg2  # pip install psycopg2
import psycopg2.extras
import re
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from flask import Flask
from flask.helpers import make_response
from flask import request
from flask.json import jsonify
import jwt
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'

DB_HOST = "localhost"
DB_NAME = "kuka"
DB_USER = "postgres"
DB_PASS = "dbhec123"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASS, host=DB_HOST)


class kuka:
    @app.route('/login/', methods=['GET', 'POST'])
    def login():
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']

            cursor.execute(
                'SELECT token FROM accounts WHERE username = %s and password=%s', (username, password,))

            account = cursor.fetchone()
            return '''
                  <h1>Token VALUE: {}</h1>'''.format(account)

        return render_template('login.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']

            cursor.execute(
                'SELECT * FROM accounts WHERE username = %s', (username,))
            account = cursor.fetchone()
            token = jwt.encode({'user': username, 'exp': datetime.utcnow(
            ) + timedelta(minutes=30)}, app.config['SECRET_KEY'])
            print(account)
            if account:
                flash('Account already exists!')
            elif not username or not password:
                flash('Please fill out the form!')
            else:
                cursor.execute("INSERT INTO accounts (username, password,token) VALUES (%s,%s,%s)",
                               (username, password, token))
            conn.commit()
            flash('You have successfully registered!')
        elif request.method == 'POST':
            flash('Please fill out the form!')
        return render_template('register.html')

    @app.route('/protected')
    def protected():
        try:
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            token = request.args.get('token')
            cursor.execute(
                'SELECT token FROM accounts WHERE token = %s', (token,))
            account = cursor.fetchone()
            if(account[0] == token):
                return '<h1>Hello, token which is provided is correct</h1>'
        except TypeError:
            return '<h1>Hello, Could not verify the token </h1>, '.format(account)

    @ app.route('/logout')
    def logout():
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('username', None)
        return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
kuka.login()
