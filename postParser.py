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
        input_name = request[1].decode()
        print('name is' + input_name)
        if DbHandler.nameExists(input_name):
            content = DbHandler.getUser(input_name).asDict()
            content['stats'] = json.dumps(content['stats'])
            content = json.dumps(content)
        else: content = ''
        return responses.create200(content, "text/plain", len(content))
    return responses.create404("Content not found.", "text/plain", 18)

def buffer(self, data, contentLen):
    while len(data) < contentLen - 2:
        data += self.request.recv(4096)
    return data