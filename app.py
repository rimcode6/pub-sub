from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# This dictionary will be used to store subscriptions
subscriptions = {}

# This dictionary will be used to store messages
messages = {}


@app.route('/')
def index():
    return render_template('index.html', topics=subscriptions.keys())


@app.route('/publish', methods=['POST'])
def publish():
    topic = request.form['topic']
    message = request.form['message']
    if topic in subscriptions:
        messages[topic] = message
    return redirect(url_for('index'))


@app.route('/subscribe', methods=['POST'])
def subscribe():
    topic = request.form['topic']
    subscriptions[topic] = None
    return redirect(url_for('index'))


@app.route('/topic/<topic>')
def topic(topic):
    if topic in messages:
        return render_template('topic.html', topic=topic, message=messages[topic])
    else:
        return "No messages yet", 404


if __name__ == '__main__':
    app.run(debug=True)