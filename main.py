from flask import Flask, render_template, url_for, redirect, send_from_directory
from datetime import datetime
import json
import random
import os
import subprocess

app = Flask(__name__)


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# Redirectors
@app.route("/")
def redirect_home():
    return redirect(url_for("home")), 301


@app.route("/<path:path>")
def redirecter(path):
    if path in ["favicon", "security", "robots"]:
        return redirect(f"/{path}")
    elif not path.startswith("gijstenberg4a2"):
        return redirect(f"/gijstenberg4a2/{path}")

    imgurl, artwork, artist, txtcolor = random_background()
    return render_template(
        "error.html",
        e="Error redirecting",
        errornum="404",
        message1="Deze pagina bestaat niet!",
        message2="De URL die je hebt opgevraagd bestaat niet.",
        imgurl=imgurl,
        artwork=artwork,
        artist=artist,
        txtcolor=txtcolor,
    ), 404


def get_commit_and_deploy_date():
    try:
        with open(os.path.join(BASE_DIR, "data", "last_deploy.txt"), "r") as f:
            latest_deploy_date = f.read().strip()
    except FileNotFoundError:
        latest_deploy_date = "unknown"
        print("No latest deploy date found.")

    latest_commit_hash = subprocess.check_output(["git", "log", "-1", "--pretty=format:%h"], cwd=BASE_DIR).strip().decode()
    latest_commit_hash_long = subprocess.check_output(["git", "log", "-1", "--pretty=format:%H"], cwd=BASE_DIR).strip().decode()
    latest_commit_timestamp = int(subprocess.check_output(["git", "log", "-1", "--pretty=format:%ct"], cwd=BASE_DIR).strip())
    latest_commit_date = datetime.fromtimestamp(latest_commit_timestamp).strftime("%d-%m-%Y om %H:%M:%S")

    comdepdata = {
        "latest_deploy_date": latest_deploy_date,
        "latest_commit_hash": latest_commit_hash,
        "latest_commit_hash_long": latest_commit_hash_long,
        "latest_commit_date": latest_commit_date,
    }

    return comdepdata


comdepdata = get_commit_and_deploy_date()


@app.context_processor
def inject_comdepdata():
    return comdepdata


# File routes


@app.route("/favicon.ico")
@app.route("/favicon")
def favicon():
    return send_from_directory("static", "favs/main.ico", mimetype="image/vnd.microsoft.icon")


@app.route("/.well-known/security.txt")
def security_txt():
    return send_from_directory("static", "security.txt", mimetype="text/plain")


@app.route("/security.txt")
def security_txt_redirect():
    return redirect(url_for("security_txt")), 301


@app.route("/robots")
@app.route("/robots.txt")
def robots():
    return send_from_directory("static", "robots.txt", mimetype="text/plain")


# Pages

pages = [
    {
        "title": "Blok 1",
        "undertitle_1": "Beeldend",
        "undertitle_2": "Het onzichtbare zichtbaar maken",
        "img": "/static/imgs/kryptos.jpg",
        "img_undertitle_1": "Kryptos (1990)",
        "img_undertitle_2": "Jim Sanborn",
        "url": "/blok-1",
    },
    {
        "title": "Blok 2",
        "undertitle_1": "Film",
        "undertitle_2": "Speciale effecten",
        "img": "/static/imgs/interstellar.png",
        "img_undertitle_1": "Interstellar (2014)",
        "img_undertitle_2": "O.a. Christopher Nolan",
        "url": "/blok-2",
    },
    {
        "title": "Blok 3",
        "undertitle_1": "Film",
        "undertitle_2": "Jouw interpretatie",
        "img": "/static/imgs/no_other_land1.jpg",
        "img_undertitle_1": "No Other Land (2024)",
        "img_undertitle_2": "O.a. Basel Adra",
        "url": "/blok-3",
    },
    {
        "title": "Blok 4",
        "undertitle_1": "Dans",
        "undertitle_2": "Vechtkunst",
        "img": "/static/imgs/sutra1.jpg",
        "img_undertitle_1": "Sutra (2008)",
        "img_undertitle_2": "O.a. Sidi Larbi Cherkaoui",
        "url": "/blok-4",
    },
    {
        "title": "Introductielessen",
        "undertitle_1": "",
        "undertitle_2": "Liefde",
        "img": "/static/imgs/intro/the_lovers_ii.jpg",
        "img_undertitle_1": "The Lovers II (1928)",
        "img_undertitle_2": "René Magritte",
        "url": "/introductielessen",
    },
    {
        "title": "Over mij",
        "undertitle_1": "",
        "undertitle_2": "",
        "img": "",
        "url": "/over-mij"
    },
    {
        "title": "Eigen initiatieven",
        "undertitle_1": "",
        "undertitle_2": "",
        "img": "",
        "url": "/eigen-initiatieven",
    },
]


@app.route("/gijstenberg4a2")
def home():
    return render_template("home.html", pagelist=pages)


@app.route("/gijstenberg4a2/over-mij")
def about_me():
    return render_template("about_me.html")


@app.route("/gijstenberg4a2/introductielessen")
def intro():
    return render_template("intro.html")


own_ini_list = [
    {
        "act_type": "Beeldend",
        "act_name": "Zoeken naar zingeving",
        "act_loc": "Kröller-Müller Museum (Otterlo)",
        "act_date": "30 oktober 2024",
        "pdf_url": "/static/pdfs/ei1-beeldend-zoekennaarzingeving.pdf",
        "img_url": "/static/imgs/own_ini/olijfgaard.jpg",
        "artwork": "Olijfgaard (1889)",
        "artist": "Vincent van Gogh",
        "bg": "yellow",
    },
    {
        "act_type": "Architectuur",
        "act_name": "Depot Boijmans Van Beuningen",
        "act_loc": "Museumpark (Rotterdam)",
        "act_date": "28 februari 2025",
        "pdf_url": "/static/pdfs/ei2-architectuur-depot.pdf",
        "img_url": "/static/imgs/own_ini/depot_boijmans_van_beuningen.jpg",
        "artwork": "Depot Boijmans van Beuningen",
        "artist": "MVRDV",
        "bg": "red",
    },
]


@app.route("/gijstenberg4a2/eigen-initiatieven")
def own_initiatives():
    return render_template("own_ini.html", own_ini_list=own_ini_list)


@app.route("/gijstenberg4a2/blok-1")
def period_1():
    return render_template("period_1.html")


@app.route("/gijstenberg4a2/blok-2")
def period_2():
    return render_template("period_2.html")


@app.route("/gijstenberg4a2/blok-3")
def period_3():
    return render_template("period_3.html")


@app.route("/gijstenberg4a2/blok-4")
def period_4():
    return render_template("period_4.html")


@app.route("/gijstenberg4a2/blok-5")
def period_5():
    return render_template("period_5.html")


@app.route("/gijstenberg4a2/blok-6")
def period_6():
    return render_template("period_6.html")


@app.route("/gijstenberg4a2/eindverslag")
def final_report():
    return render_template("final_report.html")


# Error pages
def random_background():
    try:
        with open(os.path.join(BASE_DIR, "data", "backgroundlist.json"), "r") as file:
            data = json.load(file)
        random_background_choice = random.choice(data)

        return (
            random_background_choice.get("imgurl"),
            random_background_choice.get("artwork"),
            random_background_choice.get("artist"),
            random_background_choice.get("txtcolor"),
        )
    except Exception:
        return (
            "/static/imgs/error/primordial_chaos.jpg",
            "Primordial Chaos - No 16 (1906-1907)",
            "Hilma af Klint",
            "white",
        )


@app.errorhandler(404)
def not_found(e):
    imgurl, artwork, artist, txtcolor = random_background()
    return (
        render_template(
            "error.html",
            e=e,
            errornum="404",
            message1="Deze pagina bestaat niet!",
            message2="De URL die je hebt opgevraagd bestaat niet.",
            imgurl=imgurl,
            artwork=artwork,
            artist=artist,
            txtcolor=txtcolor,
        ),
        404,
    )


@app.errorhandler(500)
def internal_error(e):
    imgurl, artwork, artist, txtcolor = random_background()
    return (
        render_template(
            "error.html",
            e=e,
            errornum="500",
            message1="Oeps! Er is iets misgegaan",
            message2="Er lijkt een probleem te zijn op de server. De pagina kon niet worden geladen. Probeer het later opnieuw.",
            imgurl=imgurl,
            artwork=artwork,
            artist=artist,
            txtcolor=txtcolor,
        ),
        500,
    )


if __name__ == "__main__":
    app.run(debug=True)
