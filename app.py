from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        beruf = request.form.get("beruf")
        return f"Hallo {name}, wir suchen Jobs für: {beruf}!"
    return render_template("index.html")

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)), debug=True)

