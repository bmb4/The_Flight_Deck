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
    cookies = util.getCookies(request[0])
    if path == "signup":
        return CreateAccount.createaccount(inputs)
    elif path == "login":
        return Login.login(self, inputs)
    elif path == "simple_get_profile":
        input_name = data.decode().split('=')[1]
        if DbHandler.nameExists(input_name):
            content = DbHandler.getUser(input_name).asDict()
            content['stats'] = json.dumps(content['stats'])
        else: content = ''
        content = json.dumps(content)
        return responses.create200(content, "text/plain", len(content))
    elif path == 'verify_users':
        users, content = json.loads(inputs['users']), 'True'
        for name in users:
            if not DbHandler.nameExists(name): content = 'False'
        return responses.create200(content, "text/plain", len(content))
    elif path == 'game_result':
        isDraw, winner, loser = inputs['isDraw'], inputs['winner'], inputs['loser']
        DbHandler.applyGameResults(isDraw, winner, loser)
        return responses.create200('', "text/plain", 0)
    return responses.create404("Content not found.", "text/plain", 18)

def buffer(self, data, contentLen):
    while len(data) < contentLen - 2:
        data += self.request.recv(4096)
    return data