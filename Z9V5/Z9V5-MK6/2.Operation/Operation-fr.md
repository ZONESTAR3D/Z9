
## <a id="choose-language">:globe_with_meridians: Choose language </a>
[![](../../lanpic/EN.png)](./Operation.md)
[![](../../lanpic/ES.png)](./Operation-es.md)
[![](../../lanpic/PT.png)](./Operation-pt.md)
[![](../../lanpic/FR.png)](./Operation-fr.md)
[![](../../lanpic/DE.png)](./Operation-de.md)
[![](../../lanpic/IT.png)](./Operation-it.md)
[![](../../lanpic/RU.png)](./Operation-ru.md)
[![](../../lanpic/JP.png)](./Operation-jp.md)
[![](../../lanpic/KR.png)](./Operation-kr.md)

----
## Guide d'opération
Avant de commencer l'impression, vous devez niveler le lit chaud (ajuster finement la distance entre la buse et la plate-forme d'impression) et charger les filaments dans les extrudeuses et la partie chaude.
## Mise à niveau du lit chaud
#### :warning: Pour une imprimante 3D FDM, la distance entre la buse et le lit chaud est très importante lors de l'impression de la première couche. Si la distance est trop proche, les filaments ne peuvent pas s'écouler hors de la buse, et même endommager la buse et le lit chaud. Si la distance est trop grande, les filaments ne peuvent pas être collés sur le lit chaud, les couches suivantes ne peuvent pas être empilées correctement et entraîner un échec d'impression.
###### [![](https://img.youtube.com/vi/jNf98S0u2VQ/0.jpg)](https://www.youtube.com/watch?v=jNf98S0u2VQ)
- **Étape 1.** Allumez l'imprimante 3D, puis faites ***Prepare>>Auto Home>>Home All*** sur le MENU LCD, attendez que le hotend aille en position HOME.
- **Étape 2.** Serrez les écrous manuels sous le lit pour faire descendre le lit jusqu'à la position la plus basse (Fig. 1).
- **Étape 3.** Faites ***Préparer>> Nivellement du lit>> Point 1*** sur le panneau de commande (Fig 2), la buse ira jusqu'aux coins du lit, desserrez les écrous à main sous le foyer (Fig. 3) et laissez la buse toucher presque le foyer (Fig. 4). Continuez à faire le ***Point 2/3/4*** jusqu'à ce que les 4 coins soient nivelés.
- **Étape 4.** Répétez l'étape 3 et faites 2 à 3 tours, jusqu'à ce que les quatre coins soient à la même hauteur.
![](./Operation/levelbed.png)

----
### Charger les filaments
###### [![](https://img.youtube.com/vi/1rr4dXRxKc4/0.jpg)](https://www.youtube.com/watch?v=1rr4dXRxKc4)
Cette imprimante est équipée de quatre extrudeuses et d'une extrémité chaude de mélange de couleurs 4-IN-1-OUT. Les extrudeuses et le hot end sont reliés par un guide filament (tube PTFE). ***Avant d'imprimer, vous devez charger les 4 filaments dans les extrudeuses et les insérer dans le bas de l'extrémité chaude.***
- **Étape 1.** Faites ***Préparation>>Auto Accueil>>Maison Tout*** sur le panneau de commande, puis faites ***Préparation>>Température>> Préchauffer le PLA***, en attendant que la température de la buse soit atteinte. à 190 ℃ (Fig. 1).
- **Étape 2.** Utilisez une pince diagonale pour couper la tête du filament (Fig. 2), puis appuyez sur la poignée de l'extrudeuse n°1 et insérez le filament, poussez le filament jusqu'à ce que vous puissiez voir le filament dans le PTFE. guide (Fig. 3). Faites tourner l'engrenage de l'extrudeuse n°1 (Fig. 4), observez le filament jusqu'à ce qu'il entre au bas de l'extrémité chaude.
- **Étape 3.** En utilisant la même méthode qu'à l'étape 2 pour charger les filaments dans l'extrudeuse n°2 ~ l'extrudeuse n°4, surveillez les filaments jusqu'à ce qu'ils entrent dans le bas de l'extrémité chaude.
- **Étape 4.** Faites tourner lentement l'engrenage de l'extrudeuse n°1 ~ de l'extrudeuse n°4 un par un et observez la buse jusqu'à ce que vous puissiez voir le filament s'écouler de la buse (Fig. 5).
![](./Operation/loadfilament.png)

----
### Imprimez vos travaux "Hellow World"
#### Imprimer un fichier de test d'une seule couleur
###### [![](https://img.youtube.com/vi/NbVy8NjKt_s/0.jpg)](https://www.youtube.com/watch?v=NbVy8NjKt_s)
- **Étape 1.** Insérez la carte SD dans la prise pour carte SD de l'imprimante (Fig 1).
- **Étape 2.** Cliquez sur l'ICÔNE ***Imprimer*** sur le panneau de commande et choisissez ***xyz_cube.gcode*** (Fig 2), cliquez sur le bouton pour lancer l'impression.
- **Étape 3.** Attendez que la hotend et le foyer atteignent la température de réglage (Fig. 3), la buse reviendra à la position d'origine, puis se déplacera au-dessus de la plate-forme d'impression et extrudera le filament, utilisez une pince à épiler. pour retirer le filament de sortie (Fig. 4).
- **Étape 4.** Lorsque la buse s'est déplacée vers le lit chaud et commence à imprimer, double-cliquez sur le bouton pour ouvrir un menu **Babystep Z** (Fig 5), tournez lentement le bouton pour affiner la hauteur d'impression. plate-forme, surveillez la distance entre la buse et le lit, jusqu'à ce que la distance soit bonne (Fig. 6).
- **Étape 5.** Attendez la fin de l'impression (Fig. 7), attendez que le foyer refroidisse (Fig. 8), puis retirez l'objet imprimé du foyer (Fig. 9).
![](./Operation/firstprint.png)

#### Imprimer un fichier de test multicolore
###### [![](https://img.youtube.com/vi/iddKadfrdjw/0.jpg)](https://www.youtube.com/watch?v=iddKadfrdjw)
Les étapes pour l'impression multicolore et l'impression monochrome sont fondamentalement les mêmes, mais avant de commencer l'impression, veuillez extruder quelques filaments de toutes les extrudeuses pour confirmer que l'extrémité chaude fonctionne normalement.
- **Étape 1.** Insérez la carte SD dans la prise pour carte SD de l'imprimante.
- **Étape 2.** Chauffez la buse et extrudez du filament. **Préparer>>Filament : *Préchauffer la buse : 200* -> *Extrudeuse : Tout* -> *Charger lentement***.
- **Étape 3.** Cliquez sur l'ICÔNE « Imprimer » sur le panneau de commande et choisissez ***M4_4CTest.gcode***, cliquez sur le bouton pour lancer l'impression.
- **Étape 4.** Ajustez finement la distance entre la buse et le lit.
- **Étape 5.** Attendez que l'impression soit terminée.

-----
### :fireworks: Félicitations !
Après avoir imprimé les premières œuvres, vous avez une compréhension de base du fonctionnement de l’imprimante 3D. Ensuite, vous pouvez imprimer d'autres fichiers de test ou découper votre propre modèle 3D et utiliser la machine pour l'imprimer.
Il est recommandé de télécharger et d'installer le logiciel de découpage, et de lire le guide de l'utilisateur du logiciel de découpage pour savoir comment l'utiliser. Pour plus de détails, veuillez vous référer au [:book: **Guide de découpage**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/4.Slicing).