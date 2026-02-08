# **1 [ère] Par�e**

Nous avons vu comment créer un flux d’objets dans le modèle 3D.


Nous pouvons faire la même chose d’une façon plus abstraite avec l’ou�l de
flux de processus. L’ou�l Flux de processus vous permet de créer un
organigramme de logique. À l’intérieur de cet organigramme, vous allez
ajouter des _activités_ qui con�ennent des pe�ts morceaux de logique
préprogrammée.

Lors de l’exécu�on d’un modèle de simula�on, des pe�ts cercles verts
appelés _jetons_ se déplaceront à travers les ac�vités de flux de processus,
exécutant la fonc�on logique.










Re�rer la Source1, le Sink1 et la connexion


  - Aller dans le menu « Process Flow » puis « Add a General Process
Flow »










- Cliquer deux fois sur le panneau blanc et choisir l’ac�vité ~~« Inter-~~


~~-~~ ~~L’ac�vité « Inter-Arrival Source » crée de nouveaux jetons selon un~~
intervalle de temps spécifique. Semblable au style d'arrivée « InterArrival Time » de la source standard du modèle 3D, vous pouvez
u�liser un nombre fixe pour définir un intervalle de temps exact entre
les créa�ons de jetons ou vous pouvez u�liser une distribu�on
sta�s�que pour calculer de manière aléatoire le temps entre les
arrivées. Une fois qu'un jeton est créé, il sera libéré pour l'ac�vité
suivante.










  - On va ajouter l’ac�vité « atribuer des é�quetes » (Assign Labels)


~~L'ac�vité Atribuer des é�quetes crée ou modife des é�quetes sur divers~~
objets. Les é�quetes peuvent être u�lisées pour stocker des données
importantes sur divers objets. Vous pouvez atribuer des é�quetes à
n'importe quel objet possédant des é�quetes qui incluent, sans s'y limiter :




- ~~Un jeton entrant~~




- Un jeton parent




- Éléments de flux




- Objets 3D tels qu'un opérateur ou un processeur




- Un fux de processus




- Je définis un nom, par exemple : « Mon_Type »










Ensuite, en guise d’exemple, on va lui définir 3 valeurs différentes
selon les pourcentages suivants 33%, 33% et 34%


- A présent on crée un objet avec « Create Object »










Avec la pipete vous allez chercher l’objet Queue1


  - Si vous lancez « Run », vous verrez des objets arriver dans Queue1


Chaque objet créé a bien une valeur spécifique


  - Décidons de changer le visuel des objets selon le type
Ajoutons l’ac�vité « Change Visual »










- Lancez le modèle








# **2 [ème] Par�e**

  - Pour chaque objet créé nous avons 3 types différents, metons en
place 3 lignes de produc�on.


`o` Produit type 1 passera par les process : « Inspec�on » « Peinture » - « Séchage »

`o` Produit type 2 passera par les process : « Découpe » « Inspec�on » - Polissage »

`o` Produit type 3 passera par les process : « Découpe » « Peinture » - « Séchage » - « Inspec�on »










Commençons par la créa�on des pièces.

Assembler les ac�vités suivantes :


A la Source, on règle les temps d’arrivée et d’inter-arrivée


Dans Assign Labels, on définit le Label « Type » By Percentage de
la façon suivante :










Puis en fonc�on des types on définit où l’envoyer avec Decide :


A présent nous plaçons 3 conteneurs dans notre espace de travail :


Puis à l’intérieur du Process1 nous placerons les Tâches suivantes :








Dans « **Create Object »,** on définit où l’objet se crée et en quelle quan�té










Avec « **Change Visual »**, on lui donne une couleur (pour le suivre plus
facilement), la couleur dépendra de son Type.


A présent on crée la suite de tâches :

Dans **« Create TS »,** on désigne **OP_Type1** comme l’opérateur des objets de
Type1










Dans **Travel**, on indique où doit se rendre l’Op


Avec **Load**, il charge l’objet


Dans **Travel**, on indique la première étape du type1, ici Inspec�on










**Unload,** on décharge l’objet pour Inspec�on


Enfin dans **« Wait for Event »** on précise bien **« On Process Finish »**










On poursuit le process des pièces de type1 :


Pour le conteneur « Inspec�on->Peinture », voici comment on procède :

Dans la Tâche **Travel,** on indique que l’on est au poste Inspec�on










**Load,** se fait comme précédemment


On se déplace avec **Travel** au poste de peinture


On décharge au poste de peinture par **Unload**










Dans **« Wait for Event »** on indique l’objet et l’évènement « On Process
Finish »


On suit la même logique pour **« Pain�ng->Curing »**


Puis **Curing -> StockSortie**










Et on termine le flux des type1 par :


Par des simples copier-coller des conteneurs, on fait de même pour les deux
autres flux. Vous devriez obtenir ce diagramme de flux :










- Vous pouvez à présent, dans le modèle 3D, déplacer les objets afin de
minimiser les déplacements/croisements des opérateurs (méthodes
des chaînons…).

- Metez en place des indicateurs sta�s�ques per�nents.2










