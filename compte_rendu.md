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

## Exercices Shell

1. Lister tous les objets de type Question : faites une boucle pour afficher les attributs de
chaque question sur une ligne différente. Indice : remarquer que
Question.objects.all() est un itérable sur lequel vous pouvez boucler avec une
simple boucle for
```python
    questions = Question.objects.all()
    
    for q in questions:
        print(q.question_text)
        print(q.pub_date)
   ```
```python
What's up?
2026-11-02 13:55:05+00:00
Quel est votre animal de compagnie préféré ?
2026-09-10 07:21:17+00:00
De quelle couleur est le cheval blanc d'Henri IV ?
2025-05-16 09:23:55+00:00
Comment est votre blanquette ?
2026-10-17 20:11:32+00:00
Combien de tiens valent un tu l'auras ?
2026-01-19 04:48:21+00:00
Que pensez-vous des panda roux ?
2026-10-30 10:03:11+00:00 
``` 
2. Ajoutez un filtre sur la date de publication – portant par ex. sur un de ses composants4
suivants : year, month, day – de vos questions et lister un sous-ensemble de vos
questions suivant les dates que vous avez saisies à l'exercice précédent.

On cherche par exmeple les questions publier avant 2026 sur le mois de mai
```python
questions = Question.objects.filter(pub_date__year__lt=2026, pub_date__month=5)
for q in questions: 
    print(q)
```
```python
De quelle couleur est le cheval blanc d'Henri IV ?
```
3. Trouvez la deuxième question (pour laquelle l'attribut de clé primaire id = 2) de votre base
de données, puis affichez les valeurs de tous ses attributs et tous les choix associés.
```python
q = Question.objects.get(pk=2)
print(q.question_text)
print(q.pub_date)
print(q.choice_set.all())
```
```python
Quel est votre animal de compagnie préféré ?
2026-09-10 07:21:17+00:00
<QuerySet [<Choice: Chien>, <Choice: Chat>, <Choice: Galinette cendrée>]>
```
4. Faites une boucle pour afficher les attributs de chaque question et leurs choix associés.
```python
questions = Question.objects.all()
for q in questions:
     print(q.question_text)
     print(q.pub_date)
     for c in q.choice_set.all():
             print(c.choice_text)
```
```python
What's up?
2026-11-02 13:55:05+00:00
Not much
The sky
Quel est votre animal de compagnie préféré ?
2026-09-10 07:21:17+00:00
Chien
Chat
Galinette cendrée
De quelle couleur est le cheval blanc d'Henri IV ?
2025-05-16 09:23:55+00:00
Blanc
Noir
Je suis Daltonien
Comment est votre blanquette ?
2026-10-17 20:11:32+00:00
Bonne
Super bonne
Super super bonne
Combien de tiens valent un tu l'auras ?
2026-01-19 04:48:21+00:00
1
2
3
Que pensez-vous des panda roux ?
2026-10-30 10:03:11+00:00
Ils sont mignons
Ils sont adorables
Ils sont mignons ET adorables
```
5. Affichez le nombre de choix enregistrés pour chaque question.
```python
questions = Question.objects.all()
for q in questions:            
     print(q.question_text)
     print(q.choice_set.count())
```
```python
What's up?
2
Quel est votre animal de compagnie préféré ?
3
De quelle couleur est le cheval blanc d'Henri IV ?
3
Comment est votre blanquette ?
3
Combien de tiens valent un tu l'auras ?
3
Que pensez-vous des panda roux ?
3
```