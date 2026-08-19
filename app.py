from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/products")
def products():
    return render_template("products.html")


@app.route("/orders")
def orders():
    return render_template("orders.html")


@app.route("/customers")
def customers():
    return render_template("customers.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/inventory")
def inventory():
    return render_template("inventory.html")


@app.route("/payments")
def payments():
    return render_template("payments.html")


@app.route("/reports")
def reports():
    return render_template("reports.html")


@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route("/logout")
def logout():
    return "Logout"


if __name__ == "__main__":
    app.run(debug=True)