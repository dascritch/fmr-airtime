Utilisation d'Ansible pour installer et préconfigurer Airtime pour FMR.

# Configuration SSH

Il faut que l'opérateur puisse se connecter par SSH avec sa propre clé privée
`~/.ssh/id_dsa.pub` (ou autre). Pour cela, il doit d'abord ajouter sa clé publique à
l'utilisateur `deploy` du serveur `<hostname>` :

```bash
# Ajouter sa clé publique :
ssh-copy-id -i ~/.ssh/id_dsa.pub deploy@<hostname>
# Pour cette première connexion, le mot de passe de l'utilisateur distant est
# demandé.

# Vérifier que l'on peut dorénavant se connecter sans mot de passe :
ssh deploy@<fqdn_airtime> hostname -f
```

**Note** : pour se créer sa paire de clés SSH publique/privée, voir sur
[Ubuntu-fr](http://doc.ubuntu-fr.org/ssh#authentification_par_un_systeme_de_cles_publiqueprivee).

# Récupérer Ansible


```bash
cd ~/devel/
git clone git://github.com/ansible/ansible.git
```

# Playbook Airtime

Récupérer ce playbook :

```bash
cd ~/devel/
git clone git@github.com:dascritch/fmr-airtime.git
cd fmr-airtime/ansible_playbook
```

## Définition des variables

Ajouter `<hostname>` au fichier d'inventaire `inventory`.

Créer le fichier (en se basant sur un déjà présent) `host_vars/<hostname>` et
modifier les variables qu'il contient.

Vérifier éventuellement que les fichiers `Servers` et `Airtime` (sous `
group_vars`) contiennent eux aussi les bonnes valeurs.

Vérifier notamment :

- program_code
- security_file
- airtime_pass_md5
- admin_email

## Utilisation

```bash
# Charger l'environnement de travail Ansible
source ~/devel/ansible/hacking/env-setup

# Lancer l'exécution du playbook :
# - Sur toutes les machines (du groupe "Airtime") :
ansible-playbook --sudo --ask-sudo-pass airtime.yml
# - Sur une seule machine :
ansible-playbook -s -K airtime.yml --limit <hostname>

# Note : saisir comme demandé le mot de passe de l'utilisateur distant (deploy)
```

En cas d'interruption réseau, il suffit de relancer le playbook Ansible
(commande `ansible-playbook`) ; cela ne pose aucune problème, son exécution
étant idempotente.

