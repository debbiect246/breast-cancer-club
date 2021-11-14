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

app.secret_key = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


date = date.today()


# Global functions:
# ==============
def find_user():
    """
    Determines current user using the username value of the current session
    user and returns the current user as a dict.
    """
    current_user = mongo.db.users.find_one({"username": session["user"]})
    return current_user


def find_id():
    """
    Determines the ObjectId value of the current user and returns it as a
    string value.
    """
    user_id = str(find_user()['_id'])
    return user_id

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

# Add profile form
@app.route("/add_profile", methods=["GET", "POST"])
def add_profile():
    if request.method == "POST":
        # default values if fields are left blank
        default_img = ("profile_image.png")
        profile = {
            "member_type": request.form.get("member_type"),
            "fullname": request.form.get("fullname"),
            "birthday": request.form.get("birthday"),
            "image": request.form.get("image") or default_img,
            "created_by": session["user"],
            "date_created": date.strftime("%d %b %Y")
        }
        mongo.db.profiles.insert_one(profile)
        flash("Your Profile Has Been Added")
        return redirect(url_for("my_profile", username=session["user"]))

    profiles = mongo.db.profiles.find().sort("fullname", 1)
    return render_template("add_profile.html", profiles=profiles)


# Update profile form
@app.route("/update_profile/<profile_id>", methods=["GET", "POST"])
def update_profile(profile_id):
    if request.method == "POST":
        # default values if fields are left blank
        default_img = ("profile_image.png")
        update = {
            "member_type": request.form.get("member_type"),
            "fullname": request.form.get("fullname"),
            "birthday": request.form.get("birthday"),
            "image": request.form.get("image") or default_img,
            "created_by": session["user"],
            "date_created": date.strftime("%d %b %Y")
        }
        mongo.db.profiles.update({"_id": ObjectId(profile_id)}, update)
        flash("Your Profile Has Been Updated")
        return redirect(url_for("my_profile", username=session["user"]))

    profile = mongo.db.profiles.find_one({"_id": ObjectId(profile_id)})
    profiles = mongo.db.profiles.find().sort("fullname", 1)
    return render_template("update_profile.html", profile=profile,
                           profiles=profiles)


# Display personal profile page
@app.route("/my_profile/<username>", methods=["GET", "POST"])
def my_profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        my_profile = list(mongo.db.profiles.find(
                {"created_by": session["user"]}))
        user = mongo.db.users.find_one({"username": session["user"]})
        return render_template("profile.html", username=username,
                               user=user, profiles=my_profile)
    return redirect(url_for('login'))
    
#blog view
# Displays all blog posts  in the db
@app.route("/blogs")
def blogs():
    blogs = list(mongo.db.blogs.find())
    return render_template("blogs.html", blogs=blogs)


# Display blog post
@app.route("/blog_detail/<blog_id>")
def blog_detail(blog_id):
    blog = mongo.db.blogs.find_one({"_id": ObjectId(blog_id)})
    return render_template("blog_detail.html",
                           blog=blog)


# Allow users to add a blog post to db
@app.route("/add_blog", methods=["GET", "POST"])
def add_blog():
    if request.method == "POST":
        # default values if fields are left blank
        default_img = ("blogimage.png")
        blog = {
            "blog_title": request.form.get("blog_title"),
            "content": request.form.get("content"),
            "image": request.form.get("image") or default_img,
            "created_by": session["user"],
            "date_created": date.strftime("%d %b %Y"),
        }
        mongo.db.blogs.insert_one(blog)
        flash("Your Blog Post Has Been Added")
        return redirect(url_for("blogs", username=session["user"]))

    blog = mongo.db.blogs.find().sort("blog_title", 1)
    return render_template("add_blog.html", blogs=blogs)


# Update blog post
@app.route("/edit_blog/<blog_id>", methods=["GET", "POST"])
def edit_blog(blog_id):
    if request.method == "POST":
        # default values if fields are left blank
        default_img = ("blog_image.png")
        update = {
            "blog_title": request.form.get("blog_title"),
            "content": request.form.get("content"),
            "image": request.form.get("image") or default_img,
            "created_by": session["user"],
            "date_created": date.strftime("%d %b %Y")
        }
        mongo.db.blogs.update({"_id": ObjectId(blog_id)}, update)
        flash("Your Blog Post has been updated")
        return redirect(url_for("blogs", username=session["user"]))

    blog = mongo.db.blogs.find_one({"_id": ObjectId(blog_id)})
    blogs = mongo.db.blogs.find().sort("blog_title", 1)
    print(blog)
    return render_template("edit_blog.html", blog=blog, blogs=blogs)


# Allow users to delete blog post
@app.route("/delete_blog/<blog_id>")
def delete_blog(blog_id):
    mongo.db.blogs.remove({"_id": ObjectId(blog_id)})
    flash("Blog Post has been deleted")
    return redirect(url_for("blogs", username=session["user"]))


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
    meetUps = mongo.db.meetUp.find()
    return render_template("locations.html", locations=locations, meetUps=meetUps)


@app.route("/add_location", methods=["GET", "POST"])
def add_location():
    """
    Allows admin user to add a location to the database.  It can then be 
    selected when setting up an event
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
    number_attending = len(meetUp['attending'])
    print(number_attending)

    return render_template('event_details.html', meetUp=meetUp, 
                           location=location, 
                           number_attending=number_attending)
    

@app.route("/attending/<meetUp_id>", methods=["GET", "POST"])
def attending(meetUp_id):
    """
    Records the user id of a user and adds it to the attending array within a 
    MeetUp document on the database
    """
    user_id = find_id()
    meetUp = mongo.db.meetUp.find_one({"_id": ObjectId(meetUp_id)})
    if request.method == "POST":
        attendee = user_id
        mongo.db.meetUp.update_one(MeetUp, {"$push": {"attending": attendee}})
        flash("You have been recorded as attending")

    return redirect(url_for("event_details", meetUp_id=meetUp_id))

#error handlers
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for("index"))


# Run the App
# =================

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)