from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def cadastro():
    return render_template("home.html")



@app.route("/vistoria")
def vistoria():
    return render_template("vistoria.html")



if __name__ == "__main__":
    app.run(debug=True)