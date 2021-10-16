import util
import responses

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
        content = util.getFile("templates/leaderboard.html)
        return responses.create200(content, "text/html", len(content))        
    elif path == "static":
        content = util.getFile("templates/static/WebsiteCSS.css")
        return responses.create200(content, "text/css", len(content))
    return responses.create404("Content not found.", "text/plain", 18)
