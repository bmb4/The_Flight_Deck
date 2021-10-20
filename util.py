import getParser
import postParser

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
        return postParser.postHandler(self, request)
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

def getFileBytes(fileName):
    file = open(fileName, 'rb')
    content = file.read()
    file.close()
    return content

def getBoundary(header):
    lines = header.split("\r\n")
    boundary = ""
    for line in lines:
        if "boundary=" in line:
            boundary = line.split("boundary=")[1].strip()
    return boundary

def formParser(data, boundary):
    print(data)
    dictionary = {}
    parts = data.split(("--" + boundary).encode())
    print(parts)
    try:

        parts = parts[0].split("&".encode())
        for part in parts:
            split = part.split("=".encode())
            dictionary[split[0].decode()] = split[1].decode()
        print(dictionary)
        return dictionary
    except:

        parts = parts[0].split("+".encode())
        for part in parts[1:-1]:
            split = part.split(double_new_line)
            if "filename".encode() in split[0]:
                name = findFilename(split[0])
            else:
                name = split[0].decode().split("name=")[1].strip("\r\n").replace('"','')
            data = split[1].strip(new_line)
            dictionary[name] = data.decode()

        print(dictionary)
        return dictionary

def findFilename(bytestring):
    decoded_bytes = bytestring.decode()
    index_of_filename = decoded_bytes.index('; filename=')
    updated_bytes = decoded_bytes[index_of_filename:]
    string = ""
    for char in updated_bytes:
        if char == '\r':
            break
        else:
            string += char
    index_of_quote = string.index('"')
    filename = string[index_of_quote+1:len(string)-1]
    print(filename)
    return filename
