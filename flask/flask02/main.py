#https://repl.it/talk/learn/Flask-Tutorial-Part-1-the-basics/26272
import random, string
from flask import Flask, render_template, request

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)




@app.route('/')  # What happens when the user visits the site
def base_page():

	random_num = random.randint(1, 6)  # Sets the random number
	return render_template(
		'base.html',  # Template file path, starting from the templates folder. 
		random_number=random_num  # Sets the variable random_number in the template
	)


@app.route('/2')
def page_2():
	
	random_str = random.choice(['Piedra','Papel','Tijera'])
	return render_template('site_2.html', random_str=random_str)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='localhost',  
		port=5002
	)