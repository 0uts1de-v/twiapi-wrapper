import config
import json


def timeline(count):
    twitter = config.twitter
    
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json" #タイムライン取得エンドポイント

    params ={"count" : count}
    
    res = twitter.get(url, params = params)

    if res.status_code != 200:
        print("Get timeline failed. : %s" % res.text)
        
    return json.loads(res.text)