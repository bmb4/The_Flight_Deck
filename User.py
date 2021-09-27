class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.stats = {"Games Played": 0, "Wins": 0, "Losses": 0, "Draws": 0}
        return

    def updateStats(self, stat, newNum):
        self.stats[stat] = newNum

    def asDict(self):
        newDict = {"username": self.username, "password": self.password, "stats": self.stats}
        return newDict