#encoding:UTF-8
import urllib
import urllib.request
import  sys
import json

def getNowWeather(loc):
# 数据字典
    data = {}
    data['location'] = loc
    data['key'] = 'SKAv6x_if4JwoaNBv'
    url_values = urllib.parse.urlencode(data)

    url = "https://api.seniverse.com/v3/weather/now.json?"
    full_url = url + url_values

    data = urllib.request.urlopen(full_url).read()
    # print(type(data))
    z_data = data.decode('UTF-8')
    jdata = json.loads(z_data)
    return jdata

def getNowAnswer(res,intent):
    locname = res['results'][0]['location']['name']          #地点名称
    time = res['results'][0]['last_update']                  #时间
    code = res['results'][0]['now']['code']                  #天气代码
    fl = res['results'][0]['now']['feels_like']                   #体感温度
    tmp = res['results'][0]['now']['temperature']                     #温度
    wea_txt = res['results'][0]['now']['text']            #天气描述
    wind_deg = res['results'][0]['now']['wind_direction_degree']           #风向360度
    wind_dir = res['results'][0]['now']['wind_direction']           #风向
    wind_sc = res['results'][0]['now']['wind_scale']            #风力
    wind_spd = res['results'][0]['now']['wind_speed']           #风速
    hum = res['results'][0]['now']['humidity']                     #湿度
    pres = res['results'][0]['now']['pressure']                   #大气压强
    vis = res['results'][0]['now']['visibility']                    #能见度
    cloud = res['results'][0]['now']['clouds']                 #云量

    if intent == 'wea':                     #询问天气、气候
        data = '小A为您播报天气：'+locname+'现在'+',天气：'+wea_txt+',体感温度；'+fl+'度，温度：'+tmp+'度，风向：'+wind_dir+\
               '，风速：'+wind_spd+'千米每小时，湿度：'+hum+',能见度：'+vis+'千米'
        # print(data)
        return data

    if intent == 'tmp':
        data = '小A为您播报天气：'+locname+'现在'+'温度：'+tmp+'度'
        # print(data)
        return data

    if intent == 'wind':
        data = '小A为您播报天气：'+locname+'现在'+'风向：'+wind_dir+',风力：'+wind_sc+'级,风速：'+wind_spd+'千米每小时'
        # print(data)
        return data

    if intent == 'hum':
        data = '小A为您播报天气：'+locname+'现在'+'湿度：'+hum
        # print(data)
        return data


def getForcWeather(loc,start, days):
    # 数据字典
    data = {}
    data['location'] = loc
    data['key'] = 'SKAv6x_if4JwoaNBv'
    data['start'] = start
    data['days'] = days

    url_values = urllib.parse.urlencode(data)

    url = "https://api.seniverse.com/v3/weather/daily.json?"
    full_url = url + url_values

    data = urllib.request.urlopen(full_url).read()
    # print(type(data))
    z_data = data.decode('UTF-8')
    jdata = json.loads(z_data)
    # print(jdata['results'][0]['daily'][2]['date'])
    # print(type(jdata))
    # print(len(jdata['results'][0]['daily']))
    return jdata

def getForcAnswer(res, intent):
    number = len(res['results'][0]['daily'])
    locname = res['results'][0]['location']['name']  # 地点名称

    if intent == 'wea':
        data = '小A为您播报天气:'+locname
        for i in range(number):
            time = res['results'][0]['daily'][i]['date']                    #时间
            text_day = res['results'][0]['daily'][i]['text_day']            #白天天气描述
            code_day = res['results'][0]['daily'][i]['code_day']            #天气代码
            text_night = res['results'][0]['daily'][i]['text_night']        #晚上天气描述
            code_night = res['results'][0]['daily'][i]['code_night']        #晚上天气代码
            high = res['results'][0]['daily'][i]['high']                    #当天最高气温
            low = res['results'][0]['daily'][i]['low']                      #最低气温
            precip = res['results'][0]['daily'][i]['precip']                #降水概率
            wind_direction = res['results'][0]['daily'][i]['wind_direction']       #风向文字
            wind_speed = res['results'][0]['daily'][i]['wind_speed']        #风速
            wind_scale = res['results'][0]['daily'][i]['wind_scale']        #风力等级

            data = data + time+'白天天气'+text_day+'，晚上天气'+text_night+',最高气温'+high+'度，最低气温：'+low+\
                   '度，风向：'+wind_direction+',风速为：'+wind_speed+'千米每小时，风力为：'+wind_scale+'级；'
        return data

    if intent == 'rain':
        data = '小A为您播报天气:'+locname
        for i in range(number):
            time = res['results'][0]['daily'][i]['date']                    #时间
            text_day = res['results'][0]['daily'][i]['text_day']            #白天天气描述
            code_day = res['results'][0]['daily'][i]['code_day']            #天气代码
            text_night = res['results'][0]['daily'][i]['text_night']        #晚上天气描述
            code_night = res['results'][0]['daily'][i]['code_night']        #晚上天气代码
            high = res['results'][0]['daily'][i]['high']                    #当天最高气温
            low = res['results'][0]['daily'][i]['low']                      #最低气温
            precip = res['results'][0]['daily'][i]['precip']                #降水概率


            data = data+time+'白天天气'+text_day+'，晚上天气'+text_night+'; '

        return data

    if intent == 'tmp':
        data = '小A为您播报天气:'+locname
        for i in range(number):
            time = res['results'][0]['daily'][i]['date']                    #时间
            text_day = res['results'][0]['daily'][i]['text_day']            #白天天气描述
            code_day = res['results'][0]['daily'][i]['code_day']            #天气代码
            text_night = res['results'][0]['daily'][i]['text_night']        #晚上天气描述
            code_night = res['results'][0]['daily'][i]['code_night']        #晚上天气代码
            high = res['results'][0]['daily'][i]['high']                    #当天最高气温
            low = res['results'][0]['daily'][i]['low']                      #最低气温
            precip = res['results'][0]['daily'][i]['precip']                #降水概率
            wind_direction = res['results'][0]['daily'][i]['wind_direction']       #风向文字
            wind_speed = res['results'][0]['daily'][i]['wind_speed']        #风速
            wind_scale = res['results'][0]['daily'][i]['wind_scale']        #风力等级

            data = data+time+'最高温度为：'+high+'度，最低温度为：'+low+'度; '

        return data

    if intent == 'wind':
        data = '小A为您播报天气:'+locname
        for i in range(number):
            time = res['results'][0]['daily'][i]['date']                    #时间
            wind_direction = res['results'][0]['daily'][i]['wind_direction']       #风向文字
            wind_speed = res['results'][0]['daily'][i]['wind_speed']        #风速
            wind_scale = res['results'][0]['daily'][i]['wind_scale']        #风力等级

            data = data + time+'风向为：'+wind_direction+'，风速为：'+wind_speed+'千米每小时,风力等级为：'+wind_scale+'级； '

        return data


def getHourWeather(loc, start, hours):
    # 数据字典
    data = {}
    data['location'] = loc
    data['key'] = 'SKAv6x_if4JwoaNBv'
    data['start'] = start
    data['hours'] = hours

    url_values = urllib.parse.urlencode(data)

    url = "https://api.seniverse.com/v3/weather/hourly.json?"
    full_url = url + url_values

    data = urllib.request.urlopen(full_url).read()
    # print(type(data))
    z_data = data.decode('UTF-8')
    jdata = json.loads(z_data)
    # print(jdata)
    # print(type(jdata))
    return jdata

def getHourAnswer(res,intent):
    number = len(res['results'][0]['hourly'])
    # print(number)
    locname = res['results'][0]['location']['name']                                 #地点名称

    if intent == 'wea':
        data = '小A为您播报天气:'+locname
        for i in range(number):
            time = res['results'][0]['hourly'][i]['time']                           #时间
            text = res['results'][0]['hourly'][i]['text']                           #天气状况
            code = res['results'][0]['hourly'][i]['code']                           #天气代码
            temp = res['results'][0]['hourly'][i]['temperature']                    #温度
            humidity = res['results'][0]['hourly'][i]['humidity']                   #湿度
            wind_direction = res['results'][0]['hourly'][i]['wind_direction']       #风向
            wind_speed = res['results'][0]['hourly'][i]['wind_speed']               #风速
            data = data +time+'天气：'+text+',温度:'+temp+'度,湿度：'+humidity+',风向为：'+wind_direction+',风速为：'+wind_speed+'千米每小时; '

        return data

    if intent == 'tmp':
        data = '小A为您播报天气:' + locname
        for i in range(number):
            time = res['results'][0]['hourly'][i]['time']  # 时间
            text = res['results'][0]['hourly'][i]['text']  # 天气状况
            code = res['results'][0]['hourly'][i]['code']  # 天气代码
            temp = res['results'][0]['hourly'][i]['temperature']  # 温度
            humidity = res['results'][0]['hourly'][i]['humidity']  # 湿度
            wind_direction = res['results'][0]['hourly'][i]['wind_direction']  # 风向
            wind_speed = res['results'][0]['hourly'][i]['wind_speed']  # 风速
            data = data + time + '天气：' + text + ',温度:' + temp + '度; '

        return data

    if intent == 'wind':
        data = '小A为您播报天气:' + locname
        for i in range(number):
            time = res['results'][0]['hourly'][i]['time']  # 时间
            text = res['results'][0]['hourly'][i]['text']  # 天气状况
            code = res['results'][0]['hourly'][i]['code']  # 天气代码
            temp = res['results'][0]['hourly'][i]['temperature']  # 温度
            humidity = res['results'][0]['hourly'][i]['humidity']  # 湿度
            wind_direction = res['results'][0]['hourly'][i]['wind_direction']  # 风向
            wind_speed = res['results'][0]['hourly'][i]['wind_speed']  # 风速
            data = data + time + '天气：' + text + ',风向为：' + wind_direction + ',风速为：' + wind_speed + '千米每小时; '

        return data


def getAir(loc):
    # 数据字典
    data = {}
    data['location'] = loc
    data['key'] = 'SKAv6x_if4JwoaNBv'

    url_values = urllib.parse.urlencode(data)

    url = " https://api.seniverse.com/v3/air/now.json?"
    full_url = url + url_values

    data = urllib.request.urlopen(full_url).read()
    # print(type(data))
    z_data = data.decode('UTF-8')
    jdata = json.loads(z_data)
    # print(jdata['results'][0]['air']['city']['aqi'])
    return jdata

def getAirAnswer(res):
    locname = res['results'][0]['location']['name']                             #地点
    aqi = res['results'][0]['air']['city']['aqi']                               #空气质量指数
    pm25 = res['results'][0]['air']['city']['pm25']                             #pm2.5颗粒物
    pm10 = res['results'][0]['air']['city']['pm10']                             #PM10颗粒物
    so2 = res['results'][0]['air']['city']['so2']                               #二氧化硫一小时平均值
    no2 = res['results'][0]['air']['city']['no2']                               #二氧化氮一小时平均值
    co = res['results'][0]['air']['city']['co']                                 #一氧化氮一小时平均值
    o3 = res['results'][0]['air']['city']['o3']                                 #臭氧一小时平均值
    primary_pollutant = res['results'][0]['air']['city']['primary_pollutant']   #首要污染物
    quality = res['results'][0]['air']['city']['quality']                       #空气质量

    data = '小A为您播报天气:' + locname+'空气质量为:'+quality+',空气质量指数为:'+aqi+',pm2.5指数为:'+pm25+',pm10指数为:'+pm10

    return data

def getForcAir(loc,days):
    # 数据字典
    data = {}
    data['location'] = loc
    data['key'] = 'SKAv6x_if4JwoaNBv'
    data['days'] = days

    url_values = urllib.parse.urlencode(data)

    url = "https://api.seniverse.com/v3/air/daily.json?"
    full_url = url + url_values

    data = urllib.request.urlopen(full_url).read()
    # print(type(data))
    z_data = data.decode('UTF-8')
    jdata = json.loads(z_data)
    # print(jdata['results'][0]['air']['city']['aqi'])
    return jdata

def getForcAirAnswer(res):
    number = len(res['results'][0]['daily'])
    locname = res['results'][0]['location']['name']
    data = '小A为您播报天气:' + locname

    for i in range(number):
        date = res['results'][0]['daily'][i]['date']        #时间
        aqi = res['results'][0]['daily'][i]['aqi']  # 空气质量指数
        pm25 = res['results'][0]['daily'][i]['pm25']  # pm2.5颗粒物
        pm10 = res['results'][0]['daily'][i]['pm10']  # PM10颗粒物
        so2 = res['results'][0]['daily'][i]['so2']  # 二氧化硫一小时平均值
        no2 = res['results'][0]['daily'][i]['no2']  # 二氧化氮一小时平均值
        co = res['results'][0]['daily'][i]['co']  # 一氧化氮一小时平均值
        o3 = res['results'][0]['daily'][i]['o3']  # 臭氧一小时平均值
        quality = res['results'][0]['daily'][i]['quality']  # 空气质量

        data = data + date + '空气质量为:'+quality+',空气质量指数为:'+aqi+',pm2.5指数为:'+pm25+',pm10指数为:'+pm10+'; '

    return data

def getLifeStyle(loc):
    # 数据字典
    data = {}
    data['location'] = loc
    data['key'] = 'SKAv6x_if4JwoaNBv'

    url_values = urllib.parse.urlencode(data)

    url = "https://api.seniverse.com/v3/life/suggestion.json?"
    full_url = url + url_values

    data = urllib.request.urlopen(full_url).read()
    # print(type(data))
    z_data = data.decode('UTF-8')
    jdata = json.loads(z_data)
    # print(jdata)
    # print(type(jdata))
    return jdata

def getLifeStyleAnswer(res, intent):
    locname = res['results'][0]['location']['name']                    #地点
    air_pollution = res['results'][0]['suggestion']['air_pollution']['details']    #空气污染
    chill = res['results'][0]['suggestion']['chill']['details']                    #寒冷
    comfort = res['results'][0]['suggestion']['comfort']['details']                #舒适
    dating = res['results'][0]['suggestion']['dating']['details']                  #约会
    dressing = res['results'][0]['suggestion']['dressing']['details']              #穿衣
    flu = res['results'][0]['suggestion']['flu']['details']                        #感冒
    sport = res['results'][0]['suggestion']['sport']['details']                    #运动
    sunscreen = res['results'][0]['suggestion']['sunscreen']['details']            #防晒
    traffic = res['results'][0]['suggestion']['traffic']['details']                #交通
    travel = res['results'][0]['suggestion']['travel']['details']                  #旅游
    umbrella= res['results'][0]['suggestion']['umbrella']['details']               #雨伞
    uv = res['results'][0]['suggestion']['uv']['details']                          #紫外线
    car_washing = res['results'][0]['suggestion']['car_washing']['details']        #洗车

    if intent == 'air':
        data = '小A为您播报天气:' + locname + '空气污染:'+air_pollution
        return data
    if intent == 'chill':
        data = '小A为您播报天气:' + locname +chill
        return data
    if intent == 'comfort':
        data = '小A为您播报天气:' + locname + comfort
        return data
    if intent == 'dating':
        data = '小A为您播报天气:' + locname +dating
        return data
    if intent == 'dressing':
        data = '小A为您播报天气:' + locname + dressing
        return data
    if intent == 'flu':
        data = '小A为您播报天气:' + locname + flu
        return data
    if intent == 'sport':
        data = '小A为您播报天气:' + locname + sport
        return data
    if intent == 'sunscreen':
        data = '小A为您播报天气:' + locname + sunscreen
        return data
    if intent == 'traffic':
        data = '小A为您播报天气:' + locname + traffic
        return data
    if intent == 'travel':
        data = '小A为您播报天气:' + locname + travel
        return data
    if intent == 'umbrella':
        data = '小A为您播报天气:' + locname + umbrella
        return data
    if intent == 'uv':
        data = '小A为您播报天气:' + locname + uv
        return data
    if intent == 'car_washing':
        data = '小A为您播报天气:' + locname + car_washing
        return data



# if __name__ == '__main__':
    # loc = sys.argv[1]
    # res = getNowWeather(loc)
    # getNowAnswer(res, sys.argv[2])
    # res = getForcWeather(loc, 1, 8)
    # data = getForcAnswer(res, sys.argv[2])
    # print(data)
    # res = getHourWeather(loc, 7, 10)
    # data = getHourAnswer(res, sys.argv[2])
    # print(data)
    # res = getAir(loc)
    # getAirAnswer(res)
    # res = getForcAir(loc, 5)
    # getForcAirAnswer(res)
    # res = getLifeStyle(loc)
    # data = getLifeStyleAnswer(res, sys.argv[2])
    # print(data)
    # getForeLifeStyle(loc)
    # getNowAir(loc)
