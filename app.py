from flask import (
    Flask,
    render_template,
    url_for,
    redirect,
    send_from_directory,
    request,
)

app = Flask(__name__)


@app.before_request
def handle_redirects():
    path = request.path
    if path == "/":
        return redirect(url_for("home")), 301
    if path.lstrip("/") in ["favicon", "security", "robots"]:
        return None
    if not path.startswith("/gijstenberg4a2") and not path.startswith("/static"):
        return redirect(f"/gijstenberg4a2{path}")


# File routes


@app.route("/favicon.ico")
@app.route("/favicon")
def favicon():
    return send_from_directory(
        "static/assets/icons", "favicon.ico", mimetype="image/vnd.microsoft.icon"
    )


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


@app.route("/gijstenberg4a2")
def home():
    return render_template("home.html")


@app.route("/gijstenberg4a2/over-mij")
def about_me():
    return render_template("about_me.html")


@app.route("/gijstenberg4a2/introductielessen")
def intro():
    return render_template("intro.html")


@app.route("/gijstenberg4a2/eigen-initiatieven")
def own_initiatives():
    return render_template("own_initiatives.html")


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
def render_error(e, errornum, message1, message2):
    return render_template(
        "error.html",
        e=e,
        errornum=errornum,
        message1=message1,
        message2=message2,
        imgurl=url_for("static", filename="images/error/primordial_chaos.jpg"),
        artwork="Primordial Chaos - No 16 (1906-1907)",
        artist="Hilma af Klint",
        txtcolor="white",
    )


@app.errorhandler(404)
def not_found(e):
    return (
        render_error(
            e,
            "404",
            "Deze pagina bestaat niet!",
            "De URL die je hebt opgevraagd bestaat niet.",
        ),
        404,
    )


@app.errorhandler(500)
def internal_error(e):
    return (
        render_error(
            e,
            "500",
            "Oeps! Er is iets misgegaan",
            "Er lijkt een probleem te zijn op de server. De pagina kon niet worden geladen. Probeer het later opnieuw.",
        ),
        500,
    )


if __name__ == "__main__":
    app.run(debug=True)
