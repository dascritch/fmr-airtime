Utilisation d'Ansible pour installer et préconfigurer Airtime pour FMR.

# Configuration SSH

Il faut que l'opérateur puisse se connecter par SSH avec sa clé privée. Pour cela, il doit d'abord ajouter sa clé publique sur le serveur :

```bash
# Ajouter sa clé publique
ssh-copy-id -i ~/.ssh/id_dsa.pub fmr@airtime
# Pour cette première fois, le mot de passe de l'utilisateur distant est demandé

# Vérifier que l'on peut dorénavant se connecter sans mot de passe :
ssh fmr@airtime
```

**Note** : pour se créer sa paire de clés SSH publique/privée, voir sur [Ubuntu-fr](http://doc.ubuntu-fr.org/ssh#authentification_par_un_systeme_de_cles_publiqueprivee).

# Définition des variables

Vérifier que les fichiers `group_vars/Servers` et `host_vars/airtime.radio-fmr.lan` contiennent bien les valeurs voulues.

# Utilisation

```bash
# Charger l'environnement de travail Ansible
source ~/devel/ansible/hacking/env-setup

# Lancer l'exécution du playbook airtime.yml (sur les machines du groupe "Airtime")
ansible-playbook -i inventory --ask-sudo-pass airtime.yml
# Saisir comme demandé le mot de passe de l'utilisateur distant
```

En cas d'interruption réseau, il suffit de relancer le playbook Ansible (commande `ansible-playbook`) ; cela ne pose aucune problème, son exécution étant idempotente.

# Troubleshooting

```bash
# Pour lister les variables vues par Ansible
ansible -i inventory airtime -m setup
```

