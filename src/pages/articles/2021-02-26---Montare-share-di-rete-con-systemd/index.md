---
title: 'Montare share di rete con systemd'
date: '2021-02-26'
layout: post
category: "Linux"
tags:
  - 'Linux'
  - 'Systemd'
description: 'Una delle utilità di `systemd` è quella di poter montare dei volumi remoti (per esempio uno share di Samba o un volume di NFS) solo quando lo stack di rete è attivo.'
---

Una delle utilità di `systemd` è quella di poter montare dei volumi remoti (per esempio uno share di `Samba` o un volume di `NFS`) solo quando lo stack di rete è attivo.

Attenzione: il concetto di *stack di rete attivo* è ben spiegato nella [documentazione di systemd](https://www.freedesktop.org/wiki/Software/systemd/NetworkTarget/).

# Il file di mount

`systemd` ci viene in soccorso grazie all'unità `mount`, gestita nello stesso modo, per esempio, di un `service`.

Questo è un esempio di `mount` per uno share di `Samba`:

```ini
[Unit]
Description=Mount media share

[Mount]
What=//192.168.178.120/media
Where=/mnt/media
Type=cifs
Options=iocharset=utf8,file_mode=0644,dir_mode=0755,username=guest,password=guest

[Install]
WantedBy=multi-user.target
After=network-online.target
Wants=network-online.target
```

Basterà creare questo file nella directory `/etc/systemd/system` con esattamente lo stesso nome della directory di mount.

Nel caso riportato, file si dovrà chiamare `mnt-media.mount`.

Dopo aver eseguito il reload di `systemd`:

```bash
$ sudo systemctl daemon-reload
```

Potremo attivare la nostra unità di mount:

```bash
$ sudo systemctl enable mnt-media.mount
Created symlink /etc/systemd/system/multi-user.target.wants/mnt-media.mount → /etc/systemd/system/mnt-media.mount.

$ sudo systemctl start mnt-media.mount
```

Le opzioni di `cifs` sono ben dettagliate nella [documentazione ufficiale](https://linux.die.net/man/8/mount.cifs).

# Utilizzo di fstab

In teoria si potrebbe utilizzare `fstab` per il mount degli share remoti, ma nella mia esperienza questo porta a due problemi:

* mancata integrazione con lo stack di rete: è molto complesso gestire punti di mount che dipendono dalla connessione di rete
* `x-systemd.automount`, con questa opzione `systemd` genererà automaticamente una unità di `automount` per ogni riga di `fstab` su cui è specificata questa opzione. In pratica, trovo questa via più complessa da gestire (es, ricordarsi il punto preciso dove specificare l'opzione).

Fatte queste considerazioni, personalmente, preferisco la via più esplicita di creare delle unit dedicate e lasciar fare tutto a `systemd`.
