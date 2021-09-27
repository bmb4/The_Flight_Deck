def create200(content, mime, length):
    response = "HTTP/1.1 200 OK\r\nContent-Type: " + mime + "\r\nContent-Length: " + str(
        length) + "\r\nX-Content-Type-Options: nosniff\r\n\r\n" + content
    return response.encode()

def create404(content, mime, length):
    response = "HTTP/1.1 404 Not Found\r\nContent-Type: " + mime + "\r\nContent-Length: " + str(
        length) + "\r\nX-Content-Type-Options: nosniff\r\n\r\n" + content
    return response.encode()