from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form['password']

        # Retrieve the user from the database
        users_collection = mongo.db.users
        user = users_collection.find_one({'email': email})

        if user and check_password_hash(user['password'], password):
            # Redirect to the 'index' page after successful login
            print("Login successful. Redirecting to index.")
            return redirect(url_for('index'))

        return 'Invalid email or password.'

    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/js")
def java_script():
    return render_template("java playlist.html")

@app.route("/css")
def css():
    return render_template("css.html")

@app.route("/html")
def html():
    return render_template("html.html")

@app.route("/m1")
def m1():
    return render_template("m1.html")

@app.route("/m2")
def m2():
    return render_template("m2.html")

@app.route("/m3")
def m3():
    return render_template("m3.html")

@app.route("/physics")
def physic():
    return render_template("physics.html")

@app.route("/chemistry")
def chemsitry():
    return render_template("chemistry.html")

@app.route("/ds")
def ds():
    return render_template("ds.html")

@app.route("/sem1")
def sem1():
    return render_template("sem1.html")

@app.route("/sem2")
def sem2():
    return render_template("sem2.html")

@app.route("/sem3")
def sem3():
    return render_template("sem3.html")

@app.route('/register', methods=['GET', 'POST'])

def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Hash the password before storing it
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Insert the user into the database
        users_collection = mongo.db.users
        users_collection.insert_one({'email': email, 'password': hashed_password})

        return render_template("login.html")

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)