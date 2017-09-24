import json
import os
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 \
	as Features

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def getJson():
	with open(os.path.join(__location__, 'MHacksX-Watson.json'), "a+") as jsonFile:
		try:
			jsonFile.seek(0)  # rewind
			data = json.load(jsonFile)
		except:
			data = {"msg": 'error'}
		jsonFile.close()
		return data

credentials = getJson()
print(credentials)
natural_language_understanding = NaturalLanguageUnderstandingV1(
	username=credentials['username'],
	password=credentials['password'],
	version=credentials['version'])

def getSentiment(text=None, url=None):
	if(url==None):
		response = natural_language_understanding.analyze(
			text=text,
			features=[
				Features.Sentiment(
				# Sentiment options
					targets=[
						"bitcoin"
					]
				)
			]
		)
	else:
		response = natural_language_understanding.analyze(
			url=url,
			features=[
				Features.Sentiment(
				# Sentiment options
					targets=[
						"bitcoin"
					]
				)
			]
		)
	return json.dumps(response, indent=2)