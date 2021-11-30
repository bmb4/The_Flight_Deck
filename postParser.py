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
    print(contentLen, boundary)
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
        users, content = json.loads(data.decode()), 'valid'
        if not DbHandler.nameExists(users[0]) or not DbHandler.nameExists(users[1]) or users[0] == users[1]: content = 'invalid'
        return responses.create200(content, "text/plain", len(content))
    elif path == 'game_result':
        username = cookies["name"]
        game = ()
        for g in self.games:
            if username in g:
                game = g
        if game[0] == username:
            inputs = json.loads(data.decode())
            isDraw, winner, loser = inputs['isDraw'], inputs['winner'], inputs['loser']
            DbHandler.applyGameResults(isDraw, winner, loser)
            if isDraw: content = "IT'S A DRAW"
            else: content = 'Winner is <b>' + winner + "</b> :) <br> Better luck next time <b>" + loser + "</b> :("
            return responses.create200(content, "text/plain", len(content))
    elif path == "invite":
        nameDict = json.loads(data.decode())
        username = cookies["name"]
        friend = nameDict["name"]
        self.games.append((username,friend))
        print("POST NEW GAME:", self.games)
        self.lastMoves[(username,friend)] = (-1, username)
        content = "NewGame"
        return responses.create200(content, "text/html", len(content))
    elif path == "moves":
        numberDict = json.loads(data.decode())
        username = cookies["name"]
        column = numberDict["number"]
        game = ()
        for g in self.games:
            if username in g:
                game = g

        if game[0] == username:
            otherPlayer = game[1]
        else:
            otherPlayer = game[0]

        prevMove = self.lastMoves[game]
        if prevMove[1] == username:
            self.lastMoves[game] = (column, otherPlayer)
            print("Just Posted: ", self.lastMoves)
        else:
            print("NOT YOUR TURN")
    return responses.create404("Content not found.", "text/plain", 18)

def buffer(self, data, contentLen):
    while len(data) < contentLen - 2:
        data += self.request.recv(4096)
    return data