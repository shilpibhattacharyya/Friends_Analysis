import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2019-07-12',
        iam_apikey='1erf8hkp6tJpTAVzh8_F7HmyRTWG6Rn9A567j5lyAcaM',
        url='https://gateway.watsonplatform.net/natural-language-understanding/api'
    )
##rachel
response = natural_language_understanding.analyze(
    text='nothing happen really making together looking around trying you.\\n talking friends anything coming him.\\n probably everything too.\\n really excuse rachel alright forget actually something sounds course okay.\\n started wanted little thought this.\\n supposed okay.\\n getting sorry.\\n happened laughing apartment starts matter listen monica know.\\n chandler right.\\n yeah.\\n birthday pheebs please people everybody phoebe crying amazing anyway believe person picture stupid already thanks thinking remember almost married somebody someone here.\\n phoebe better another telling points out.\\n that.\\n pretty minute things beautiful laughs always enough couple wedding coffee yknow everyone saying thank totally oh.\\n taking second father seeing though entering called tomorrow office leaves bedroom friend monica listens joshua',
    features=Features(emotion=EmotionOptions())).get_result()

print(json.dumps(response, indent=2))

##ross
response = natural_language_understanding.analyze(
    text='amazing that.\\n anything alright please looking start rachel everything minute wanted another taking actually thought always talking nothing happened okay.\\n friend chandler really this.\\n saying thing happen people totally coming little tomorrow someone making laugh second together married okay.\\n course stupid couple probably something monica laughing believe leaf really everyone birthday point thank listens already remember sound better pheebs you.\\n telling seeing around beautiful thinking pretty getting trying yeah.\\n phoebe out.\\n him.\\n entering here.\\n somebody excuse anyway supposed everybody know enough coffee listen monica apartment called matter sorry.\\n started wedding thanks father cry almost friend phoebe forget though too.\\n know.\\n picture right.\\n bedroom person oh.\\n office',
    features=Features(emotion=EmotionOptions())).get_result()

print(json.dumps(response, indent=2))

##monica
response = natural_language_understanding.analyze(
    text='everything stupid minute phoebe someone him.\\n this.\\n you.\\n believe rachel somebody chandler monica people person tomorrow anything really friend listen everyone everybody around looking thanks thank seeing thing pretty getting something entering called always actually coming please friend remember laughing that.\\n listens alright leaf nothing start another started picture point supposed birthday phoebe thought right.\\n happen course sound trying wedding making couple really laugh totally pheebs better talking sorry.\\n enough little forget already almost cry probably yknow taking bedroom apartment here.\\n happened amazing thinking beautiful too.\\n okay.\\n know.\\n wanted matter out.\\n though father yeah.\\n okay.\\n together anyway saying second excuse married monica oh.\\n telling office coffee joshua',
    features=Features(emotion=EmotionOptions())).get_result()

print(json.dumps(response, indent=2))

##phoebe
response = natural_language_understanding.analyze(
    text='taking sound rachel here.\\n chandler saying thought monica alright better probably seeing you.\\n together laugh really matter nothing coming birthday friend thinking talking leaf thing around believe someone start minute people right.\\n course getting phoebe person little something excuse looking amazing everyone everybody that.\\n point please already thank entering yeah.\\n really wanted anything bedroom wedding married actually pretty him.\\n friend trying making okay.\\n apartment forget tomorrow listen stupid remember always sorry.\\n this.\\n yknow totally supposed called oh.\\n though anyway listens another okay.\\n everything know.\\n thanks happen pheebs out.\\n almost telling somebody couple beautiful second laughing enough too.\\n monica office picture father happened coffee started cry',
    features=Features(emotion=EmotionOptions())).get_result()

print(json.dumps(response, indent=2))

#chandler
response = natural_language_understanding.analyze(
    text='little monica probably phoebe people supposed almost someone really tomorrow believe rachel anything everything really happened please trying something know.\\n chandler too.\\n father talking telling you.\\n him.\\n already start pheebs though taking around actually leaf apartment picture this.\\n birthday married together thing looking sound forget thought point everyone amazing second coming another somebody listens remember stupid course called pretty couple laugh friend getting happen always nothing listen better that.\\n enough thank alright totally right.\\n everybody beautiful yknow office sorry.\\n entering anyway thinking thanks saying out.\\n excuse wanted wedding cry person okay.\\n monica seeing yeah.\\n okay.\\n here.\\n bedroom matter friend coffee minute started laughing making oh.\\n joshua phoebe',
    features=Features(emotion=EmotionOptions())).get_result()

print(json.dumps(response, indent=2))

#joey
response = natural_language_understanding.analyze(
    text='believe rachel around almost thinking you.\\n forget really someone okay.\\n totally alright something thing yeah.\\n saying thank that.\\n better together tomorrow probably happened happen really little actually listen nothing anything course start chandler thought matter taking another second point know.\\n trying friend too.\\n phoebe supposed picture laughing pheebs always minute everyone monica people looking getting please leaf sound remember bedroom person everything called coming telling beautiful apartment oh.\\n okay.\\n already started stupid here.\\n friend talking though excuse laugh sorry.\\n married thanks coffee pretty out.\\n father this.\\n wanted cry anyway making entering everybody seeing yknow birthday enough amazing wedding right.\\n phoebe listens couple monica somebody him.\\n office',
    features=Features(emotion=EmotionOptions())).get_result()

print(json.dumps(response, indent=2))

