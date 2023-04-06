
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Set up authenticator with API key
authenticator = IAMAuthenticator(apikey='Pd5cO8UjWdpu6eUeGoxoFE4jv-V-Skp8utxDVq2Y0tx8')

# Set up Language Translator service instance
translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

# Set service URL
translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/8db497f5-0e78-474d-8884-b26288f63c01')

def english_to_french(english_text):
    #select source and target language
    source_lang = 'en'
    target_lang = 'fr'

    # Call the translate() method to translate the text
    translation = translator.translate(
        text=english_text,
        source=source_lang,
        target=target_lang).get_result()

    # Extract the translated text from the response
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    #select source and target language
    source_lang = 'fr'
    target_lang = 'en'

    # Call the translate() method to translate the text
    translation = translator.translate(
        text=french_text,
        source=source_lang,
        target=target_lang).get_result()

    # Extract the translated text from the response
    english_text = translation['translations'][0]['translation']
    return english_text   

