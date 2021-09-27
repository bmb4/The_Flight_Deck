import getParser

double_new_line = "\r\n\r\n".encode()
new_line = "\r\n".encode()

def httpParser(self, data):
    split = data.split(double_new_line, 1)
    header = data.split(double_new_line)[0].decode()
    if len(split) == 1:
        body = b''
    else:
        body = split[1]
    request = [header, body]
    requestType = header.split("\r\n")[0].split("/")[0].strip()
    print(requestType)
    if requestType == "GET":
        return getParser.getHandler(self, request)
    elif requestType == "POST":
        return #postParser.postHandler(self, request)
    else:
        print("big oops")

def getPath(header):
    lines = header.split("\r\n")
    path = lines[0].split("/")[1].split(" ")[0].strip()
    return path

def getContentLen(header):
    lines = header.split("\r\n")
    contentLen = 0
    for line in lines:
        if "Content-Length: " in line:
            contentLen = int(line.split("Content-Length: ")[1])
    return contentLen

def getFile(fileName):
    file = open(fileName)
    content = file.read()
    file.close()
    return content

