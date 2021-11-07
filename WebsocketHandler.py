import hashlib
import base64
import json
import DbHandler
import util

GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"

def createConnection(header):
    key = getKey(header)
    print(key)
    key = key + GUID
    print(key)
    hashed = hashlib.sha1(key.encode()).digest()
    base64_bytes = base64.b64encode(hashed)
    target = base64_bytes.decode("ascii")
    return target

def getKey(header):
    lines = header.split("\r\n")
    key = ""
    for line in lines:
        if "Sec-WebSocket-Key: " in line:
            key = line.split("Sec-WebSocket-Key: ")[1]
    return key

def loop(self):
    user = self.addressToUser[self.client_address[0]]
    try:
        while True:
            print("Socket: ",self.request.client_address[0])
            received_data = self.request.recv(4096).strip()
            parse = frameParser(received_data).decode()
            clientJson = json.loads(parse)
            print(clientJson)
            if clientJson["type"] == "move":
                ### read the json for the move and return the json from the game logic

        
                ###return message is structured like the example below. Can use any key/value though
                #returnMessage = {"type": "move", "name": user, "column": int}
                returnMessage = str(returnMessage).replace("'", '"').replace(" ", "")
                frame = frameCreator(returnMessage.encode())
                #sends back to initial sender
                self.request.sendall(frame)

                #other player = recipient. should be sent in the clientJson
                self.userToAddress[recipient].sendall(frame)
            if clientJson["type"] == "invite":
                player1 = user
                player2 = clientJson["name"]
                self.games = self.games.append((player1,player2))
                returnMessage = {"type": "invite"}
                returnMessage = str(returnMessage).replace("'", '"').replace(" ", "")
                frame = frameCreator(returnMessage.encode())

                self.userToAddress[player1].sendall(frame)
                self.userToAddress[player2].sendall(frame)
    except:
        del self.userToAddress[user]
        pass

def frameParser(data):
    FIN = data[0] & 0b10000000
    opCode = data[0] & 0b00001111
    maskCode = data[1] & 0b10000000
    len1 = data[1] & 0b01111111
    length = 0
    nextByte = 0
    if len1 < 126:
        length = len1
        nextByte = 2
    elif len1 == 126:
        length = int.from_bytes(bytes(data[2:4]), "big")
        nextByte = 4
    elif len1 == 127:
        length = int.from_bytes(bytes(data[2:10]), "big")
        nextByte = 10


    if maskCode != 0:
        mask = data[nextByte:nextByte+4]
        nextByte += 4
        payload = data[nextByte:nextByte+length]
        payload = XOR(mask,payload)
    else:
        payload = data[nextByte:nextByte+length]
    return payload

def XOR(mask, payload):
    output = []
    for i in range(len(payload)):
        byte = payload[i]
        output.append(byte ^ mask[i % 4])
    return bytearray(output)

def frameCreator(data):
    output = [0b10000001]
    len1 = len(data)
    if len1 < 126:
        output.append(len1)
    elif 126 <= len1 < 65536:
        output.append(126)
        len1 = len1.to_bytes(2, "big")
        for byte in len1:
            output.append(byte)
    else:
        output.append(127)
        len1 = len1.to_bytes(8, "big")
        for byte in len1:
            output.append(byte)
    for byte in data:
        output.append(byte)
    return bytearray(output)