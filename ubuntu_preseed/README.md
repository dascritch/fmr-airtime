Procédure suivie pour installer Ubuntu Server 14.04.1 pour FMR.

# Création de la clé USB

- Télécharger `ubuntu-14.04.1-server-amd64.iso` ;
  - Lien [Bittorrent](http://releases.ubuntu.com/14.04.1/ubuntu-14.04.1-desktop-amd64.iso.torrent) ou [DDL](http://releases.ubuntu.com/14.04.1/ubuntu-14.04.1-server-amd64.iso)
- Créer la clé USB avec `Unetbootin`.

# Préparation du preseed

- Déposer le fichier `fmr-ubuntu.preseed` ci-joint à la racine de la clé USB ;

Pour générer le mot de passe chiffré : `openssl passwd -1`

- Modifier le fichier `syslinux.cfg` pour que sa première option de démarrage,
- après `timeout`, soit :

```
label fmr
menu label Automatiquement installer Ubuntu pour ^FMR
kernel /install/vmlinuz
append initrd=/install/initrd.gz file=/cdrom/fmr-ubuntu.preseed hostname=fmr-airtime auto=true priority=critical vga=788 quiet --
```

**Remarque** : si les disques-dur n'étaient pas dans l'ordre « normal »,
c'est-à-dire :

- si le premier disque `/dev/sda` (qui est normalement dédié au système) est dédié au stockage des sonores ; et
- si c'est le second `/dev/sdb` qui est dédié au système ;

Alors il faudrait modifier les options du fichier `fmr-ubuntu.preseed` :

- `d-i partman-auto/disk string /dev/sdb` ; et
- `d-i grub-installer/bootdev  string /dev/sdb`

# Installation automatique

Il ne reste plus qu'à démarrer la machine, taper des `<F10>` dès le premier
*<bip>* pour pouvoir choisir de démarrer sur la clé USB, et l'installation
va se faire automatiquement.

Si l'installation s'est bien passée, la machine s'éteint toute seule.

Retirer la clé USB et rallumer le serveur : on peut maintenant y installer
**Airtime** via Ansible : voir [ansible_playbook](../ansible_playbook).

