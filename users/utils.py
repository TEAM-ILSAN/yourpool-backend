import hashlib
import hmac
import base64

from moiza.settings import NOFITICATION_CONFIG

def make_signature(timestamp):
    access_key = NOFITICATION_CONFIG['ACCESS_KEY']
    secret_key = NOFITICATION_CONFIG['SECRET_KEY']
    
    secret_key = bytes(secret_key, 'UTF-8')

    uri = "/sms/v2/services/ncp:sms:kr:292039892832:moiza/messages"

    message = "POST" + " " + uri + "\n" + timestamp + "\n" + access_key
    message = bytes(message + 'UTF-8')
    signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())

    return signingKey
