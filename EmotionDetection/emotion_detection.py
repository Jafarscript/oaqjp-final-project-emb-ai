import json  # Import the json library to parse the text response
import requests  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):
    """
    Sends text to the Watson Emotion Predict service and formats the output.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json=myobj, headers=header)
    
    # 1. Parse the JSON text string into a Python dictionary
    formatted_response = json.loads(response.text)
    
    # 2. Extract the main emotion dictionary nested deep inside the response structure
    # Path: emotionPredictions -> first item [0] -> emotion
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # 3. Extract the individual scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # 4. Find the dominant emotion (the key with the highest numeric value)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # 5. Package the data into the exact format requested
    output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return output
