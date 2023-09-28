""" Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
"""

from flask import Flask, render_template, request

from AI_EmotionRecognition.sentiment_analysis import sentiment_analyzer

app = Flask("SentimentAnalyser")


""" 
This code receives the text from the HTML interface and 
runs sentiment analysis over it using sentiment_analysis()
function. The output returned shows the label and its confidence 
score for the provided text.
"""


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    text_to_analyze = request.args.get("textToAnalyze")
    result = sentiment_analyzer(text_to_analyze)
    label = result["label"]
    score = result["score"]
    if label is None:
        return "Invalid input ! Try again."
    return "The given text has been identified as {} with a score of {}.".format(
        label.split("_")[1], score
    )


@app.route("/")
def render_index_page():
    """This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template("index.html")


""" This functions executes the flask app and deploys it on localhost:5000"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
