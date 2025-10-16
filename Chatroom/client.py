import socket
import threading

name = input("Masukkan nama: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def terima():
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg == "NAMA":
                client.send(name.encode())
            else:
                print(msg)
        except:
            print("Koneksi terputus.")
            client.close()
            break

def kirim():
    while True:
        try:
            pesan = input("")
            msg = f"{name}: {pesan}"
            client.send(msg.encode())
        except:
            break

threading.Thread(target=terima).start()
threading.Thread(target=kirim).start()
