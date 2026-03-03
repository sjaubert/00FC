# **TP : Palettisation-Dépalettisation**


- Nous voulons en permanence 4 palettes : choisir 0 Pour « **Inter-arrival Time** » dans la source des palettes


- Dans les propriétés du StockPalette mettre 4 dans le **Max Content**, puis aller piquer Operator1 pour **Use Transport**


3


- Paramétrer la sourceProduit et le poste1


- L’operator1 chargera les colis sur les palettes en sortie du convoyeur. Cliquer sur l’étiquette en sortie du convoyeur.


Dans ses paramètres choisir Operator1 comme Use Transport


4


- Les propriétés du Combiner sont données ci-dessous :


- Pour le Separator faire attention à l’ordre de sortie des ports


                    - **Port 1 vers la sortie des palettes**

                    - **Port 2 vers le 2** **[ème]** **Processor**


5


  - Dans les propriétés du Separator désigner le 2 [ème] opérateur comme **Use Transport**


**Questions/propositions**


  - Mettre en place des indicateurs statistiques sur les taux d’occupation/charge des processors/operators

  - Est-il envisageable d’avoir un seul opérateur ?

  - Peut-on ajuster les temps de processus afin de fluidifier le flux

  - Quelle serait l'incidence d'augmenter la capacité des stocks à 6 palettes sur l'efficacité opérationnelle et les coûts de stockage ?
Comment cela affecterait-il la gestion des stocks ?

  - Si le temps de process des postes de production varie selon une loi exponentielle de moyenne **10s** que constatez-vous ?

  - Modifiez le modèle afin que les palettes déchargées rejoignent le **StockPalette** (cela nécessitera quelques modifications…)


6


