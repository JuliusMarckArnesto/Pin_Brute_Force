import socket
import time

def main():
    host = "127.0.0.1"
    port = 8888
    path = "/verify"
    method = "POST"
    num = 0
    num_str = f"{num:03d}"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        print(client_socket)
        # client_socket.settimeout(5)
        client_socket.connect((host, port))
        request = (f"{method}{path}  HTTP/1.1\r\n"
                f"Host: {host}:{port} \r\n"
                f"Content-type: application/x-www-form-urlencoded\r\n"
                f"Accept: */*\r\n"
                f"Accept-Encoding:gzip, deflate, br\r\n"
                f"Connection: keep-alive\r\n"
                f"Content-Length:{len(num_str)}\r\n"
                "\r\n"
                f"magicNumber={num:03d}"
                )
        
        for i in range(0, 1000):
            client_socket.sendall(num_str.encode())
            message = client_socket.recv(4092).decode()
            print(">>", message)
            if "ACCESS GRANTED" in message:
                print("pass ok " + str(num))
                break
            else:
                print("try agin")
                num = i
                # time.sleep(1)
        # client_socket.sendall(request.encode())
        # print(client_socket.sendall(request.encode()))
        

        answer = ""
        response = b''
        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            response += data
            return response
        print(response.decode())

        
        # request("POST", body)
            
        
        print(data)

        

        
    client_socket.close()


# def request(method, path, body=None):


#     request = (f"{method} HTTP/1.1\r\n"
#                 f"Host: {host}:{port} \r\n"
#                 f"Content-type: application/x-www-form-urlencoded\r\n"
#                 f"Accept: */*\r\n"
#                 f"Accept-Encoding:gzip, deflate, br\r\n"
#                 f"Connection: close\r\n"
#                 f"Content-Length:{len(body)}\r\n"
#                 "\r\n"
#                 f"{body}"


if __name__ == "__main__":
    main()