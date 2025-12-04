import socket

SRV_ADDR = "192.168.0.144"
SRV_PORT = 44446

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # predisponiamo il socket
s.bind((SRV_ADDR, SRV_PORT)) # assegnamo al socket l'ip e la porta
s.listen(1) # mattiamo in ascolto il server
print(f"Server in ascolto alla porta {SRV_PORT}")
# il comando .accept() blocca l'esecuzione fino a quando non riceve
# un pacchetto alla porta sulla quale sta ascoltando
# quando il pacchetto arriva popola la variabile address con 
# le informazioni del dispositivo che si è connesso
# e predispone la variabile connection per rivecere i dati
# che verranno inviati
connection, address = s.accept()
print(f"Siamo stati contattati da {address}")
while True:
    data = connection.recv(20)
    if data == b'exit\n': break
    connection.sendall(b'ricevuto\n')
    # connection.close()
    print(data.decode('UTF-8'))
connection.close()
