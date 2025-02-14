# Application de statistiques PYTHON

Réalisation d'un projet d'application de statistique, en groupe de 2

## Objectifs d'amélioration du projet

- Cinqs graphiques (+1 motivé)
- Une application pour gérer les graphiques et selecionner les fichiers à ouvrir
- Export des graphiques en pdf

## Interface graphique

### Page d'accueil de l'interface graphique

Aperçu de la page d'accueil.

![Accueil interface](/page_accueil_interface_graphique.png)

### Aperçus de la page d'un des graphiques

Il est possible de modifier sur le graphiques:

- Les titres
- Les couleurs
- et certains aspects propres aux graphiques

![Graphique interface](/page_graphique_interface_graphique.png)

## Fonctionnement du projet

### Arborescence du Projet

Ce projet contient plusieurs dossiers :

- graphiques (ce dossier contient les scripts de réalisation des graphs + l'ouverture du fichier + la création de pdf)
  - img (ce dossier est à l'intérieur du dossier img et contient les images par défaut et les images générées par l'application graphique)
- pages (ce dossier contient toutes les pages de l'interface graphique)
- pdf (le dossier où les pdf sont envoyés lorsqu'ils sont créés)
- racine (elle contient les fichiers de données)

### Ouverture de l'interface graphique

Pour ouvrir l'interface graphique, il faut entrer la commande suivante dans l'invite de commande

```bash
python3 index.py
```

