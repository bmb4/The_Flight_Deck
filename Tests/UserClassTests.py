import unittest
import User

class UserClassTests(unittest.TestCase):

    def testNewUser(self):
        newUser = User.User("testName", "testPassword")
        self.assertTrue(newUser.username, "testName")
        self.assertTrue(newUser.password, "testPassword")
        self.assertTrue(newUser.stats, {"Games Played": 0, "Wins": 0, "Losses": 0, "Draws": 0})

    def testUpdateStats(self):
        newUser = User.User("testName", "testPassword")
        self.assertTrue(newUser.stats, {"Games Played": 0, "Wins": 0, "Losses": 0, "Draws": 0})
        newUser.updateStats("Wins", 5)
        self.assertTrue(newUser.stats, {"Games Played": 0, "Wins": 5, "Losses": 0, "Draws": 0})
        newUser.updateStats("Draws", 13)
        self.assertTrue(newUser.stats, {"Games Played": 0, "Wins": 5, "Losses": 0, "Draws": 13})

    def testAsDict(self):
        newUser = User.User("testName", "testPassword")
        self.assertTrue(newUser.asDict(), {"username":"testName","password":"testPassword","stats":{"Games Played": 0, "Wins": 0, "Losses": 0, "Draws": 0}})

