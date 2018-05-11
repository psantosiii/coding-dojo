from flask import Flask, render_template, request,session, redirect

# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('friendsdb')
# now, we may invoke the query_db method
@app.route('/')
def index():
    my_friends = mysql.query_db("SELECT * FROM friends;")
    print("all the friends",my_friends)
    return render_template("index.html",friends = my_friends)

@app.route('/new_friend', methods=['POST'])
def new_friends():
    query = 'INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());'
    data = {
            'first_name': request.form['first_name'],
            'last_name':  request.form['last_name'],
            'occupation': request.form['occupation']
           }
    mysql.query_db(query, data)
    return redirect('/')
@app.route('/delete', methods=['post'])
def delete():
    query = "DELETE FROM friends WHERE first_name = %(first_name)s;"
    data = {
             'first_name': request.form['first_name'],
    }
    mysql.query_db(query, data)
    return redirect('/')
@app.route('/update_job', methods=['post'])
def update():
    query = "UPDATE friends SET occupation = %(occupation)s, updated_at = NOW() WHERE first_name = %(first_name)s;"
    data = {
            'first_name': request.form['first_name'],
            'occupation': request.form['occupation']
    }   
    mysql.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

