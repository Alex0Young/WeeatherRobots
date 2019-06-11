# -*- coding: utf-8 -*-
import urllib.request as ul_re
import json
import urllib
def getAccess():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=t8LVuMdxnVcQu06f1HcRzZkG&client_secret=AkrpSSKA6LuEK7IhN3SSbMF5EguaziGl'
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response=urllib.request.urlopen(request).read()
    # print(type(response))
    content = response.decode('utf-8')
    if content:
        data = content.split(',', 5)
        return data[3][16:-1]
    else:
        return 0

def getRes():
    access_token = getAccess()
    url = 'https://aip.baidubce.com/rpc/2.0/unit/bot/chat?access_token=' + access_token
    keyword = input('Please input your question: ')
    post_data  = {
	    "bot_session": "",
	    "log_id": "7758521",
	    "request": {
		    "bernard_level": 0,
		    "client_session": "{\"client_results\":\"\", \"candidate_options\":[]}",
		    "query": keyword,
		    "query_info": {
			    "asr_candidates": [],
			    "source": "KEYBOARD",
			    "type": "TEXT"
		    },
		    "updates": "",
		    "user_id": "88888"
	    },
	    "bot_id": "58846",
	    "version": "2.0"
    }
    encoded_data = json.dumps(post_data).encode('utf-8')
    headers = {'Content-Type': 'application/json'}

    request = ul_re.Request(url, data=encoded_data, headers=headers)
    response = ul_re.urlopen(request)
    content = response.read()

    result = str(content,'utf-8')
    result = json.loads(result)
    print(type(result))

    intent = result['result']['response']['schema']['intent']
# locname = result['result']['response']['schema']['slots']
    locname = result['result']['response']['schema']['slots'][0]['normalized_word']
    time = result['result']['response']['schema']['slots'][1]['normalized_word']
    # weather = result['result']['response']['schema']['slots'][2]['normalized_word']
    bot_session = result['result']['bot_session']
    bots = json.loads(bot_session)
    session = bots['session_id']
# print('session: '+session)
    say = result['result']['response']['action_list'][0]['say']
    type1 = result['result']['response']['action_list'][0]['type']
    # print('bot_session: ' + bot_session)
    print('say: ' + say)
    print('type1: ' + type1)
    print('intent: ' + intent)
    print('locname: ' + str(locname))
    print('time: ' + time)
    # print('weather: ' + weather)
    print(bot_session)
    # print(result)
    return bot_session

def getRes2(bot):
    word = input('Pleas 2: ')
    access_token = getAccess()
    url = 'https://aip.baidubce.com/rpc/2.0/unit/bot/chat?access_token=' + access_token
    # keyword = input('Please input your question: ')
    post_data  = {
	    "bot_session": bot,
	    "log_id": "7758521",
	    "request": {
		    "bernard_level": 0,
		    "client_session": "{\"client_results\":\"\", \"candidate_options\":[]}",
		    "query": word,
		    "query_info": {
			    "asr_candidates": [],
			    "source": "KEYBOARD",
			    "type": "TEXT"
		    },
		    "updates": "",
		    "user_id": "88888"
	    },
	    "bot_id": "58846",
	    "version": "2.0"
    }
    encoded_data = json.dumps(post_data).encode('utf-8')
    headers = {'Content-Type': 'application/json'}

    request = ul_re.Request(url, data=encoded_data, headers=headers)
    response = ul_re.urlopen(request)
    content = response.read()
    result = str(content,'utf-8')
    result = json.loads(result)
    print(type(result))
    intent = result['result']['response']['schema']['intent']
# locname = result['result']['response']['schema']['slots']
    locname = result['result']['response']['schema']['slots'][0]['normalized_word']
    time = result['result']['response']['schema']['slots'][1]['normalized_word']
    weather = result['result']['response']['schema']['slots'][2]['normalized_word']
    bot_session = result['result']['bot_session']
    bots = json.loads(bot_session)
    session = bots['session_id']
# print('session: '+session)
    say = result['result']['response']['action_list'][0]['say']
    type1 = result['result']['response']['action_list'][0]['type']
    # print('bot_session: ' + bot_session)
    print('say: ' + say)
    print('type1: ' + type1)
    print('intent: ' + intent)
    print('locname: ' + str(locname))
    print('time: ' + time)
    print('weather: ' + weather)
    # print(bot_session)
    # print(result)

bot = getRes()
getRes2(bot)