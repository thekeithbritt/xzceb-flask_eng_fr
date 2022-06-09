'''This module translates from English to French
and French to English using IBM Language Translator'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.' \
    'language-translator.watson.cloud.ibm.com/instances/20e20b1d-bccb-4a27-937f-d8b2a6349c13')

def englishToFrench(englishText):
    '''Function that translates from English to French'''

    translation = language_translator.translate(text = englishText, model_id = 'en-fr').get_result()
    frenchText = translation['translations'][0]['translation']

    return frenchText

def frenchToEnglish(frenchText):
    '''Function that translates from French to English'''

    translation = language_translator.translate(text = frenchText, model_id = 'fr-en').get_result()
    englishText = translation['translations'][0]['translation']
    return englishText
