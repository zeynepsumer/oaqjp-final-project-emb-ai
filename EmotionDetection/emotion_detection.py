import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    
    # If the response status code is 200, extract the results
    if response.status_code == 200:
        emotion_predictions = formatted_response["emotionPredictions"][0]["emotion"]
        anger_score = emotion_predictions["anger"]
        disgust_score = emotion_predictions["disgust"]    
        fear_score = emotion_predictions["fear"]
        joy_score = emotion_predictions["joy"]
        sadness_score = emotion_predictions["sadness"]
        dominant_emotion = max(emotion_predictions, key = emotion_predictions.get)

    # If the response status code is 400, set results to None
    elif response.status_code == 400:
        emotion_predictions = None
        anger_score = None
        disgust_score = None  
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    new_response = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
        }

    return new_response
