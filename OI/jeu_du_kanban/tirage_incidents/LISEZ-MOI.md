# Tirage des incidents, Jeu du Kanban

Page web autonome qui remplace la manipulation des dés et du paquet de cartes incident.
Une équipe, un appareil.

---

## Contenu du dossier

| Fichier | Rôle |
|---|---|
| `index.html` | La page complète. Un seul fichier, aucune dépendance, fonctionne hors connexion une fois chargé. |
| `donnees_cartes.json` | Les 80 cartes extraites de `Cartes incident.pptx`, pour référence et contrôle. La page embarque sa propre copie de ces données. |

---

## Déroulement

1. Chaque table saisit son nom d'équipe et démarre la séance.
2. Au début de chaque heure, la table appuie sur **Lancer le dé**.
3. Un **1** ou un **6** déclenche un incident. Toute autre valeur : la production continue, la table passe à l'heure suivante.
4. En cas d'incident, une carte est tirée au hasard : code, atelier concerné, énoncé, et la table des gravités.
5. La table appuie sur **Lancer le dé de gravité**. La ligne correspondante est surlignée, les autres sont estompées.
6. L'historique de la séance conserve chaque heure, chaque jet et chaque conséquence.

---

## Options au démarrage

**Tirage sans remise** (activé par défaut)
La page simule un vrai paquet de 80 cartes. Une carte tirée ne ressort pas tant que le paquet n'est pas épuisé. Décocher pour un tirage indépendant à chaque fois.

**Afficher le commentaire animateur** (désactivé par défaut)
Chaque carte du diaporama d'origine porte un commentaire qui explique pourquoi le même incident a des conséquences différentes selon le dé. Le guide d'animation CIPE conseille de poser la question aux participants avant de donner la réponse. À laisser décoché si la table joue seule.

---

## Points techniques

- **Correspondance dé / gravité.** Elle n'est pas uniforme d'une carte à l'autre. Certaines cartes découpent 1-2 / 3-4-5 / 6, d'autres 1-2-3 / 4-5 / 6, d'autres 1-2-3-4 / 5-6, et huit cartes n'ont que deux niveaux. Chaque table a été extraite dé par dé depuis les formes vectorielles du fichier `Cartes incident.pptx`, puis vérifiée contre les diapos rendues.
- **Reprise après fermeture.** L'état de la séance est conservé dans le navigateur de l'appareil. Fermer l'onglet ou rafraîchir la page ne perd rien. Le bouton **Réinitialiser la séance** efface tout.
- **Modification du contenu.** Les cartes sont dans la variable `CARTES` au début du bloc `<script>` du fichier `index.html`.

---

## Mise à disposition des équipes

La page est un fichier local. Pour qu'elle soit atteignable depuis les smartphones des stagiaires, il faut la publier. Trois voies possibles :

1. **Hébergement web (GitHub Pages, ou tout hébergement statique).** Une URL, un QR code projeté au tableau, chaque table scanne. C'est la voie la plus simple en séance.
2. **Serveur local sur le poste formateur.** `python -m http.server 8000` dans ce dossier, puis les téléphones ouvrent `http://ADRESSE-IP-DU-POSTE:8000`. Dépend de la configuration du réseau du site : l'isolation des clients Wi-Fi, fréquente en établissement, bloque cette voie.
3. **Envoi du fichier.** Le fichier est transmis à chaque stagiaire, qui l'ouvre depuis son gestionnaire de fichiers. Fonctionne, mais l'ouverture d'un fichier HTML local est peu commode sur téléphone.

---

S. Jaubert, Pôle Formation UIMM Centre-Val de Loire
Cartes incident : Jeu du Kanban, CIPE
