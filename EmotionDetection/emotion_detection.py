import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the emotion detector API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

   # If the response status code is 200, extract  the response
    if response.status_code == 200:
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        res = formatted_response['emotionPredictions']
        dic=res[0]["emotion"]
        sortdic=dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        print(sortdic)
        first_item = next(iter(sortdic.items()))
        print(first_item)
        dic["dominant_emotion"]= first_item[0]
        res= dic
        
    # If the response status code is 500, set response to None
    elif response.status_code == 500:
        res = None
        
    # For any other unexpected status codes, set response to None
    else:
        res = None
        

    # Return the response 
    return (res)

