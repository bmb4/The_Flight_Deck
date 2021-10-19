import socketserver
import util
import sys
import os
import pymongo

password = os.environ.get('DB_PASSWORD')
port = 5000
# addressToUsername = {}   # client address to username     # COMMENTED OUT FOR LATER USE
# usernameToAddress = {}        # implemented for logging out

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
                received_data = self.request.recv(1024)

                client_id = self.client_address[0] #+ ":" + str(self.client_address[1])
                print(client_id + " is sending data:")

                # if self.request not in self.clientSockets:
                #     print("NEW CLIENT")
                #     self.clientSockets.append(self.request)
                # print(self.clientSockets)
                #Token comment to make a difference in merge
                print("\n\n")
                sys.stdout.flush()
                sys.stderr.flush()

                self.request.sendall(util.httpParser(self, received_data))

if __name__ == '__main__':

    ##print("Hello world")
    ##MongoDbExample.addRandomNumber()
    ##MongoDbExample.showAllNums()
    #DB name correct below? I think so
    client = pymongo.MongoClient("mongodb+srv://bmb4:"+str(password)+"@Four-in-a-Sequence.3v48s.mongodb.net/DB?retryWrites=true&w=majority")
    db = client.test

    db = client["db"]
    test = db["test"]
    ##Get working mongo
    ##test.insert_one({"name":"John"})
    ##user = test.find_one({"name": "John"})
    ##print(user)

    host = "0.0.0.0"
    # host = "localhost"
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    print(port)

    server = socketserver.ThreadingTCPServer((host, port), MyTCPHandler)
    server.serve_forever()

   