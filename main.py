from flask import Flask, render_template, url_for, redirect, send_from_directory
import json
import random
import os


app = Flask(__name__)


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Redirecters

@app.route("/")
def redirecthome():
    return redirect(url_for('home')), 301


@app.route('/<path:path>')
def redirecter(path):
    if path in ["favicon", "security", "robots"]:
        return redirect(f"/{path}")
    elif not path.startswith("gijstenberg4a2"):
        return redirect(f"/gijstenberg4a2/{path}")
    
    imgurl, artwork, artist, txtcolor = randomBackground()
    return render_template("error.html", e="Error redirecting", errornum="404", message1="Die pagina bestaat niet!", message2="De URL die je hebt verzocht bestaat niet.", imgurl=imgurl, artwork=artwork, artist=artist, txtcolor=txtcolor), 404



# File stuff

@app.route('/favicon.ico')
@app.route('/favicon')
def favicon():
    return send_from_directory('static', "favs/main.ico", mimetype='image/vnd.microsoft.icon')


@app.route("/.well-known/security.txt")
def securitytxt():
    return send_from_directory('static', "security.txt", mimetype="text/plain")

@app.route("/security.txt")
def securitytxtredirect():
    return redirect(url_for('securitytxt')), 301

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
        "img": "/static/imgs/brava.jpg",
        "img_undertitle_1": "Brava! (2022)",
        "img_undertitle_2": "EJ Hill",
        "url": "/blok-1"
    },
    {
        "title": "Blok 2",
        "undertitle_1": "Film",
        "undertitle_2": "Speciale effecten",
        "img": "/static/imgs/Interstellar.png",
        "img_undertitle_1": "Interstellar (2014)",
        "img_undertitle_2": "O.a. Christopher Nolan",
        "url": "/blok-2"
    },
    {
        "title": "Blok 3",
        "undertitle_1": "Film",
        "undertitle_2": "Jouw interpretatie",
        "img": "/static/imgs/nootherland.jpg",
        "img_undertitle_1": "No Other Land (2024)",
        "img_undertitle_2": "O.a. Basel Adra",
        "url": "/blok-3"
    },
    {
        "title": "Blok 4",
        "undertitle_1": "Dans",
        "undertitle_2": "Vechtkunst",
        "img": "/static/imgs/sutra.jpg",
        "img_undertitle_1": "Sutra (2008)",
        "img_undertitle_2": "O.a. Sidi Larbi Cherkaoui",
        "url": "/blok-4"
    },
    {
        "title": "Introductielessen",
        "undertitle_1": "",
        "undertitle_2": "Liefde",
        "img": "/static/imgs/LoversIIMargritte.jpg",
        "img_undertitle_1": "The Lovers II (1928)",
        "img_undertitle_2": "René Magritte",
        "url": "/introductielessen"
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
        "url": "/eigen-initiatieven"
    }
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
        "act_name": "Zoeken naar Zingeving",
        "act_loc": "Kröller-Müller Museum (Otterlo)",
        "act_date": "30 oktober 2024",
        "pdf_url": "/static/pdfs/EI1-Beeldend-ZoekenNaarZingeving.pdf",
        "img_url": "/static/imgs/own_ini/olijfgaard.jpg",
        "artwork": "Olijfgaard (1889)",
        "artist": "Vincent van Gogh",
        "bg": "yellow"
    },
    {   
        "act_type": "Architectuur",
        "act_name": "Depot Boijmans Van Beuningen",
        "act_loc": "Museumpark (Rotterdam)",
        "act_date": "28 februari 2025",
        "pdf_url": "/static/pdfs/EI2-Architectuur-Depot.pdf",
        "img_url": "/static/imgs/own_ini/depot.jpg",
        "artwork": "Depot Boijmans van Beuningen",
        "artist": "MVRDV",
        "bg": "red"
    }
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




# Error pages

def randomBackground():
    try:
        with open(os.path.join(BASE_DIR, "data", "backgroundlist.json"), "r") as file:
            data = json.load(file)
        randomBackgroundChoice = random.choice(data)

        return randomBackgroundChoice.get("imgurl"), randomBackgroundChoice.get("artwork"), randomBackgroundChoice.get("artist"), randomBackgroundChoice.get("txtcolor")
    except Exception:
        return "/static/imgs/error/Primordial_Chaos.jpg", "Primordial Chaos - No 16 (1906-1907)", "Hilma af Klint", "white"


@app.errorhandler(404)
def not_found(e):
    imgurl, artwork, artist, txtcolor = randomBackground()
    return render_template("error.html", e=e, errornum="404", message1="Die pagina bestaat niet!", message2="De URL die je hebt verzocht bestaat niet.", imgurl=imgurl, artwork=artwork, artist=artist, txtcolor=txtcolor), 404

@app.errorhandler(500)
def internal_error(e):
    imgurl, artwork, artist, txtcolor = randomBackground()
    return render_template("error.html", e=e, errornum="404", message1="Oeps! Er is iets misgegaan", message2="Er lijkt een probleem te zijn op de server. De pagina kon niet worden geladen. Probeer het later nog eens.", imgurl=imgurl, artwork=artwork, artist=artist, txtcolor=txtcolor), 505


if __name__ == '__main__':
    app.run(debug=True)
