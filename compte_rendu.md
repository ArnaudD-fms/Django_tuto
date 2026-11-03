# Compte-rendu tutoriel Django

## Interface admin

+ Voyez-vous tous les attributs de vos classes ?

Les attributs des classes sont visibles, de plus différents typs de champs du modèle correspondent au composant graphique d'entrée HTML approprié.
Ainsi, l'attribut date par exemple, permet d'avoir dans l'interface d'administration un raccourci vers un calendrier.

+ Pouvez-vous filtrer vos données suivants tous les attributs ?

Non en l'état il n'est pas possible de filter les données par attributs

+ Pouvez-vous trier vos données suivants tous les attributs ?

Non, on peut uniquement voir toutes les données d'un modèle

+ Pouvez-vous chercher un contenu parmi tous les champs ?

Non, il n'est pas non plus possible de trouver un contenu spécifique présent dans un champ

### Quelles modifications apporter pour répondre positivement aux questions ci-dessus ?

Avec l'ajout de ModelAdmin et des 4 options suivantes : **lisy_display**, **list_filter**, **ordering** et **search_fields**, il est maintenant
possible de filtrer, trier et faire une recherche parmi tous les champs.

## Création d'un nouvel utilisateur

Si l'on créer un utilisateur sans lui octroyer de droits particuliers, il ne pourra pas se connecter à la page d'administration.

En ajoutant le statut "équipe" à l'utilisateur, il peut maintenant se connecter à la page d'administration. (Cependant il ne peut toujours pas y effectuer d'action tant qu'on ne lui attribue pas spécifiquement des droits)

Pour désactiver le compte d'un utilisateur sans le supprimer, il suffit de décocher la case "Actif". 
Cela permet de garder toutes les informations d'un compte et de pouvoir le réactiver au besoin sans avoir à le supprimer puis le recréer.