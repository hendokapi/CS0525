import socket

target = input("IP da scansionare: ")
portrange = input("Range delle porte (es 20-100): ")

lowport = int(portrange.split('-')[0])  # ['20', '100'] -> 20
highport = int(portrange.split('-')[1]) # ['20', '100'] -> 100

print(f"Scansionando l'IP {target} da porta {lowport} a porta {highport}")

for port in range(lowport, highport + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if status == 0:
        print(f"Porta {port}: APERTA")
    else:
        print(f"Porta {port}: CHIUSA")
    s.close()