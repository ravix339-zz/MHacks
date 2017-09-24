# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import sys

import requests

from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

# Instantiates a client
client = language.LanguageServiceClient()

def getSentiment(text=None, url=None):
	if(url==None):
		document = types.Document(
		    content=text,
		    type=types.Document.Type.PLAIN_TEXT)
		# Detects the sentiment of the text
		result = client.analyze_sentiment(document=document).document_sentiment
	else:
		html = requests.get(url)
		document = types.Document(
		    content=html.content,
		    type="HTML")
		result = client.analyze_sentiment(document=document).document_sentiment
	return (result.score, result.magnitude)


