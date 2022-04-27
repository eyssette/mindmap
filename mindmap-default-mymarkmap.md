# myMarkmap

## Un outil libre \\  et gratuit

### <span class="ml-2">[Sources](https://github.com/eyssette/myMarkmap/) sur Github</span>
### _Auteur_ : [Cédric Eyssette](https://eyssette.github.io/)
### Créé à partir du \\  logiciel [markmap](https://markmap.js.org/)

## Pour faire des \\  cartes mentales

- Clic sur 🖊️ (en haut à gauche) \\ pour **éditer** sa carte mentale.  \\ On utilise la syntaxe **Markdown** \\ pour créer des branches
  - `# Titre`  \\ pour le niveau 1
  - `## Sous-titre` \\  pour le niveau 2
  - `### Niveau 3`, \\  `#### Niveau 4` \\ … ensuite
  - Ou bien, on fait une liste à puces \\ `- Niveau 3` \\ 　`  - Niveau 4` \\ `- Niveau 3` \\ (on ajoute 2 espaces avant  \\ pour  passer à un autre niveau)
- Clic sur 👓 pour **cacher** la \\  fenêtre d'édition et **voir**  \\ seulement la carte mentale
- Clic sur 💾 pour **enregistrer**  \\ la carte au format _svg_
- Clic sur 🔗 pour copier un **lien** \\  de **partage** de la carte mentale \\ dans le presse-papier
- Clic sur les **cercles** à l'intersection \\ des différentes branches pour \\ **afficher ou masquer la suite**

## Usages plus \\  avancés<!--fold-->

- On peut utiliser d'autres \\  **balises markdown**
  - `**texte**` : pour mettre en **gras**
  - `_texte_` : pour mettre en _italiques_
  - `[lien](URL)` : pour insérer un [lien](https://eyssette.github.io/)
  - `![](URL)` : pour insérer une image
  - ``` `code` ``` : Pour insérer du `code` 
- On peut utiliser certaines **balises HTML** \\ pour contrôler plus précisément \\ l'affichage de sa carte mentale
  - ` \\ ` pour forcer le passage à la ligne
  - `<!--fold-->` pour que les sous-branches \\ soient cachées par défaut : il faut cliquer \\ sur le cercle pour afficher la suite<!-- fold-->
    - Cette branche est cachée par défaut !
    - Cette branche aussi !
  - `<span style="...">texte</span>` \\ pour changer le style d'un élément
- On peut utiliser \\ **d'autres balises**
  - Des codes pour les emojis :+1:
  - `\\` pour le passage à la ligne
  - `{{partie masquée}}` pour masquer une partie d'un texte
  - `![h-25](URL)` : pour spécifier la hauteur  \\de l'image (de h-25, h-50 … à h-200)
- **Raccourcis** clavier
  - `e` pour ouvrir la fenêtre d'édition
  - `Escape` pour la fermer
  - `s` pour sauvegarder la carte au format _svg_
  - `l` pour copier le lien vers la carte
- On peut mettre son texte **sur une forge** \\  et l'afficher avec myMarkmap ainsi :
`https://mymarkmap.vercel.app/#URL`
