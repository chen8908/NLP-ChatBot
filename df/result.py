
import google.cloud.dialogflow_v2 as dialogflow
from google.api_core.exceptions import InvalidArgument
from fastapi import HTTPException


DIALOGFLOW_PROJECT_ID = 'our-axon-321206'
DIALOGFLOW_LANGUAGE_CODE = 'zh-TW'
SESSION_ID = 'anything'

def get_query(msg):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=msg, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)

    return session_client, session, query_input

def get_df_answer(msg):
    session_client, session, query_input = get_query(msg)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise HTTPException(status_code=400, detail='InvalidArgument')

    result = {
        'intent': response.query_result.intent.display_name,
        'confidence': response.query_result.intent_detection_confidence,
        'fulfillment': response.query_result.fulfillment_text
    }

    return result
