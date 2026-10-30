'''Emotion Detector server'''
# Import Flask, render_template, request from the flask framework package :
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    '''Function to get response for emotion'''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if emotion res is None, indicating an error or invalid input
    if response is None:
        return "Invalid input! Try again."

    # Extract the emotion from the response
    angerscore = response['anger']
    disgustscore = response['disgust']
    fearscore = response['fear']
    joyscore = response['joy']
    sadnessscore = response['sadness']
    dominantemotion = response['dominant_emotion']
    # Return a formatted string with the emotion
    return f"""For the given statement, the system response is
    'anger': {angerscore}, disgust': {disgustscore}, 
    'fear': {fearscore}, 'joy': {joyscore} and 'sadness': {sadnessscore}. 
    The dominant emotion is {dominantemotion}."""

@app.route("/")
def render_index_page():
    '''Render main page'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
