from flask import Flask, render_template, abort

app = Flask(__name__)

projects = [
    {
        "name": "Habit Tracker",
        "thumb": "img/habit-tracker.png",
        "hero": "img/ht.jpg",
        "categories": ["Python", "Flask", "MongoDB"],
        "slug": "habit-tracker",
        "prod": "https://habit-tracker-production-aeaa.up.railway.app/"
    },
    {
        "name": "Microblog",
        "thumb": "img/mblog.png",
        "hero": "img/mb.jpg",
        "categories": ["Python", "Flask", "MongoDB"],
        "slug": "microblog",
        "prod": "https://python-microblog-z9at.onrender.com/"
    },
    {
        "name": "Tech Times",
        "thumb": "img/blog.png",
        "hero": "img/bg.jpg",
        "categories": ["Node.js", "EJS", "MongoDB"],
        "slug": "tech-times"
    }
]

slug_to_project = {project["slug"]: project for project in projects}


@app.route("/")
def home():
    return render_template("home.html", projects = projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(
        f"project_{slug}.html",
        project = slug_to_project[slug]
    )

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
