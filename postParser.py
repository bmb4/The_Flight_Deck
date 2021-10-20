import responses
import util
import CreateAccount
import Login
import json
import DbHandler

def postHandler(self, request):
    path = util.getPath(request[0])
    print(path)
    contentLen = util.getContentLen(request[0])
    boundary = util.getBoundary(request[0])
    data = buffer(self, request[1], contentLen)
    inputs = util.formParser(data,boundary)
    if path == "signup":
        return CreateAccount.createaccount(inputs)
    elif path == "login":
        return Login.login(inputs)
    elif path == "simple_get_profile":
        input_name = request[1].decode().split('=')[1]
        # if DbHandler.nameExists(input_name):
        #     response = DbHandler.getUser(input_name).asDict()
        # else: response = response = {"username": '', "password": '', "stats": {
        #             "played": 0, "wins": 0, "losses": 0, "draws": 0
        #         }}
        # print('response: ' + response)
        response = {"username": input_name, "password": '123456', "stats": {
            "played": 6, "wins": 1, "losses": 2, "draws": 3
        }}
        response['stats'] = json.dumps(response['stats'])
        return responses.create200(json.dumps(response), "text/plain", len(json.dumps(response)))
    return responses.create404("Content not found.", "text/plain", 18)

def buffer(self, data, contentLen):
    while len(data) < contentLen - 2:
        data += self.request.recv(4096)
    return data