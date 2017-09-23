# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import requests

from oauth2client.client import GoogleCredentials
credentials = GoogleCredentials.get_application_default()

# Instantiates a client
client = language.LanguageServiceClient()

def getSentiment(url):
	html = requests.get(url)
	document = types.Document(
	    content=html.content,
	    type="HTML")
	print(html.content)
	# Detects the sentiment of the text
	sentiment = client.analyze_sentiment(document=document).document_sentiment

	print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
	return(sentiment.score, sentiment.magnitude)
