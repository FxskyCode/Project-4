from flask import Flask, request, jsonify, render_template, redirect
import numpy as np
import markdown.extensions.fenced_code
import tools.sql_queries as sql
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

app = Flask(__name__)

# Render the markdwon
@app.route("/")
def main_page ():
    #readme_file = open("README.md", "r")
    #return markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return render_template("index.html", )

# GET:
# SQL get everything
@app.route("/all/")
def all ():
    return jsonify(sql.get_everything())

# SQL get everything from one character
@app.route("/<name>/", )
def everithing_from_characters (name):
    return jsonify(sql.get_everything_from_character(name))

# SQL get just dialogues from one character
@app.route("/lines/<name>/", )
def lines_from_characters (name):
    return jsonify(sql.get_just_dialogue(name))

# SQL get the mean of sentiment analysis of each line from one character
@app.route("/sa/<name>/", )
def sa_from_character (name):
    everything = sql.get_just_dialogue(name)
    return jsonify(np.mean([sia.polarity_scores(i["line"])["compound"] for i in everything]))

# SQL get all characters and their total lines
@app.route("/characters/")
def characters ():
    return jsonify(sql.get_characters())



# POST:

@app.route("/add/")
def form():
    print("patata")
    # Passing to my function: do the inserr
    return render_template('form.html')


@app.route("/add-row/", methods=['POST'])
def try_post():
    print("patata")
    if request.method == 'POST':
        season = request.form.get('season')
        episode = request.form.get('episode')
        title = request.form.get('title')
        scene = request.form.get('scene')
        speaker = request.form.get('speaker')
        line = request.form.get('line')
        print(season)
        print(episode)
        print(title)
        print(request)
        print(request.method)

        sql.insert_one_row(season, episode, title, scene, speaker, line)
        return "roger"


if __name__ == "__main__":  
    app.run(port=9000, debug=True)