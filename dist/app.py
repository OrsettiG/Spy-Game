from flask import Flask, render_template, request
import random
from secret_server import generate_player_roles


app = Flask(__name__)
app.static_folder = 'static'

# The main game route will be on index
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        players = generate_player_roles(request.form)
        return render_template('template.html', players=players)
    return render_template('template.html')

if __name__ == "__main__":
    app.run(debug=True)