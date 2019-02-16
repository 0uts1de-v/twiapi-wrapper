import config
from requests_oauthlib import OAuth1Session
import json
import base64


def tweet(text, *img):
    if len(img) > 4:
        print("too many images")
        return -1
    
    if type(text) != str:
        text = str(text)
    
    twitter = OAuth1Session(config.CK, config.CS, config.AT, config.ATS)
    
    url = "https://api.twitter.com/1.1/statuses/update.json"
    url_img = "https://upload.twitter.com/1.1/media/upload.json"
    media_id = []
    
    for i in range(len(img)):
        files = {"media" : img[i]}
        res_img = twitter.post(url_img, files = files)
        if res_img.status_code != 200:
            print("Failed to upload image : %s" % res_img.text)
            return -1
        media_id.append(json.loads(res_img.text)["media_id"])
    
    if len(media_id) == 0:
        params = {"status" : text}
    else:
        params = {"status" : text, "media_ids" : ",".join(map(str, media_id))}
    
    res = twitter.post(url, params = params)
    
    if res.status_code != 200:
        print("Failed to post : %s"% res.text)
    