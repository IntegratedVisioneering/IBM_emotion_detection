''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

""" This is the GET route for retrieving the data and providing the response"""
@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """Retrieve the text to analyze from the request arguments"""
    text_to_analyze = request.args.get('textToAnalyze')
    #ass the text to the sentiment_analyzer function and store the response
    response = sentiment_analyzer(text_to_analyze)
    #Extract the label and score from the response
    label = response['label']
    score = response['score']
    #error handling
    #Check if the label is None, indicating an error or invalid input
    if label is None:
        return "Invalid input! Try again."
    #Return a formatted string with the sentiment label and score
    return f"The given text has been identified as {label.split('_')[1]} with a score of {score}."

#This function initiates the rendering of the main applicationpage over the Flask channel
@app.route("/")
def render_index_page():
    """returns the index tenplate information"""
    return render_template('index.html')

#This functions executes the flask app and deploys it on localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
