import flask
from flask import render_template, request

# My flask app
from BotResponses import bot_response

app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.render_template('index.html')


# Bot
@app.route('/bot')
def form():
    return flask.render_template('bot.html')


@app.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html', form_data=form_data)


@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return str(bot_response(user_text))


if __name__ == '__main__':
    app.run(debug=True)
