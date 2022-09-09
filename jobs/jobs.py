import imp
from django.conf import Settings
from time import time
import requests
import json
import random
from datetime import datetime

timeZone = datetime.now()

def schedule_api():
    print("이야~~~~~~~jobs")