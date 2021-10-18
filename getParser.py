import util
import responses
import DbHandler
import json

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
    elif path == "LandingPage":
        content = util.getFile("templates/Landing Page.html")
        return responses.create200(content, "text/html", len(content))
    elif path == "leaderboard":
        leaders = DbHandler.getLeaders()
        content = util.getFile("templates/leaderboard.html")
        content = content.replace('{{ Wins 1 }}', leaders[0]['wins'])
        content = content.replace('{{ Wins 2 }}', leaders[1]['wins'])
        content = content.replace('{{ Wins 3 }}', leaders[2]['wins'])
        content = content.replace('{{ Username 1 }}', leaders[0]['username'])
        content = content.replace('{{ Username 2 }}', leaders[1]['username'])
        content = content.replace('{{ Username 3 }}', leaders[2]['username'])
        return responses.create200(content, "text/html", len(content))
    elif path == "static":
        content = util.getFile("templates/static/WebsiteCSS.css")
        return responses.create200(content, "text/css", len(content))
    elif path == "ProfilePage":
        content = util.getFile("templates/ProfilePage.html")
        return responses.create200(content, "text/html", len(content))
    elif path == "inSession.php":
        content = util.getFile("inSession.php")
        return responses.create200(content, "application/x-httpd-php", len(content))
    elif path == "profileScript.js":
        content = util.getFile("profileScript.js")
        return responses.create200(content, "text/javascript", len(content))
    elif path == "get_stats":
        print([x for x in DbHandler.db])
        content = json.dumps([x for x in DbHandler.db])
        return responses.create200(content, "application/json", len(content))
    return responses.create404("Content not found.", "text/plain", 18)

