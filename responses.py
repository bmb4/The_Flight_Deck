def create200(content, mime, length):
    response = "HTTP/1.1 200 OK\r\nContent-Type: " + mime + "\r\nContent-Length: " + str(
        length) + "\r\nX-Content-Type-Options: nosniff\r\n\r\n" + content
    return response.encode()

def create404(content, mime, length):
    response = "HTTP/1.1 404 Not Found\r\nContent-Type: " + mime + "\r\nContent-Length: " + str(
        length) + "\r\nX-Content-Type-Options: nosniff\r\n\r\n" + content
    return response.encode()

def create301(newPath):
    response = "HTTP/1.1 301 Moved Permanently\r\nLocation: " + newPath + "\r\nContent-Length:0" + \
               "\r\nX-Content-Type-Options: nosniff\r\n\r\n"
    return response.encode()

def create200Bytes(content, mime, length):
    response = b"HTTP/1.1 200 OK\r\nContent-Type: " + mime.encode() + b"\r\nContent-Length: " + str(
        length).encode() + b"\r\nX-Content-Type-Options: nosniff\r\n\r\n" + content
    return response
