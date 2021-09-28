import socketserver
import util
import sys
#from Examples import MongoDbExample

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
                received_data = self.request.recv(1024)

                client_id = self.client_address[0] #+ ":" + str(self.client_address[1])
                print(client_id + " is sending data:")

                # if self.request not in self.clientSockets:
                #     print("NEW CLIENT")
                #     self.clientSockets.append(self.request)
                # print(self.clientSockets)

                print("\n\n")
                sys.stdout.flush()
                sys.stderr.flush()

                self.request.sendall(util.httpParser(self, received_data))

if __name__ == '__main__':
    ##print("Hello world")
    ##MongoDbExample.addRandomNumber()
    ##MongoDbExample.showAllNums()

    host = "0.0.0.0"
    # host = "localhost"
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    print(port)
    server = socketserver.ThreadingTCPServer((host, port), MyTCPHandler)
    server.serve_forever()