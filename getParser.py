import util
import responses
import DbHandler

authentication_messages = []

def getHandler(self, request):
    path = util.getPath(request[0])
    print(path)
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
        content = util.getFile("templates/static/Website.css")
        return responses.create200(content, "text/css", len(content))
    elif path == "Profile":
        content = util.getFile("templates/ProfilePage.html")
        return responses.create200(content, "text/html", len(content))
    elif path == "NewGame":
        content = util.getFile("templates/gamePage.html")
        return responses.create200(content, "text/html", len(content))
    elif path == "fourSeq.js":
        content = util.getFile("fourSeq.js")
        return responses.create200(content, "text/javascript", len(content))
    elif path == "profileScript.js":
        content = util.getFile("profileScript.js")
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
    return responses.create404("Content not found.", "text/plain", 18)

