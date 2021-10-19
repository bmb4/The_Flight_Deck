import json

import util
import responses
import DbHandler

authentication_messages = []

def postHandler(self, request):
    # DOES NOT HANDLE UTF-8 NOR MULTIPART-FORM DATA
    path = util.getPath(request[0])
    print(path)
    if path == "simple_get_profile":
        input_name = request[1].decode().split('=')[1]
        response = {"username": input_name, "password": '123456', "stats": {
            "played": 6, "wins": 1, "losses": 2, "draws": 3
        }}
        response['stats'] = json.dumps(response['stats'])
        return responses.create200(json.dumps(response), "text/plain", len(json.dumps(response)))
    return responses.create404("Content not found.", "text/plain", 18)

