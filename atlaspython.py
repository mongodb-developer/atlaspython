import os
import requests
from requests.auth import HTTPDigestAuth
import pprint

baseurl = "https://cloud.mongodb.com/api/atlas/v1.0/"

response = requests.get(baseurl, auth=HTTPDigestAuth(
    os.environ["ATLAS_USER"], os.environ["ATLAS_USER_KEY"]))

pprint.pprint(response.json())
