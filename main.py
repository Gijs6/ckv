from flask import Flask, render_template, url_for, redirect, send_from_directory
import json
import random


app = Flask(__name__)


# Redirecters

@app.route("/")
def redirecthome():
    return redirect(url_for('home')), 301


@app.route('/<path:path>')
def redirecter(path):
    if path in ["favicon", "security", "robots"]:
        return redirect(f"/{path}")
    elif not path.startswith("gijsckv"):
        return redirect(f"/gijsckv/{path}")
    try:
        afburl, kunstwerk, kunstenaar, txtcolor = randomBackground()
    except:
        afburl = "/static/afbs/error/cirkels2.jpg"
        kunstwerk = "Primordial Chaos - No 16 (1906-1907)"
        kunstenaar = "Hilma af Klint"
        txtcolor = "white"
    return render_template("ckverror.html", e="Error redirecting", errornum="404", errorbericht1="Die pagina bestaat niet!", errorbericht2="De URL die je hebt verzocht bestaat niet.", afburl=afburl, kunstwerk=kunstwerk, kunstenaar=kunstenaar, txtcolor=txtcolor), 404



# File stuff

@app.route('/favicon.ico')
@app.route('/favicon')
def favicon():
    return send_from_directory('static', "favs/cirkels.ico", mimetype='image/vnd.microsoft.icon')


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

@app.route("/gijsckv")
def home():
    with open("static/data/paglijst.json", "r") as file:
        paglijst = json.load(file)
    return render_template("ckvhome.html", pagdata=paglijst)


@app.route("/gijsckv/over-mij")
def over_mij():
    return render_template("ckvovermij.html")

@app.route("/gijsckv/introductielessen")
def introductie():
    return render_template("ckvintro.html")

@app.route("/gijsckv/eigen-initiatieven")
def eigen_initiatieven():
    return render_template("ckvei.html")

@app.route("/gijsckv/blok-1")
def blok1():
    return render_template("ckvb1.html")

@app.route("/gijsckv/blok-2")
def blok2():
    return render_template("ckvb2.html")

@app.route("/gijsckv/blok-3")
def blok3():
    return render_template("ckvb3.html")

@app.route("/gijsckv/blok-4")
def blok4():
    return render_template("ckvb4.html")

@app.route("/gijsckv/colofon")
def colofon():
    return render_template("ckvcolofon.html")




# Short routs (redirects)
# Prefixed by the main redirecter

@app.route("/gijsckv/om")
@app.route("/gijsckv/overmij")
def over_mij_redi():
    return redirect("/gijsckv/over-mij")

@app.route("/gijsckv/il")
@app.route("/gijsckv/intro")
@app.route("/gijsckv/introles")
def introductie_redi():
    return redirect("/gijsckv/introductielessen")

@app.route("/gijsckv/ei")
@app.route("/gijsckv/eigini")
@app.route("/gijsckv/eigeninitiatieven")
def eigen_initiatieven_redi():
    return redirect("/gijsckv/eigen-initiatieven")

@app.route("/gijsckv/b1")
@app.route("/gijsckv/blok1")
def blok1_redi():
    return redirect("/gijsckv/blok-1")

@app.route("/gijsckv/b2")
@app.route("/gijsckv/blok2")
def blok2_redi():
    return redirect("/gijsckv/blok-2")

@app.route("/gijsckv/b3")
@app.route("/gijsckv/blok3")
def blok3_redi():
    return redirect("/gijsckv/blok-3")

@app.route("/gijsckv/b4")
@app.route("/gijsckv/blok4")
def blok4_redi():
    return redirect("/gijsckv/blok-4")

@app.route("/gijsckv/cf")
@app.route("/gijsckv/col")
def colofon_redi():
    return redirect("/gijsckv/colofon")



def randomBackground():
    with open("static/data/backgroundlist.json", "r") as file:
        data = json.load(file)
    randomBackgroundChoice = random.choice(data)

    return randomBackgroundChoice.get("afburl"), randomBackgroundChoice.get("kunstwerk"), randomBackgroundChoice.get("kunstenaar"), randomBackgroundChoice.get("txtcolor")




# Error pages

@app.errorhandler(404)
def not_found(e):
    try:
        afburl, kunstwerk, kunstenaar, txtcolor = randomBackground()
    except:
        afburl = "/static/afbs/error/cirkels2.jpg"
        kunstwerk = "Primordial Chaos - No 16 (1906-1907)"
        kunstenaar = "Hilma af Klint"
        txtcolor = "white"
    return render_template("ckverror.html", e=e, errornum="404", errorbericht1="Die pagina bestaat niet!", errorbericht2="De URL die je hebt verzocht bestaat niet.", afburl=afburl, kunstwerk=kunstwerk, kunstenaar=kunstenaar, txtcolor=txtcolor), 404

@app.errorhandler(500)
def internal_error(e):
    try:
        afburl, kunstwerk, kunstenaar, txtcolor = randomBackground()
    except:
        afburl = "/static/afbs/error/cirkels2.jpg"
        kunstwerk = "Primordial Chaos - No 16 (1906-1907)"
        kunstenaar = "Hilma af Klint"
        txtcolor = "white"
    return render_template("ckverror.html", e=e, errornum="500", errorbericht1="Oeps! Er is iets misgegaan", errorbericht2="Er lijkt een probleem te zijn op de server. De pagina kon niet worden geladen. Probeer het later nog eens.", afburl=afburl, kunstwerk=kunstwerk, kunstenaar=kunstenaar, txtcolor=txtcolor), 500


if __name__ == '__main__':
    app.run(debug=True)
