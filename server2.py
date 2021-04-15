import socket
import pickle
from client import connectAndSend

HOST = ''       # Endereco IP do Servidor          
PORT = 3001     # Porta que o Servidor esta
            
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

while True :
    con, cliente = tcp.accept()
    print ('Conectado por', cliente)
    while True:
        msg = con.recv(4096)
        arrayRecieved = pickle.loads(msg)
        if not msg: break
        print (cliente)
        print (arrayRecieved)
        break

    print ('Finalizando conexao do cliente...', cliente)
    con.close()
    break