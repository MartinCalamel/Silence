# Silence

[![Python Tests](https://github.com/WallabyMt59/Silence/actions/workflows/python-tests.yml/badge.svg)](https://github.com/WallabyMt59/Silence/actions/workflows/python-tests.yml)

<img src="./images/logo.jpg" alt="Description" width="300" style="display: block; margin: auto;">

## Sommaire
* [Sommaire](#sommaire)
* [Objectifs](#objectifs)

## Objectifs
Silence possède un double objectif :
* Créer une messagerie chiffrée avec un système de gestion fiable
* Me permettre d'apprendre les dessous d'un tel système.

## Fonctionnement
Nous allons maintenant détailler le fonctionnement des différents composant du projet.  
### files
Ce composant permet la manipulation de fichier. Il possèdes 4 fonctions principales et une fonction de verification.

#### Fonctions principales
* `read` => permet de lire un fichier.
* `write` => permet décrire dans un fichier en remplaçant le contenu.
* `add` => permet d'ajouter du contenu à la fin du fichier.
* `create_file` => crée un fichier.

#### Fonctions de verification
* `exist_file` => retourne sous la forme d'un booléen si le fichier existe (*essentiel pour les fonction de lecture et d'addition*)

### info
Ce composant permet d'afficher des informations à l'utilisateur tels que les erreurs ou les logs.  
Pour le moment il ne possède qu'une seul fonction `error` permettant d'afficher une erreur en rouge dans la console.

### type
Ce composant permet de verifier le type d'une variable afin de contrôler les paramètre fournis au fonction.  
Il ne possède qu'une seule fonction `check_type` qui effectue cette verification.

### auth_protocol
Ce composant permet d'effectuer une authentification sécurisée avec un identifiant et un mot de passe.  
Le stockage de ces données est également sécurisé avec un hash et un sel.  
Il y a donc deux fonctions principales et des fonctions annexes qui permettent à celles-ci de fonctionner correctement.  
#### Fonctions principales
* `verif_user` => vérifie si l'utilisateur existe et si le mot de passe est bon.
* `new_user` => Ajoute un utilisateur à la base de donnée.

#### Fonctions annexes
