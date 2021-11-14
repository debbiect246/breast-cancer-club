import os
from datetime import date, datetime
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
# envWS.py should exist only in Development
if os.path.exists("envWS.py"):
    import envWS

app = Flask(__name__)




# take app configuration from OS environment variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


date = date.today()

# App routes
# ==============
@app.route("/")  # trigger point through webserver: "/"= root directory home page
def index():
    return render_template("index.html")

# Register user in the db
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if user already in db
        existing_user = mongo.db.users.find_one(
                        {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("register"))

        # check if email already in db
        existing_email = mongo.db.users.find_one(
                        {"email": request.form.get("email").lower()})

        if existing_email:
            flash("Email address already registered!")
            return redirect(url_for("register"))

        # add user details to db
        register = {
            "firstname": request.form.get("firstname").lower(),
            "lastname": request.form.get("lastname").lower(),
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "date_created": date.strftime("%d %b %Y")
        }
        mongo.db.users.insert_one(register)

        # put the user into a session cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign Up Successful!")
        return redirect(url_for("my_profile", username=session["user"]))

    return render_template("register.html")


# Log existing user into site
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if user already in db
        existing_user = mongo.db.users.find_one(
                        {"username": request.form.get("username").lower()})
        # ensure password matches
        if existing_user:
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for("my_profile",
                                username=session["user"]))
            else:
                # invalid password
                flash("Incorrect Username/Password!")
                return redirect(url_for("login"))
        else:
            # username doesn't exist/is incorrect
            flash("Incorrect Usernname/Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Logs user out of their account
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

#blog view
@app.route("/blog")
def blog():
    return render_template("blog.html")


#events view
@app.route("/events")
def events():
        meetUps = mongo.db.meetUp.find()
        print(meetUps)
        return render_template('events.html', meetUps=meetUps)


#locations view (temporary)
@app.route("/locations")
def locations():
    locations = mongo.db.locations.find()
    print('hello')
    print(locations)
    meetUps = mongo.db.meetUp.find()
    print(meetUps)
    return render_template("locations.html", locations=locations, meetUps=meetUps)


@app.route("/add_location", methods=["GET", "POST"])
def add_location():
    """
    Allows admin user to add a location to the database.  It can then be selected when setting up an event
    """
    print('add location function called')
    if request.method == "POST":
        print('add location POST request')
        location = {
            "name": request.form.get("name"),
            "x": request.form.get("x-coord"),
            "y": request.form.get("y-coord")
        }
        print(location)
        mongo.db.locations.insert_one(location)
        flash("Location added")

        return redirect(url_for('locations'))
    
    return render_template('add_location.html')


@app.route("/event_details/<meetUp_id>")
def event_details(meetUp_id):
    """
    Returns details of the selected event along with a location map
    """
    meetUp = mongo.db.meetUp.find_one({"_id": ObjectId(meetUp_id)})
    location = mongo.db.locations.find_one({"name": meetUp['location']})
    return render_template('event_details.html', meetUp=meetUp, location=location)
    

#error handlers
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for("index"))


# Run the App
# =================

if __name__ == "__main__":

    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("FLASK_DEBUG"))