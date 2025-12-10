# Metasploitable 2

Sito ufficiale: [Metasploitable 2 Documentation](https://docs.rapid7.com/metasploit/metasploitable-2/)

## Login

```
user: msfadmin
pass: msfadmin
```

Per motivi di sicurezza i sistemi linux non mostrano alcun carattere durante la dicitura della password

Se dopo un po' di tempo di inattività lo schermo diventa nero, dare invio per riattivarlo.

## Cambiare lingua della tastiera

```
sudo loadkeys it
```

## Controllare le configurazioni di rete

Comando moderno:

```
ip a
```

oppure (comando più vecchio):

```
ifconfig
```

## Riavvio

```
sudo reboot
```

## Spegnimento

```
sudo poweroff
```

## Configurazioni di rete

```
sudo nano /etc/network/interfaces
```

contenuto del file:

```
# This file describes the network interfaces available on your system
# and how to activate them. Form more information, see interfaces(5)

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
auto eth0
iface eth0 inet dhcp
```

Per settare un ip statico, commentare l'ultima riga con il simbolo # e poi aggiungere il resto delle configurazioni:

```
auto eth0
# iface eth0 inet dhcp
iface eth0 inet static
address 192.168.50.20
netmask 255.255.255.0
gateway 192.168.50.1
# dns-nameservers 8.8.8.8 1.1.1.1
```

Per ricaricare le configurazioni di rete (dopo averle modificate ad esempio):

```
sudo /etc/init.d/networking restart
```

controllare con `ip a` se le configurazioni sono state applicate correttamente.

## Accesso tramite ssh da un altro computer

La Metasploitable supporta solo algoritmi obsoleti e ritenuti ormai insicuri, quindi va forzato il loro utilizzo aggiungendo dei flag. Dal terminale dell'altro computer eseguire il comando:

```
ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedAlgorithms=+ssh-rsa msfadmin@<IP_Metasploitable>
```

quindi inserire la password quando richiesto. Esempio:

```
ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedAlgorithms=+ssh-rsa msfadmin@192.168.0.150
```

è possibile anche editare il file `nano ~/.ssh/config` per applicare i flag in maniera permanente aggiungendo questo al file dell'altro dispositivo:

```
Host <IP_Metasploitable>
    HostKeyAlgorithms +ssh-rsa
    PubkeyAcceptedAlgorithms +ssh-rsa
```

con queste configurazioni è possibile accedere con il comando `ssh msfadmin@<IP_Metasploitable>`
