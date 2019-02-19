from requests_oauthlib import OAuth1Session


def set(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    global CK, CS, AT, ATS
    CK = CONSUMER_KEY
    CS = CONSUMER_SECRET
    AT = ACCESS_TOKEN
    ATS = ACCESS_TOKEN_SECRET


def login():
    global twitter
    twitter = OAuth1Session(CK, CS, AT, ATS)