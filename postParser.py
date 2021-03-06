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
        input_name = data.decode().split('=')[1]
        print(input_name)
        if DbHandler.nameExists(input_name):
            content = DbHandler.getUser(input_name).asDict()
            content['stats'] = json.dumps(content['stats'])
        else: content = ''
        content = json.dumps(content)
        return responses.create200(content, "text/plain", len(content))
    elif path == 'verify_users':
        users, content = json.loads(data.decode()), 'valid'
        if not DbHandler.nameExists(users[0]) or not DbHandler.nameExists(users[1]) or users[0] == users[1]: content = 'invalid'
        return responses.create200(content, "text/plain", len(content))
    elif path == 'game_result':
        inputs = json.loads(data.decode())
        isDraw, winner, loser = inputs['isDraw'], inputs['winner'], inputs['loser']
        DbHandler.applyGameResults(isDraw, winner, loser)
        if isDraw: content = "IT'S A DRAW"
        else: content = 'Winner is <b>' + winner + "</b> :) <br> Better luck next time <b>" + loser + "</b> :("
        return responses.create200(content, "text/plain", len(content))
    return responses.create404("Content not found.", "text/plain", 18)

def buffer(self, data, contentLen):
    while len(data) < contentLen - 2:
        data += self.request.recv(4096)
    return data