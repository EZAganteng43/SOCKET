import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 55555))
server.listen()
print("Server berjalan dan menunggu koneksi...")

clients = {}
# key = socket client, value = nickname

def broadcast(msg, sender=None):
    for c in clients:
        if c != sender:
            try:
                c.send(msg)
            except:
                c.close()
                del clients[c]

def handle(client):
    name = client.recv(1024).decode()
    clients[client] = name
    print(f"[+] {name} bergabung ke chat.")

    while True:
        try:
            msg = client.recv(1024)
            if not msg:
                break
            print(f"{name} ➜ {msg.decode()}")
            broadcast(msg, client)
        except:
            break

    print(f"[-] {name} keluar dari chat.")
    client.close()
    del clients[client]
    broadcast(f"{name} keluar dari chat.".encode())

while True:
    client, addr = server.accept()
    client.send("NAMA".encode())
    threading.Thread(target=handle, args=(client,)).start()
