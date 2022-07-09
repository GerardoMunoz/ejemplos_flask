#https://repl.it/talk/learn/Flask-Tutorial-Part-1-the-basics/26272
import random
from flask import Flask, render_template
app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)


@app.route('/')  # What happens when the user visits the site
def base_page():
    return render_template('base.html')


@app.route('/otra_pagina')
def page_2():
    return render_template('site_2.html')


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(  # Starts the site
        host='localhost',  
        port=5001
    )
