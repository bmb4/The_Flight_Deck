class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.stats = {"Games Played": 0, "Wins": 0, "Losses": 0, "Draws": 0}
        self.profile_pic = ''
        return

    def updateStats(self, stat, newNum):
        self.stats[stat] = newNum

    def changeProfilePic(self, filename):
        self.profile_pic = filename

    def asDict(self):
        newDict = {"username": self.username, "password": self.password, "stats": self.stats, "profile_pic": self.profile_pic}
        return newDict