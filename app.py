from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def base():
    return render_template("base.html")






app.run("0.0.0.0",5000,debug=True)