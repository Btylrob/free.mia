from flask import Flask, render_template, request, redirect
import json
import datetime

app = Flask(__name__)




# Store tweets in memory
try:
    with open("msg.json", "r") as file:
        tweets = json.load(file)
except(FileNotFoundError, json.JSONDecodeError):
    tweets = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        if content:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d, %I:%M%p")
            username = "btylrob12"
            tweet = {"content" : content,"timestamp"  : timestamp, "username" : username}
            tweets.append(tweet)

            with open("msg.json", "w") as file:
                json.dump(tweets,file, indent=4)

        return redirect('/')
    return render_template('index.html', tweets=reversed(tweets))  # latest first

if __name__ == '__main__':
    app.run(debug=True)
