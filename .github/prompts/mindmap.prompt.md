---
description: "Créer une carte mentale au format myMarkmap à partir d'un thème donné"
name: "mindmap"
argument-hint: "Sur quel thème veux-tu créer une carte mentale ?"
agent: mindmap
---

# Générateur de carte mentale myMarkmap

À partir du thème donné en argument, génère une carte mentale en Markdown, au format myMarkmap.
Par défaut, écris la carte mentale dans le fichier donné en argument, mais si tu n'as pas accès à un fichier ou si l'utilisateur te demande de ne pas le faire, écris la carte mentale dans ta réponse, dans un bloc code prêt à être copié-collé.


## Syntaxe à respecter

- Le titre de niveau 1 (#) doit être utilisé pour le premier niveau de la carte mentale
- Les titres de niveau 2 (##) doivent être utilisés pour les branches principales de la carte mentale
- Pour les niveaux suivants, utilise un titre de niveau supérieur à celui du niveau précédent, saut s'il s'agit du dernier niveau de la branche. Pour le dernier niveau de la branche, utilise un tiret (-) suivi d'un espace pour lister les éléments à retenir.
- Saute une ligne entre chaque branche de la carte mentale pour améliorer la lisibilité.

## Formulation de la carte mentale

- Le contenu des titres de niveau 1 et 2 doit être formulé de manière courte.
- Les autres contenus peuvent être formulés de manière plus longue, mais doivent rester concis et clairs.
- Il faut éviter d'avoir plus de 3 niveaux au total, sauf si c'est vraiment nécessaire.
- Pour chaque niveau, il faut éviter d'avoir plus de 4 éléments, et préférer même avoir 2 ou 3 branches au maximum.

## Exemple de format attendu

```md
# La Révolution française

## Les causes
- Les inégalités sociales
- La crise financière
- Les idées des Lumières

## Les événements clés
- La prise de la Bastille
- La Déclaration des droits de l'homme et du citoyen

## Bilan de la Révolution

### Fin de la monarchie absolue
- Abolition des privilèges
- Mise en place de la République

### Ambivalence de la Révolution
- Progrès social et politique
- Violence et instabilité politique
```

## Options dans le YAML

Par défaut, ajoute au début de la carte un en-tête YAML avec les options suivantes : 

```md
---
theme: nolines
maxWidth: 300
initialExpandLevel: 100
focusOnBranch: false
automaticResize: true
---
```


## Formules mathématiques en Latex
S'il faut insérer des formules mathématiques, on peut utiliser du Latex, avec la syntaxe suivante : 
```md
$$Latex de type block$$

formule en $Latex de type inline$
```

## Parties masquées

Si l'utilisateur le demande, tu peux masquer certaines parties de la carte mentale en utilisant la syntaxe suivante : `{{partie masquée}}`.

```md
# La Révolution française

## Les dates clés
- Prise de la Bastille : {{14 juillet 1789}}
- DDHC : {{26 août 1789}}
```