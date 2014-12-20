Procédure suivie pour installer Ubuntu Server 14.04.1 pour FMR.

# Création de la clé USB

- Télécharger `ubuntu-14.04.1-server-amd64.iso` ;
  - Liens [Bittorrent](http://releases.ubuntu.com/14.04.1/ubuntu-14.04.1-desktop-amd64.iso.torrent) et [direct](http://releases.ubuntu.com/14.04.1/ubuntu-14.04.1-server-amd64.iso)
- Créer la clé USB avec `Unetbootin`.

# Préparation du preseed

- Déposer le fichier `fmr-airtime-ubuntu.preseed` ci-joint à la racine de la clé USB ;

Pour générer le mot de passe chiffré : `openssl passwd -1`

- Modifier le fichier `syslinux.cfg` pour qu'il contienne une entrée configurée ainsi :

```
label fmr
menu label Installer Ubuntu Server pour ^FMR
kernel /install/vmlinuz
append initrd=/install/initrd.gz file=/cdrom/fmr-airtime-ubuntu.preseed auto=true priority=critical vga=788  quiet --
```

**Attention** : il y a une petite subtilité pour la machine installée en 2014, concernant ses disques-durs :

- `/dev/sda` (IDE, 1 To) : est utilisé pour le stockage des sonores ;
- `/dev/sdb` (SATA, 500 Go) : est dédié au système.

Il a donc fallu modifier les options du fichier preseed :

- `d-i partman-auto/disk string /dev/sdb` ; et
- `d-i grub-installer/bootdev  string /dev/sdb /dev/sda`

# Installation automatique

Il ne reste plus qu'à booter la machine, cliquer `<F10>` pour choisir de démarrer sur la clé USB, et l'installation *devrait* se faire automatiquement.

Si tout s'est bien passé, la machine s'éteint.

Il ne reste qu'à la rallumer et y installer Airtime avec Ansible : voir [ansible_playbook](../ansible_playbook).

