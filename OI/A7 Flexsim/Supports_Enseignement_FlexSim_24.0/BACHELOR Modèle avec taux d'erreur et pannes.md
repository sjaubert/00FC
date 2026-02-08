Les pièces passeront par les processeurs 1 et 2, qui traitent respectivement une côte x et y


Le cahier des charges impose une côte pour x comprise entre 75cm et 85cm, pour y comprise
entre 45cm et 55cm.


Si en sortie du Processor1, x ne respecte pas le CDC, la pièce ira dans le stock Erreur_X, si en
sortie du processor2, y ne respecte pas le CDC la pièce ira dans le stock Erreur_Y.


Nous enregistrerons dans des tableaux différentes informations concernant les côtes x et y au
fur et à mesure de la production.


**Le temps d’ouverture d’une journée va de 8H00 à 17H00.**


  - Par la suite nous introduirons un planning journalier pour les machines et des pannes
sur chaque processeur.

  - L’objectif sera de déterminer le taux de qualité, la disponibilité et le TRS de la ligne.










# **Paramétrage des objets**

La source


Rien de particulier, par exemple :


Stock en entrée On peut éventuellement traiter par Batch de 10


**Processor1**


On commence par définir un Trigger **« On Process Finish »** pour définir la taille en x et la couleur
de l’objet


X suivra une loi Normale de moyenne 0.8 et d’écart-type 0.05


On peut régler le Process Time sur 10, ensuite il faut décider où se rend la pièce en sortie


Si x < 0.75 ou x> 0.85 on envoie la pièce au port 2, port 1 sinon


On procède de même pour le processeur 2


**Processeur 2**


Comme on a déjà défini la côte x, il ne faut plus la modifier, donc on l’impose dans le champ X
Size, et on définit Y comme suivant une loi normale de moyenne 0.5 et d’écart-type 0.05


Si y< 0.45 ou y>0.55 on l’enverra au port 2


Et on décide où envoyer la pièce comme précédemment


## **Création des tables globales**

Dans Toolbox « **Global Tables** » créer 3 tables


Avec pour chacune les colonnes suivantes :


Dès l’entrée dans un des stocks, une des tables précédentes sera renseignée.


On définit un trigger


Faire la même chose avec **Erreur_Y**


Lancer votre modèle et proposer des améliorations (comme, par exemple, sortir les pièces
défectueuses du modèle, changer les Process_Time…)


## **Insertion d’un Planning de travail**

Pour des raisons de commodités, commençons par ajouter des étapes dans le Run Time


Nous passons d’une étape à l’autre avec « Fast Forward »


(ainsi nous contrôlons facilement si le planning est
bien paramétré en nous rendant directement sur des zones de temps, le modèle se relance
simplement par Run)


**Insertion d’un planning**


Dans le Toolbox ajouter une Time Table


Comme membres, mettre les objets
suivants :


On définit une pause de 10h à
10H15, de 15h à 15H15 et une pause
déjeuner


## **Paramétrage de la fiabilité des processeurs**

Dans Toolbox se rendre sur **« MTBF MTTR »**


On choisit les objets qui seront concernés par la loi de fiabilité


Dans Functions, on définit les lois de First Failure Time (heure du premier échec. Un
nombre négatif entraînera l'ignorance du premier échec) et celle de Up Time (Temps de
disponibilité, en général nous mettons la même chose) ici nous prenons une loi
exponentielle de MTBF 1H.


On prendra pour Down Time une loi uniforme entre 5’ et 20’ (attention aux unités !)


# **Indicateurs statistiques**

Ajoutons un Dashboard


En cliquant deux fois de suite sur le panneau du Dashboard, on sélectionne **Output**


Puis on prend **Table** et on sélectionne les objets suivants


On peut aussi sélectionner un processor et aller directement dans le panneau des propriétés,
sélectionner le « pin » en regard de **State**


Choisir **Pin to Dashboard + Pie chart** et bien sûr ajouter les deux processors


Il est utile d’ajouter un collecteur de statistiques dans la barre d’outils. Pour cela aller dans  File

Cette icône doit apparaître :

Cliquer dessus, vous pouvez maintenant ajouter toutes les stats que vous souhaitez !


Voici un exemple de ce qu’on peut obtenir après une journée

## **Questions :**


  - Déterminer les taux de qualité de chaque machine puis de la ligne.

  - Déterminer les taux suivants :

`o` Taux de qualité : Le taux de qualité peut être calculé en divisant le nombre de
pièces conformes par le nombre total de pièces produites.

`o` Disponibilité : La disponibilité peut être évaluée en prenant en compte le temps
de fonctionnement planifié moins les arrêts (pauses, pannes) par rapport au
temps de fonctionnement planifié.

  - Pouvez-vous définir le TRS de la ligne (voir cours)

  - Comment faire en sorte que le processeur2 est un meilleur taux de process ?

  - Comment éviter le surplus de stock en entrée ?


**Remarque :**


Avec l’outil **Reports and Statistics**


Il sera possible de récupérer très facilement de nombreux indicateurs en générant des rapports


