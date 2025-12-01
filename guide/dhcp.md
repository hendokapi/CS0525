# DHCP

## Router

Nella CLI del router entriamo in modalità `Privileged EXEC Mode`

```
enable
```

entriamo in modalità configurazione `Global Configuration Mode`

```
configure terminal
```

quindi configuriamo le interfacce che non si trovano nella stessa rete del server DHCP (qui supponiamo l'interfaccia Gig0/0/0)

```
interface Gig0/0/0
```

Il terminale ci indicherà che ci troviamo in modalità di configurazione di una interfaccia mostrando nel prompt `(config-if)#`

Ora (se non già fatto dall'interfaccia grafica di Packet Tracer) configuriamo l'ip e la subnet-mask dell'interfaccia:

```
ip address 192.168.1.1 255.255.255.0
```

abilitiamo l'interfaccia (sono disabilitate di default)

```
no shutdown
```

quindi la configuriamo per instradare al server DHCP i pacchetti di broadcast che riceve (server DHCP supposto qui con indirizzo 192.168.20.2)

```
ip helper-address 192.168.20.2
```

Ora salviamo la configurazione affinchè non si perda al riavvio del router, prima usciamo dalla modalità di configurazione e torniamo in modalità `Privileged EXEC Mode` per poter eseguire poi il comando di salvataggio:

```
end
```

Ora possiamo eseguire il comando di salvataggio

```
copy run start
```

che è una abbreviazione di `copy running-config startup-config` e un'alternativa al vecchio comando:
`write memory` che veniva abbreviato anche con `wr mem`

Quindi torniamo nella modalità non privilegiata `User EXEC Mode`

```
exit
```

Per lanciare comandi senza uscire dalla modalità di configurazione si possono precedere con `do`

```
do copy run start
```
