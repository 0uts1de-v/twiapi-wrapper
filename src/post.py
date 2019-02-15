import config
from requests_oauthlib import OAuth1Session
import base64

twitter = OAuth1Session(config.CK, config.CS, config.AT, config.ATS)


def tweet(text, *img):
    if len(img) > 4:
        print("too many images")
        return -1
        
    if type(text) != str:
        text = str(text)
        
    url = "https://api.twitter.com/1.1/statuses/update.json"
    url_img = "https://upload.twitter.com/1.1/media/upload.json"
    
    for i in range(len(img)):
        
    
    params = {"status" : text}
    
    res twitter.post(url, params = params)
    
    if res.status_code != 200:
        print("Failed to post : %d"%res.status_code)
    