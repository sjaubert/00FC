# Tirage des incidents, Jeu du Kanban

Deux pages web autonomes qui remplacent la manipulation des dés et du paquet de cartes incident, puis rassemblent les résultats des tables en fin de séance.

Une équipe, un appareil.

---

## Contenu du dossier

| Fichier | Rôle |
|---|---|
| `index.html` | La page des équipes. Jet d'ouverture, tirage de carte, jet de gravité, historique. |
| `synthese.html` | La page du formateur. Rassemble les bilans des tables et les compare. |
| `donnees_cartes.json` | Les 80 cartes extraites de `Cartes incident.pptx`, pour référence et contrôle. Les deux pages embarquent leur propre copie de ces données. |
| `Affiche_QR_tirage_incidents.pdf` | Affiche A4 à imprimer ou à projeter, avec le QR code d'accès. |
| `qr_tirage_incidents.png` et `.svg` | Le QR code seul, à insérer dans un diaporama. Le SVG s'agrandit sans perte. |

Aucune des deux pages ne dépend d'Internet une fois chargée, ni d'un compte, ni d'un serveur. Rien n'est envoyé nulle part.

---

## Déroulement d'une séance

### Côté table

1. Chaque table scanne le QR code, saisit son nom d'équipe et démarre.
2. Au début de chaque heure, la table appuie sur **Lancer le dé**.
3. Un **1** ou un **6** déclenche un incident. Toute autre valeur : la production continue, la table passe à l'heure suivante.
4. En cas d'incident, une carte est tirée au hasard : code, atelier concerné, énoncé, table des gravités.
5. La table appuie sur **Lancer le dé de gravité**. La ligne correspondante est surlignée, les autres sont estompées.
6. L'historique de la séance conserve chaque heure, chaque jet et chaque conséquence.

### En fin de séance

7. Chaque table ouvre son historique et appuie sur **Terminer et transmettre le bilan**. Son écran affiche un QR code.
8. Le formateur scanne ce code avec l'appareil photo de son téléphone. La page de synthèse s'ouvre et l'équipe y est ajoutée.
9. Il répète l'opération pour chaque table. Trois scans, trois équipes.

Si un scan échoue, la table peut déplier **Le formateur n'arrive pas à scanner**, copier le code et le transmettre par message. Le formateur le colle dans le champ prévu au bas de la page de synthèse.

---

## Ce que montre la synthèse

- **Vue d'ensemble** : nombre d'équipes, heures jouées, incidents, taux d'incident, répartition par famille (Qualité, Panne, Effectifs, Appros).
- **Heure par heure** : un tableau croisé, une colonne par équipe. Chaque table ayant lancé son propre dé, les incidents ne coïncident pas, et deux tables touchées par la même carte peuvent subir des gravités différentes. C'est le matériau du débriefing.
- **Détail par équipe** : pour chaque incident, l'heure, la carte, l'atelier, les deux dés, la conséquence et l'énoncé de la carte.

La page s'imprime proprement, les boutons disparaissent à l'impression.

---

## Options au démarrage, côté table

**Tirage sans remise** (activé par défaut)
La page simule un vrai paquet de 80 cartes. Une carte tirée ne ressort pas tant que le paquet n'est pas épuisé. Décocher pour un tirage indépendant à chaque fois.

**Afficher le commentaire animateur** (désactivé par défaut)
Chaque carte du diaporama d'origine porte un commentaire qui explique pourquoi le même incident a des conséquences différentes selon le dé. Le guide d'animation CIPE conseille de poser la question aux participants avant de donner la réponse. À laisser décoché si la table joue seule.

---

## Points techniques

**Correspondance dé et gravité.** Elle n'est pas uniforme d'une carte à l'autre. Certaines cartes découpent 1-2 / 3-4-5 / 6, d'autres 1-2-3 / 4-5 / 6, d'autres 1-2-3-4 / 5-6, et huit cartes n'ont que deux niveaux. Chaque table a été extraite dé par dé depuis les formes vectorielles du fichier `Cartes incident.pptx`, puis vérifiée contre les diapos rendues.

**Cloisonnement des équipes.** Il n'y a pas de gestion multi-équipes dans la page des tables. Chaque navigateur a son propre espace de stockage : historique, compteur d'heures et paquet de cartes sont indépendants d'un appareil à l'autre. Ne partagez pas un téléphone entre deux tables, la seconde écraserait l'historique de la première.

**Reprise après fermeture.** L'état est conservé dans le navigateur de l'appareil. Fermer l'onglet ou rafraîchir la page ne perd rien. Le bouton **Réinitialiser la séance** efface tout.

**Le QR code du bilan.** Il contient le bilan lui-même, pas un identifiant renvoyant à un serveur. Rien ne transite par le réseau et la synthèse fonctionne hors connexion. Le générateur de QR est intégré à la page. Il a été validé en comparant ses symboles à ceux d'une bibliothèque de référence, puis en les faisant relire par un décodeur.

**Modification du contenu.** Les cartes sont dans la variable `CARTES`, au début du bloc `<script>` de chaque page.

---

S. Jaubert, Pôle Formation UIMM Centre-Val de Loire
Cartes incident : Jeu du Kanban, CIPE
