# FMR Airtime

Paramétrages du service de diffusion continue de [Radio FMR](http://radio-fmr.net/).

[Document de travail temporaire](https://lite5.framapad.org/p/FMR-Airtime-Howto)

## Hardware

Un quad-core Intel Core i3 @ 3.07GHz avec 8 Go de RAM est _largement_ suffisant.

La carte son est une [Audiophile
2496](http://www.m-audio.com/products/view/audiophile-2496), « 4-In/4-Out Audio
Card with MIDI and Digital I/O ». Backupée en cas de besoin par le chipset de la
carte mère : modifier la variable `soundcards` pour intervertir les index, et
rejouer le playbook.

## Ubuntu

L'installation d'Ubuntu Server sur la machine se fait automatiquement.

Voir [ubuntu_preseed](ubuntu_preseed).

## Airtime

L'installation et la pré-configuration se font via [Ansible](http://www.ansible.com/).

Voir [ansible_playbook](ansible_playbook).

## Configuration manuelle

Il ne reste normalement plus rien de fondamental à configurer à la main, le système est fonctionnel.

# Problèmes connus

## L'indexation des fichiers est en panne

Si Airtime est incapable d'ajouter de nouveaux fichiers à sa bibliothèque (que
ce soit via Add Media, ou directement déposé dans un Watched Folder) c'est
probablement parce qu'il bute sur un **fichier dont le nom et/ou les métadata
sont mal codés** en Unicode.

On peut s'en rendre compte dans le log
`/var/log/airtime/media-monitor/media-monitor.log` qui montre que le service
n'arrête pas de se relancer et de planter.

- **Résolution 1 (filename)** : renommer le fichier.

Ça peut être fait en masse en installant le paquet convmv, puis avec cette commande :

```bash
# D'abord on fait un tir de test à blanc :
convmv -f iso-8859-15 -t utf8 --qfrom --replace -r /mnt/localdisk/discotheque

# Si le résultat est satisfaisant, on la relance en désactivant le mode test :
convmv --notest -f iso-8859-15 -t utf8 --qfrom --replace -r /mnt/localdisk/discotheque
```

- **Résolution 2 (metadata)** : convertir les méta-données.

En suivant la [procédure
expliquée](http://sourcefabric.booktype.pro/airtime-25-for-broadcasters/preparing-media-for-ingest/)
sur le site d'Airtime.

Nécessite d'installer le paquet `python-mutagen`.

```bash
# D'abord un tir à blanc (debug et preview), pour des fichiers mp3 dont l'id3 est encodé en Windows-1251 :
find /mnt/localdisk/discotheque -name "*.mp3" -print0 | xargs -0 mid3iconv -e CP1251 -d -p

# Si OK, on relance sans mode preview (-p) :
find /mnt/localdisk/discotheque -name "*.mp3" -print0 | xargs -0 mid3iconv -e CP1251 --remove-v1
```

## Développement

Pour toucher à python, vous devrez [lancer un environnement virtuel](https://github.com/kennethreitz/python-guide/blob/master/docs/dev/virtualenvs.rst)

Oui, pour l'instant, c'est un peu le bazar, [on est en train d'arranger ça](http://iamzed.com/2009/05/07/a-primer-on-virtualenv/)

```
source adhoc/bin/activate
```

