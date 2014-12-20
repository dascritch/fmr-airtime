Utilisation d'Ansible pour installer Airtime pour FMR.

# Configuration SSH

Il faut que l'opérateur puisse se connecter par SSH avec sa clé privée. Pour cela, il doit d'abord ajouter sa clé publique sur le serveur :

```bash
ssh-copy-id -i ~/.ssh/id_dsa.pub fmr@airtime
```

# Définition des variables

Vérifier que les fichiers `group_vars/Servers` et `host_vars/airtime.radio-fmr.lan` contiennent bien les valeurs voulues.

# Utilisation

```bash
# Charger l'environnement de travail Ansible
source ~/devel/ansible/hacking/env-setup

# Lancer l'exécution du playbook airtime.yml (sur les machines du groupe "Airtime")
ansible-playbook -i inventory --ask-sudo-pass airtime.yml
```

# Troubleshooting

```bash
# Pour lister les variables vues par Ansible
ansible -i inventory fmr-airtime -m setup
```

