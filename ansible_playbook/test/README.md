Je n'ai malheureusement pas été capable de faire fonctionner le son depuis une
VM (Ubuntu 14.04 64-bit) sous VirtualBox jusque sur mon système (Debian 8.0
Jessie avec PulseAudio).

Quoiqu'il en soit, ce test permet surtout de valider l'installation du
Scrobbler API sur un serveur web autre que Airtime. (Même si, le son étant
cassé, Liquidsoap semble ne pas aller jusqu'à contacter le Scrobbler...)

```bash
# Préparer l'environnement Ansible
source ~/devel/ansible/hacking/env-setup

cd test
# Créer puis provisionner les VMs
vagrant up

# S'il faut reprovisionner (ie. rejouer Ansible)
vagrant provision
```

Ce qui crée 2 VMs : `test-airtime` et `test-scrobbler`.

