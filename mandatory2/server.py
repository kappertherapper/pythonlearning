import os
from socket import *
from datetime import datetime

server_port = 6869

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)

print(f"Server is running on port {server_port}..")


while True:
    client_connection, client_address = server_socket.accept()
    print(f"Forbindelse fra {client_address}")
    
    request = client_connection.recv(1024).decode()

    if not request:
        client_connection.close()
        continue

    try:
        message = request.split('\n')
        http = message[0].split()
        method = http[0]
        url = http[1]
        
        if url == '/':
            url = '/index.html'
        
        file = url.lstrip('/')
        
        if os.path.exists(file):
            with open(file, 'rb') as f:
                body = f.read()
            response = "HTTP/1.1 200 OK\r\n"
            status = "200"

        else:
            body = b"<html><body><h1>404 Not Found</h1><p>File not found!</p></body></html>"
            response = "HTTP/1.1 404 Not Found\r\n"
            status = "404"

    except Exception:
        body = b"HTTP/1.1 400 Bad Request\r\n\r\nBad Request"
        response = "HTTP/1.1 400 Bad Request\r\n"
        status = "400"

    response += "Content-Type: text/html\r\n"
    response += f"Content-Length: {len(body)}\r\n"
    response += "Connection: close\r\n\r\n"

    client_connection.sendall(response.encode() + body)
    client_connection.close()


    #########################

    date = datetime.now().strftime("%d/%b-%Y %H:%M:%S")
    log = f'[{date}] - {client_address[0]}, "{message[0].strip()}" {status} {len(body)}\n'
    
    with open("access.log", "a") as logs:
        logs.write(log)
    
    print(f"{file} - Status: {status}")
