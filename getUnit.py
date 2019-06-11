# encoding:utf-8
import urllib.request
import urllib3, sys,urllib
import ssl
import json
import sys
sys.path.append('..')
from Weather import getWeather as gw
import time,datetime
import urllib.request as ul_re
import urllib
# client_id 为官网获取的AK， client_secret 为官网获取的SK
#获取认证
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

#开始会话
def getUnitSession1(keyword):
    access_token = getAccess()
    if access_token != 0:
        # print(access_token)
        # url = 'https://aip.baidubce.com/rpc/2.0/unit/bot/chat?access_token=' + access_token
        # post_data = "{\"bot_session\":\"\",\"log_id\":\"7758521\",\"request\":{\"bernard_level\":1,\"client_session\":\"{\\\"client_results\\\":\\\"\\\", \\\"candidate_options\\\":[]}\",\"query\":\""+keyword+"\",\"query_info\":{\"asr_candidates\":[],\"source\":\"KEYBOARD\",\"type\":\"TEXT\"},\"updates\":\"\",\"user_id\":\"88888\"},\"bot_id\":\"58846\",\"version\":\"2.0\"}"
        # post_data = bytes(post_data, encoding='utf-8')
        # request = urllib.request.Request(url, post_data)
        # request.add_header('Content-Type', 'application/json')
        # response = urllib.request.urlopen(request)
        # content = response.read()
        # access_token = getAccess()
        url = 'https://aip.baidubce.com/rpc/2.0/unit/bot/chat?access_token=' + access_token
        post_data = {
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
        if content:
            result = str(content, 'utf-8')
            jdata = json.loads(result)
            # jdata = json.loads(res)
            # print(type(jdata))
            bot_session = jdata['result']['bot_session']
            bots = json.loads(bot_session)
            session = bots['session_id']
            # print('session: '+session)
            say = jdata['result']['response']['action_list'][0]['say']
            type1 = jdata['result']['response']['action_list'][0]['type']
            # print(type1)
            if type1 == 'satisfy':
                intent = jdata['result']['response']['schema']['intent']
                locname = jdata['result']['response']['schema']['slots'][0]['normalized_word'][-3:]
                time = jdata['result']['response']['schema']['slots'][1]['normalized_word']
                weather = jdata['result']['response']['schema']['slots'][2]['normalized_word']

                # print('bot_session: ' + bot_session)
                print('say: ' + say)
                print('type1: ' + type1)
                print('intent: '+intent)
                print('locname: '+locname)
                print('time: '+time)
                print('weather: '+weather)

                result = intent+'||'+locname+'||'+time+'||'+weather
                return result, 1, bot_session
            if type1 == 'clarify':
                why = say[-2:]
                if why == '时间':
                    intent = jdata['result']['response']['schema']['intent']
                    locname = jdata['result']['response']['schema']['slots'][0]['normalized_word'][-3:]
                    weather = jdata['result']['response']['schema']['slots'][1]['normalized_word']

                    # print('bot_session: ' + bot_session)
                    print(type(bot_session))
                    print('say: ' + say)
                    print('type1: ' + type1)
                    print('intent: '+intent)
                    print('locname: '+locname)
                    # print('time: '+time)
                    print('weather: '+weather)

                    return say, 2, bot_session
                    # return bot_session,say,intent,locname,weather
                if why == '地点':
                    # print(jdata)
                    intent = jdata['result']['response']['schema']['intent']
                    # time = jdata['result']['response']['schema']['slots'][0]['normalized_word']
                    weather = jdata['result']['response']['schema']['slots'][0]['normalized_word']

                    # print('bot_session: ' + bot_session)
                    print('say: ' + say)
                    print('type1: ' + type1)
                    print('intent: '+intent)
                    # print('locname: '+locname)
                    # print('time: '+time)
                    print('weather: '+weather)
                    # return bot_session,say,intent,time,weather
                    return say, 3, bot_session
            if type1 == 'failure':
                print(say)
                result = type1+'||'+say
                return say, 0 , bot_session
                # return bot_session, say

#多轮会话
def getUnitSession2(bot_session,keyword):
    access_token = getAccess()
    if access_token != 0:
        # print(access_token)
        # print(bot_session)
        url = 'https://aip.baidubce.com/rpc/2.0/unit/bot/chat?access_token=' + access_token
        post_data = {
            "bot_session": bot_session,
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

        if content:
            result = str(content, 'utf-8')
            jdata = json.loads(result)
            bot_session = jdata['result']['bot_session']
            say = jdata['result']['response']['action_list'][0]['say']
            type1 = jdata['result']['response']['action_list'][0]['type']
            print(type1)
            if type1 == 'satisfy':
                intent = jdata['result']['response']['schema']['intent']
                locname = jdata['result']['response']['schema']['slots'][0]['normalized_word'][-3:]
                time = jdata['result']['response']['schema']['slots'][1]['normalized_word']
                weather = jdata['result']['response']['schema']['slots'][2]['normalized_word']

                result = intent+'||'+locname+'||'+time+'||'+weather
                return result, 1, bot_session
            if type1 == 'clarify':
                why = say[-2:]
                if why == '时间':
                    intent = jdata['result']['response']['schema']['intent']
                    locname = jdata['result']['response']['schema']['slots'][0]['normalized_word'][-3:]
                    weather = jdata['result']['response']['schema']['slots'][1]['normalized_word']

                    # print('bot_session: ' + bot_session)
                    print('say: ' + say)
                    print('type1: ' + type1)
                    print('intent: '+intent)
                    print('locname: '+locname)
                    # print('time: '+time)
                    print('weather: '+weather)
                    # return bot_session,say,intent,locname,weather
                    return say, 2, bot_session
                if why == '地点':
                    intent = jdata['result']['response']['schema']['intent']
                    time = jdata['result']['response']['schema']['slots'][0]['normalized_word']
                    weather = jdata['result']['response']['schema']['slots'][1]['normalized_word']

                    # print('bot_session: ' + bot_session)
                    print('say: ' + say)
                    print('type1: ' + type1)
                    print('intent: '+intent)
                    # print('locname: '+locname)
                    print('time: '+time)
                    print('weather: '+weather)
                    # return bot_session,say,intent,time,weather
                    return say, 3, bot_session
            if type1 == 'failure':
                print(say)
                result = type1+'||'+say
                return result,0, bot_session
                # return bot_session, say

#处理日期
def getDateTime(time1):
    # %Y-%m-%d为日期格式，其中的-可以用其他代替或者不写，但是要统一，同理后面的时分秒也一样；可以只计算日期，不计算时间。
    today = datetime.date.today()
    times = time1.split('~')
    if len(times) == 2:
        date1 = times[0]
        date2 = times[1]
        date1 = time.strptime(date1, "%Y-%m-%d")
        date2 = time.strptime(date2, "%Y-%m-%d")
        date1 = datetime.datetime(date1[0], date1[1], date1[2])
        date2 = datetime.datetime(date2[0], date2[1], date2[2])

        date3 = today
        date3 = time.strptime(str(date3), "%Y-%m-%d")
        date3 = datetime.datetime(date3[0], date3[1], date3[2])
        start = date1 - date3
        starts = str(start).split(' ')
        startday = int(starts[0])
        days = date2 - date1
        span = str(days).split(' ')
        if len(span) > 1:
            day = int(span[0]) + 1
        else:
            day = 0
        day = str(day) +'||'+str(startday)

    if len(times) == 1:
        date1 = today
        date2 = times[0]
        date1 = time.strptime(str(date1), "%Y-%m-%d")
        date2 = time.strptime(date2, "%Y-%m-%d")
        date1 = datetime.datetime(date1[0], date1[1], date1[2])
        date2 = datetime.datetime(date2[0], date2[1], date2[2])
        days = date2-date1
        span = str(days).split(' ')
        if len(span) > 1:
            day = int(span[0])
        else:
            day = 0
    # print(days)
    # print(span)
    # print(span[0])
    return day

#处理时间
def getHourTime(time):
    times = time.split('|')
    if len(times) == 2:
        date = times[0]
        hour = times[1]
        today = datetime.datetime.today()
        if date == str(today)[0:10]:
            thour = today.hour
            phour = hour[0:2]
            print(phour)
            if int(phour) - thour >= 0:
                return int(phour) - thour
            else:
                return 'error, can\'t find past weather'
        else:
            return 'error, can\'t find future day hour weather'
    elif len(times) == 1:
        hour1 = times[0]
        today = datetime.datetime.today()
        thour = today.hour
        phour = hour1[0:2]
        # phour = phours[0]
        if int(phour) - thour >= 0:
            return int(phour) - thour
        else:
            # print(int(phour) - thour)
            return 'error, can\'t find past weather'
    else:
        return 'Error!'

# def Tals(result,keyword):
#     res = getUnitSession1(keyword)



#得到天气查询结果
def getAnswer(res):
    print('answer:  ')
    print(res)
    data = res.split('||')
    if len(data) == 2:
        say = data[1]
        say = '小A很抱歉，'+say
        return say
    intent = data[0]
    locname = data[1]
    time = data[2]
    weather = data[3]
    print(time)
    if time.find(':') > 0:
        span = getHourTime(time)
        if isinstance(span,int):
            tflag = 'hour'
        else:
            print(span)
            return span
    else:
        dateres = getDateTime(time)
        date = str(dateres).split('||')
        if len(date) == 1:          #单日天气
            start = date[0]
            print(date[0])
            if int(start) == 0:      #只查询今日天气
                tflag = 'now'
                span = 1
            elif int(start) > 0:     #查询未来一日天气
                tflag = 'forec'
                span = 1
            else:
                return 'Error! Can not find past weather!'
        elif len(date) == 2:        #查询未来一段时间天气
            span = date[0]
            start = date[1]
            if int(span) == 0:      #查询未来一天
                tflag = 'now'
            if int(span) > 0:       #查询未来一段日子
                tflag = 'forec'
        else:
            return 'Error! Can not find past weather!'

    if tflag == 'hour':
        if weather == '天气':
            intt = 'wea'
            res = gw.getHourWeather(locname, span, 1)
            answer = gw.getHourAnswer(res, intt)
            # print(answer)
        elif weather == '温度':
            intt = 'tmp'
            res = gw.getHourWeather(locname, span, 1)
            answer = gw.getHourAnswer(res, intt)
            # print(answer)
        elif weather == '风':
            intt = 'wind'
            res = gw.getHourWeather(locname, span, 1)
            answer = gw.getHourAnswer(res, intt)
            # print(answer)
        else:
            intt = 'wea'
            res = gw.getHourWeather(locname, span, 1)
            answer = gw.getHourAnswer(res, intt)
            # print(answer)

    if tflag == 'now':
        if weather == '天气':
            intt = 'wea'
        elif weather == '温度':
            intt = 'tmp'
        elif weather == '风':
            intt = 'wind'

        elif weather == '空气质量':
            intt = ''
            res = gw.getAir(locname)
            answer = gw.getAirAnswer(res)
            # print(answer)

        elif weather == '污染':
            intt = 'air'
        elif weather == '舒适':
            intt = 'comfort'
        elif weather == '约会':
            intt = 'dating'
        elif weather == '穿衣':
            intt = 'dressing'
        elif weather == '感冒':
            intt = 'flu'
        elif weather == '运动':
            intt = 'sport'
        elif weather == '防晒':
            intt = 'sunscreen'
        elif weather == '交通':
            intt  = 'traffic'
        elif weather == '旅游':
            intt = 'travel'
        elif weather == '雨伞':
            intt = 'umbrella'
        elif weather == '紫外线':
            intt = 'uv'
        elif weather == '洗车':
            intt = 'car_washing'
        else:
            intt = 'wea'

        if (intt == 'wea') or (intt == 'tmp') or (intt == 'wind'):
            res = gw.getNowWeather(locname)
            answer = gw.getNowAnswer(res, intt)
            # print(answer)
        elif intt == 'air' or intt == 'sport' or intt == 'travel' or intt == 'traffic' or intt == 'comfort' or intt == 'dating' or intt == 'flu' or intt == 'dressing' or intt == 'sunscreen' or intt == 'umbrella' or intt == 'car_washing' or intt == 'uv':
            res = gw.getLifeStyle(locname)
            answer = gw.getLifeStyleAnswer(res, intt)
            # print(answer)

    if tflag == 'forec':
        if weather == '天气':
            intt = 'wea'
        elif weather == '温度':
            intt = 'tmp'
        elif weather == '下雨':
            intt = 'rain'
        elif weather == '风':
            intt = 'wind'
        elif weather == '空气':
            res = gw.getForcAir(locname, span)
            answer = gw.getForcAirAnswer(res)
            # print(answer)
        else:
            intt = 'wea'

        if intt == 'wea' or intt == 'tmp' or intt == 'rain' or intt == 'wind':
            res = gw.getForcWeather(locname,start,span)
            answer = gw.getForcAnswer(res, intt)
            # print(answer)
    return answer

def getLocation(uip):
    url = "http://ip.taobao.com/service/getIpInfo.php?ip="+uip
    data = urllib.request.urlopen(url).read()
    print(type(data))
    z_data = data.decode('UTF-8')
    jdata = json.loads(z_data)
    # print(jdata)
    # print(type(jdata))
    loction = jdata['data']['city']
    region = jdata['data']['region']
    print(loction)
    print(region)
    if region == 'XX':
        return 0
    else:
        return loction
def getRecv(msg, state, bots,uip):
    mesg = json.loads(msg)
    # uip = '39.107.119.70'
    location = getLocation(uip)
    print(str(location))
    print(type(mesg))
    data = mesg.get('send_msg')
    if state == 1:
        result, state1, bot_session = getUnitSession1(data)
        if state1 == 3 and location != 0:
            data1 = data+str(location)
            print(data1)
            result,state1,bot_session = getUnitSession1(data1)
    elif state == 2 or state == 3:
        result, state1, bot_session = getUnitSession2(bots, data)
    elif state == 0:
        result, state1, bot_session = getUnitSession1(data)
    print('session time: ')
    print(state1)
    if state1 == 1:
        answer = getAnswer(result)
    else:
        answer = result

    return answer, state1, bot_session

if __name__ == '__main__':
    # result,state,bots = getUnitSession1(sys.argv[1])
    # answer = getAnswer(result)
    # print(answer)
    loc = getLocation(sys.argv[1])
    print(loc)