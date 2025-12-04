import http.client

host = input('Inserire IP: ')
port = input('Inserire la porta (default: 80): ')

if port == '':
    port = 80
else:
    port = int(port)

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('GET', '/')
    response = connection.getresponse()
    print(response)
    print('status:', response.status)

    body_bytes = response.read()
    body_string = body_bytes.decode('utf-8', errors='replace')
    print(body_string)

    connection.close()
except ConnectionRefusedError:
    print("Connessione fallita")
