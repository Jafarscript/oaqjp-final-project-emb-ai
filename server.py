"""
This module initiates a Flask application for performing emotion detection.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the text provided via a URL query parameter for emotions.
    Displays an error message if the input is invalid or blank.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # 1. Process the statement using the emotion_detector function
    response = emotion_detector(text_to_analyze)

    # 2. Extract values from the returned dictionary
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # 3. Handle cases where the text may be invalid or blank
    if dominant_emotion is None:
        return "Invalid text! Please try again."

    # 4. Return the exact system response string requested by the customer
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    Renders the main index interface page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    