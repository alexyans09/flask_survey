from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Setting a secret key for session management


@app.get("/")
def index():
    # This route diplay the form
    return render_template("index.html")

@app.post("/process")
def process():
    # This route process the form
    # Save form data into session
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]
    return redirect("/result")

@app.get("/result")
def result():
    # Retrieve form data from session
    # This route show the result
    name = session["name"]
    location = session["location"]
    language = session["language"]
    comment = session["comment"]
    return render_template("result.html", name=name, comment = comment, location = location, language = language)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
