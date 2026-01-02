from flask import render_template, request, Flask
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("\emotionDetector")
def emot_detect():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    displayed_response = "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. \\
    The dominant emotion is {}{} {}.".format(response["anger"], response["disgust"],response["fear"], \\
    response["joy"], response["sadness"],'\033[1m',response["dominant_emotion",'\033[0m'])
    return displayed_response
    
@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
