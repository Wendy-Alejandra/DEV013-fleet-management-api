"""Flask application"""
# Flask class. Instance of this class will be our WSGI application (Web Server Gateway Interface).
from flask import Flask, render_template

# Instance of Flask class. Argument __name__ is the name of the application’s module or package.
app = Flask(__name__)

@app.route("/")
def index():
    """Index view"""
#    return "<h1>Hola</h1>"
    return render_template("index.html")

# If the name of the app from main route __main__ then execute our app with the run() cmd
if __name__ == "__main__":
    app.run(debug=True, port=5000) # Debugger activated
