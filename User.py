class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.stats = {"played": 0, "wins": 0, "losses": 0, "draws": 0}
        return

    def updateStats(self, stat, newNum):
        self.stats[stat] = newNum

    def asDict(self):
        newDict = {"username": self.username, "password": self.password, "stats": self.stats}
        return newDict