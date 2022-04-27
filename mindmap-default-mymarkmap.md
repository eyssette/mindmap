# myMarkmap

## Un outil libre<br> et gratuit

### <span class="ml-2">[Sources](https://github.com/eyssette/myMarkmap/) sur Github</span>
### _Auteur_ : [Cédric Eyssette](https://eyssette.github.io/)
### Créé à partir du<br> logiciel [markmap](https://markmap.js.org/)

## Pour faire des<br> cartes mentales

- Clic sur 🖊️ (en haut à gauche)<br>pour **éditer** sa carte mentale. <br>On utilise la syntaxe **Markdown**<br>pour créer des branches
  - `# Titre` <br>pour le niveau 1
  - `## Sous-titre`<br> pour le niveau 2
  - `### Niveau 3`,<br> `#### Niveau 4`<br>… ensuite
  - Ou bien, on fait une liste à puces<br>`- Niveau 3`<br>　`  - Niveau 4`<br>`- Niveau 3`<br>(on ajoute 2 espaces avant <br>pour  passer à un autre niveau)
- Clic sur 👓 pour **cacher** la<br> fenêtre d'édition et **voir** <br>seulement la carte mentale
- Clic sur 💾 pour **enregistrer** <br>la carte au format _svg_
- Clic sur 🔗 pour copier un **lien**<br> de **partage** de la carte mentale<br>dans le presse-papier
- Clic sur les **cercles** à l'intersection<br>des différentes branches pour<br>**afficher ou masquer la suite**

## Usages plus<br> avancés

- On peut utiliser d'autres<br> **balises markdown**
  - `**texte**` : pour mettre en **gras**
  - `_texte_` : pour mettre en _italiques_
  - `[lien](URL)` : pour insérer un [lien](https://eyssette.github.io/)
  - ``` `code` ``` : Pour insérer du `code` 
- On peut utiliser certaines **balises HTML**<br>pour contrôler plus précisément<br>l'affichage de sa carte mentale
  - `<br>` pour forcer le passage à la ligne
  - `<!--fold-->` pour que les sous-branches<br>soient cachées par défaut : il faut cliquer<br>sur le cercle pour afficher la suite<!-- fold-->
    - Cette branche est cachée par défaut !
    - Cette branche aussi !
  - `<img src="URL" style="height:…"/>`<br>pour insérer une image
  - `<span style="...">texte</span>`<br>pour changer le style d'un élément
- On peut utiliser des <br>codes pour les emojis :+1:
- **Raccourcis** clavier
  - `e` pour ouvrir la fenêtre d'édition
  - `Escape` pour la fermer
  - `s` pour sauvegarder la carte au format _svg_
  - `l` pour copier le lien vers la carte
- On peut mettre son texte **sur une forge**<br> et l'afficher avec myMarkmap ainsi :
`https://mymarkmap.vercel.app/#URL`
