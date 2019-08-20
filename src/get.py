import config
import json


def user_timeline(count = 0, since_id = 0, max_id = 0):
    twitter = config.twitter
    
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json" #タイムライン取得エンドポイント

    params = {}

    if count != 0:
        params["count"] = count

    if since_id != 0:
        params["since_id"] = since_id

    if max_id != 0:
        params["max_id"] = max_id

    if len(params) == 1:
        print("Too few arguments.")
        return -1
    
    res = twitter.get(url, params = params)

    if res.status_code != 200:
        print("Get timeline failed. : %s" % res.text)
        return -1
        
    return json.loads(res.text)


def mentions_timeline(count = 0, since_id = 0, max_id = 0):
    twitter = config.twitter
    
    url = "https://api.twitter.com/1.1/statuses/mentions_timeline.json"

    params = {}

    if count != 0:
        params["count"] = count

    if since_id != 0:
        params["since_id"] = since_id

    if max_id != 0:
        params["max_id"] = max_id

    if len(params) == 0:
        print("Too few arguments.")
        return -1
    
    res = twitter.get(url, params = params)

    if res.status_code != 200:
        print("Get timeline failed. : %s" % res.text)
        return -1
        
    return json.loads(res.text)
