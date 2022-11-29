import flask
import os
from flask import send_from_directory, request, render_template
import pyjokes
import randfacts

app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    content = req['queryResult']['parameters']['content']
    if content == 'joke':
        response = pyjokes.get_joke(language = 'en', category = 'neutral' )
    elif content == 'fact':
        response = randfacts.get_fact()
    else:
        response = "say that again mate!"

    return {
        'fulfillmentText': f'Simon says, {response}'
    }

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()