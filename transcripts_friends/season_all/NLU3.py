import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2019-07-12',
        iam_apikey='1erf8hkp6tJpTAVzh8_F7HmyRTWG6Rn9A567j5lyAcaM',
        url='https://gateway.watsonplatform.net/natural-language-understanding/api'
    )

response = natural_language_understanding.analyze(
    text='nothing happen really making together looking around trying you.\\n talking friends anything coming him.\\n probably everything too.\\n really excuse rachel alright forget actually something sounds course okay.\\n started wanted little thought this.\\n supposed okay.\\n getting sorry.\\n happened laughing apartment starts matter listen monica know.\\n chandler right.\\n yeah.\\n birthday pheebs please people everybody phoebe crying amazing anyway believe person picture stupid already thanks thinking remember almost married somebody someone here.\\n phoebe better another telling points out.\\n that.\\n pretty minute things beautiful laughs always enough couple wedding coffee yknow everyone saying thank totally oh.\\n taking second father seeing though entering called tomorrow office leaves bedroom friend monica listens joshua',

    features=Features(sentiment=SentimentOptions(targets=['stocks']))).get_result()

print(json.dumps(response, indent=2))