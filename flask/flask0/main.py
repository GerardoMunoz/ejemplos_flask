#https://j2logo.com/leccion-1-la-primera-aplicacion-flask/

import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
  app.run(
    host='localhost', 
    port=5000 # después del 2000 están disponibles, en principio.
  )

