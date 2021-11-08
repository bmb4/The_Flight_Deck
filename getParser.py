import util
import responses
import DbHandler
import WebsocketHandler

authentication_messages = []

def getHandler(self, request):
    path = util.getPath(request[0])
    print(path)
    cookie = util.getCookie(request[0])
    print("Cookie: ", cookie)
    if cookie != "":
        self.lastKnownAddress[self.addressToUser[cookie]] = self.client_address[0]
    if path == "":
        content = util.getFile("templates/homeScreen.html")
        return responses.create200(content, "text/html", len(content))
    elif path == "login":
        content = util.getFile("templates/Login Page.html")
        return responses.create200(content, "text/html", len(content))
    elif path == "landingpage":
        content = util.getFile("templates/Landing Page.html")
        return responses.create200(content, "text/html", len(content))
    elif path == "signup":
         content = util.getFile("templates/CreateAccount.html")
         return responses.create200(content, "text/html", len(content))
    elif path == "tutorial":
        content = util.getFile("templates/Tutorialpage.html")
        return responses.create200(content, "text/html", len(content))        
    elif path == "leaderboard":
        leaders = DbHandler.getLeaders()
        content = util.getFile("templates/leaderboard.html")
        content = content.replace('{{ Wins 1 }}', str(leaders[0][1]))
        content = content.replace('{{ Wins 2 }}', str(leaders[1][1]))
        content = content.replace('{{ Wins 3 }}', str(leaders[2][1]))
        content = content.replace('{{ Username 1 }}', str(leaders[0][0]))
        content = content.replace('{{ Username 2 }}', str(leaders[1][0]))
        content = content.replace('{{ Username 3 }}', str(leaders[2][0]))
        return responses.create200(content, "text/html", str(len(content)))
    elif path == "static":
        content = util.getFile("templates/static/Website.CSS")
        return responses.create200(content, "text/css", len(content))
    elif path == "Profile":
        content = util.getFile("templates/ProfilePage.html")
        return responses.create200(content, "text/html", len(content))
    elif path == "NewGame":
        content = util.getFile("templates/gamePage.html")
        return responses.create200(content, "text/html", len(content))    
    elift path == "fourSeq.js":
        content = util.getFile("templates/fourSeq.js")
        return responses.create200(content, "text/javascript", len(content))
    elif path == "profileScript.js":
        content = util.getFile("profileScript.js")
        return responses.create200(content, "text/javascript", len(content))
    elif path == "websocket":
        accept = WebsocketHandler.createConnection(request[0])
        print(accept)
        self.request.sendall(responses.create101(accept))
        WebsocketHandler.loop(self, cookie)
    elif path == "functions.js":
        file = open("functions.js")
        content = file.read()
        file.close()
        return responses.create200(content, "text/javascript", len(content))
    # elif path == "inSession.php":
    #     content = util.getFile("inSession.php")
    #     return responses.create200(content, "text/html", len(content))
    # elif path == "get_stats":
    #     # content = DbHandler.allUsers()
    #     username = main.addressToUsername[self.client_address[0]]
    #     content = json.dumps(DbHandler.getUser(username).asDict())
    #     return responses.create200(content, "application/json", len(content))
    elif path == 'images':
        image_path = request[0].split("\r\n")[0].split(' ')[1].split('/')[2]
        print(path+'/'+image_path)
        mime = 'image/'+image_path.split('.')[1]
        content = util.getFileBytes(path+'/'+image_path)
        return responses.create200Bytes(content, mime, len(content))
    elif path == "InvitePage":
        content = util.getFile("templates/InvitePage.html")
        addedNames = ""
        for name in self.userToAddress:
            addedNames = addedNames + '<p><button onclick=\'socket.send(JSON.stringify({\"type\": \"invite\", \"name\" : \"' + name + '\"}))\'>' + name + '</button></p>'
        content = content.replace("{{names}}", addedNames)
        return responses.create200(content, "text/html", len(content))
    return responses.create404("Content not found.", "text/plain", 18)

