import json
import urllib2

class org_key:

    def __init__(self):
        pass
    @classmethod
    def get_response(cls, key):
        req = urllib2.Request('https://vtestapi.voatz.com/voatz/organizations/orgkey/login')
        req.add_header('Content-Type', 'application/json')
        json_data = \
            {
                "orgKey": key
            }
        response = urllib2.urlopen(req, json.dumps(json_data))
        return response

    @classmethod
    def read_response(cls, response):
        return response.info()["Csrf-Token"], response.info()["Set-Cookie"]

    @classmethod
    def read_url(cls):
        req = urllib2.Request('https://vtestapi.voatz.com/voatz/customers/delegate/create')
        req.add_header('Content-Type', 'application/json')
        req.add_header('Cookie', 'WS=r5eWHAwedAwdA5HV+ejAMIGKbWPMwt+gHsRtYAQD/fw=')
        req.add_header('Csrf-Token', 'PuX+qA5m3b3Ki1hWrHP85O0eYCvMPnz6qELiJNXZdPY=')
        json_data = \
            {
                "firstName": "xyz"
        }
        response = urllib2.urlopen(req, json.dumps(json_data))
        return response

class register_user:

    def __init__(self):
        pass


#response = org_key.get_response(984402)
#csrf, cookie = org_key.read_response(response)
response = org_key.read_url()
print response.read()
