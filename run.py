import os
from flask import Flask, render_template, request, redirect, flash, url_for


# envWS.py should exist only in Development
if os.path.exists("envWS.py"):
    import envWS

app = Flask(__name__)

# take app configuration from OS environment variables
app.secret_key = os.environ.get("FLASK_SECRET_KEY")  # => Heroku Config Vars
app.config["FLASK_IP"] = os.environ.get("FLASK_IP",   "0.0.0.0")
# the source 'PORT' name is mandated by Heroku app deployment
app.config["FLASK_PORT"] = int(os.environ.get("PORT"))
app.config["FLASK_DEBUG"] = os.environ.get("FLASK_DEBUG", "False").lower() \
                            in {'1', 'true', 't', 'yes', 'y'}

# App routes
# ==============
@app.route("/")  # trigger point through webserver: "/"= root directory home page
def index():
    return render_template("index.html")

#blog view
@app.route("/blog")
def onboarding():
    return render_template("blog.html")


#events view
@app.route("/events")
def onboarding():
    return render_template("events.html")


#error handlers
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for("index"))




# Run the App
# =================
if __name__ == "__main__":
    app.run(
        host=app.config["FLASK_IP"],
        port=app.config["FLASK_PORT"],
        debug=app.config["FLASK_DEBUG"],
        use_reloader=False
    )