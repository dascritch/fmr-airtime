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

**Remarque** : S'il y avait une petite subtilité de ce genre concernant les disques-durs :

- `/dev/sda` (IDE, 1 To) : est utilisé pour le stockage des sonores ;
- `/dev/sdb` (SATA, 500 Go) : est dédié au système.

Il faudrait modifier les options du fichier preseed :

- `d-i partman-auto/disk string /dev/sdb` ; et
- `d-i grub-installer/bootdev  string /dev/sdb`

# Installation automatique

Il ne reste plus qu'à booter la machine, taper aussitôt `<F10>` pour pouvoir choisir de démarrer sur la clé USB, et l'installation *devrait* se faire complètement automatiquement.

Si l'installation s'est bien passée, la machine s'éteint.

Il ne reste qu'à retirer la clé USB et rallumer le serveur.

On peut maintenant y installer **Airtime** via Ansible : voir [ansible_playbook](../ansible_playbook).

