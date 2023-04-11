"""
This is the translator module. This module sets up the IBM language translator instanation
and converts text from english to french and vice versa
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
import sys

print(f'The path is: {sys.path}')

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
url)

def english_to_french(english_text):
    """
    This function returns text in french that was converted from english
    """
    if(english_text):
        french_text = language_translator.translate(english_text, model_id='en-fr').get_result()
        return french_text.get("translations")[0].get("translation")
    else:
        return ''

def french_to_english(french_text):
    """
    This function returns text in english that was converted from french
    """
    if(french_text):
        english_text = language_translator.translate(french_text, model_id='fr-en').get_result()
        return english_text.get("translations")[0].get("translation")
    else:
        return ''