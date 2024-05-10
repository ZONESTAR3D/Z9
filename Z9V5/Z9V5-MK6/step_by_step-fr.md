[LCD_MENU]: https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/LCDMENU_Description.md
[PRUSA_SLICER]: https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer
[VIDEO_POWERON]: https://github.com/ZONESTAR3D/Z9/assets/29502731/02fa8e57-a292-4aa5-bb7b-eaa703e3fc1b
[VIDEO_BEDLEVEL]: https://youtu.be/jNf98S0u2VQ
[VIDEO_LOADFILAMENT]: https://youtu.be/1rr4dXRxKc4
[VIDEO_PRINT1C]: https://youtu.be/NbVy8NjKt_s
[VIDEO_PRINT4C]: https://youtu.be/iddKadfrdjw

----
## <a id="choose-language">:globe_with_meridians: Choose language </a>
[![](../lanpic/EN.png)](./step_by_step.md)
[![](../lanpic/ES.png)](./step_by_step-es.md)
[![](../lanpic/PT.png)](./step_by_step-pt.md)
[![](../lanpic/FR.png)](./step_by_step-fr.md)
[![](../lanpic/DE.png)](./step_by_step-de.md)
[![](../lanpic/IT.png)](./step_by_step-it.md)
[![](../lanpic/RU.png)](./step_by_step-ru.md)
[![](../lanpic/JP.png)](./step_by_step-jp.md)
[![](../lanpic/KR.png)](./step_by_step-kr.md)

----
## Guide étape par étape
En un mot, à partir du moment où vous recevez la machine jusqu'au moment où vous pouvez imprimer votre propre fichier de modèle 3D, 5 étapes au total sont requises : **Installation - Mise à niveau du lit - Chargement des filaments - Impression du fichier gcode de test - Tranchage et imprimez votre propre fichier 3D**.
#### Installation
[![](https://img.youtube.com/vi/pdr8nLl3T3w/0.jpg)](https://www.youtube.com/watch?v=pdr8nLl3T3w)
#### Basic Operations
[![](https://img.youtube.com/vi/GrCOZ4ADHeA/0.jpg)](https://www.youtube.com/watch?v=GrCOZ4ADHeA)

### <a id ="a1">Étape 1. Installation</a>
- 1.1 **Installation**. Reportez-vous au [:book: **guide d'installation**](./1.Installation/Installation.md) et au [:clapper: **tutoriel vidéo d'installation**](https://youtu.be/pdr8nLl3T3w) pour terminer l'installation de la machine.
- 1.2 **Câblage**. le processus de câblage consiste essentiellement à insérer la fiche dans la prise correspondante. Ce à quoi vous devez faire attention, c'est **pour vous assurer que les connecteurs sont bien branchés**, en particulier pour les prises d'accueil à 2 broches. De plus, pour le câblage de la tête d'impression (hot end), veuillez noter qu'il existe plusieurs prises identiques mais de couleurs différentes, veuillez faire attention à les brancher en fonction de la couleur de la prise.
- 1.3 **Mise sous tension**. Une fois le câblage terminé, vous pouvez [:clapper: **allumer le Z9V5**][VIDEO_POWERON]. A noter notamment que le Z9V5 dispose de 2 interrupteurs d'alimentation. l'un est un ***interrupteur AC*** (l'interrupteur rouge à l'arrière de la machine) et un autre est un ***interrupteur DC*** (un interrupteur à bouton-poussoir rond en métal à l'avant du boîtier de commande de la machine), vous devez d'abord allumer l'interrupteur AC, puis **appuyer et maintenir** l'interrupteur DC pendant environ 5 secondes pour allumer le Z9V5.
- 1.4 **Testez simplement**. Après la mise sous tension, vous pouvez utiliser le menu sur l'écran LCD ([:book: **LCD Menu description**](./2.Operation/LCDMENU_Description.md)) pour vérifier si la machine peut fonctionner normalement. Cela implique généralement plusieurs étapes :
   - 1.4.1 **Préparer>>Accueil Auto>>Accueil Tout**. Cette étape consiste à faire revenir la tête d'impression de la machine à l'origine.
   - 1.4.2 **Préparation>>Température>>Préchauffer le PLA**. Cette étape consiste à vérifier l'extrémité chaude et le lit chaud peut être chauffé normalement. Dans cette étape, lorsque la température de la buse dépasse 60 degrés, vous devriez voir un ventilateur sur le côté droit de la tête d'impression (extrémité chaude) tourner. , c'est le ventilateur de refroidissement de l'extrémité chaude.
   - 1.4.3 **Préparation>>Température>>Vitesse du VENTILATEUR :**. Après avoir appuyé sur le bouton et réglé la vitesse du ventilateur (réglée sur 255), vous devriez maintenant pouvoir augmenter le ventilateur (sur le côté gauche pour le hotend M4V6).
   Après ces 3 étapes, il est essentiellement déterminé que la machine fonctionne normalement, vous pouvez passer aux étapes suivantes. Si vous constatez qu'une pièce ne fonctionne pas correctement, veuillez vérifier le câblage ou vous référer à[:clapper: **Tutoriel vidéo de test automatique de la machine**](https://youtu.be/Mf92BlmKA0A) pour faire une machine automatique essai.

### <a id ="a2">Étape 2. Mise à niveau du lit</a>
Avant de commencer l'impression, vous devez effectuer un simple nivellement du lit pour régler la hauteur entre la buse et le lit (plate-forme d'impression), afin que le filament puisse bien être collé sur le lit. Veuillez vous référer à [:clapper: **Tutoriel vidéo sur la mise à niveau du lit**][VIDEO_BEDLEVEL] pour le faire.

### <a id ="a3">Étape 3. Charger les filaments</a>
Référez-vous à ce [:clapper: tutoriel vidéo][VIDEO_LOADFILAMENT] pour charger les 4 filaments dans les extrudeuses et la hot end.
#### :warning: ATTENTION S'IL VOUS PLAÎT :warning:
1. **Vous devez charger les 4 filaments jusqu'à l'extrémité chaude, que vous imprimiez une couleur ou des impressions 3D multicolores.**
2. **Assurez-vous que les filaments ont été chargés jusqu'au bas de l'extrémité chaude, sinon cela pourrait bloquer l'extrémité chaude.**

### <a id ="a4">Étape 4. Imprimer le fichier gcode de test</a>
Les imprimantes 3D FDM ne peuvent reconnaître que les fichiers gcode, vous devez copier les fichiers gcode sur la carte SD, insérer la carte SD dans la prise pour carte SD de l'imprimante 3D, puis commencer à imprimer.
La Z9V5Pro étant une imprimante 3D dotée de 4 extrudeuses, nous vous suggérons d'imprimer un modèle 3D une couleur et un modèle 3D 4 couleurs pour tester si la machine fonctionne correctement.
#### Imprimer des impressions 3D en une seule couleur
##### [:clapper: tutoriel vidéo][VIDEO_PRINT1C]
- **Préparer le fichier gcode**. Localisez le fichier **xyz_cube.gcode** sur votre carte SD ou [:arrow_down: cliquez ici pour le télécharger](./3.Test_gcode/xyz_cube.zip) et décompressez-le sur votre PC, puis copiez le **xyz_cube .gcode** sur la carte SD, branchez la carte SD sur la prise SD de la machine.
- **Imprimer depuis la carte SD**. Déplacez le curseur sur l'élément **Imprimer** sur l'écran LCD, cliquez sur le bouton et choisissez le fichier **xyz_cube**, cliquez sur le bouton pour lancer l'impression.
- **Régler finement la hauteur de la buse**. Attendez le chauffage de la buse et du lit chaud, et lorsque vous commencez à imprimer la première couche, double-cliquez sur le bouton de l'écran LCD et ajustez la distance entre la buse et le lit (la buse est plus haute que l'autocollant d'environ 0,4 mm), attendez que l'impression soit terminée. fini.
#### Imprimer des impressions 3D en 4 couleurs
##### [:clapper: tutoriel vidéo][VIDEO_PRINT4C]
- **Préparer le fichier gcode**. Localisez le fichier **M4_4CTest.gcode** sur votre carte SD ou [:arrow_down: cliquez ici pour le télécharger](./3.Test_gcode/M4_4CTest.zip) et décompressez-le sur votre PC, puis copiez le **M4_4CTest. .gcode** sur la carte SD, branchez la carte SD sur la prise SD de la machine.
- **Imprimer depuis la carte SD**. Déplacez le curseur sur l'élément **Imprimer** sur l'écran LCD, cliquez sur le bouton et choisissez le fichier **M4_4CTest**, cliquez sur le bouton pour lancer l'impression.
- **Régler finement la hauteur de la buse**. Attendez le chauffage de la buse et du lit chaud, et lorsque vous commencez à imprimer la première couche, double-cliquez sur le bouton de l'écran LCD et ajustez la distance entre la buse et le lit (la buse est plus haute que l'autocollant d'environ 0,4 mm), attendez que l'impression soit terminée. fini.

### <a id ="a5">Étape 5. Découper votre propre modèle 3D et l'imprimer</a>
Avant d'imprimer vos propres modèles 3D, vous devez convertir le fichier de modèle 3D (un fichier au format stl/obj/AMF qui [téléchargé depuis Internet](#a6) ou dessiné par vous-même) en un fichier gcode, ce processus est appelé < u>"**tranchage**"</u>.
- Tout d'abord, vous devez télécharger le logiciel de découpage et l'installer sur votre ordinateur, puis définir les paramètres de votre machine dans le logiciel de découpage ou charger le fichier prédéfini de votre machine défini par le fabricant de l'imprimante 3D.
- Ensuite, vous devez exécuter le logiciel de découpage, et vous devrez peut-être également définir certains paramètres en fonction des caractéristiques de votre fichier de modèle 3D, puis exécuter le découpage.
- Une fois le découpage terminé, copiez le fichier gcode généré sur la carte SD et suivez la [:point_right:Stpe 4](#a4) pour l'imprimer par votre imprimante 3D.
#### *PrusaSlicer* est le logiciel de découpage que nous avons recommandé, veuillez vous référer à [:point_right:here][PRUSA_SLICER] pour télécharger et installer le logiciel PrusaSlicer et lire le guide de l'utilisateur.
:warning: **ATTENTION S'IL VOUS PLAÎT** :warning:    
Le Z9V5Pro-MK6 par défaut est équipé d'une extrémité chaude M4V6 (4-IN-1-OUT mix Color), veuillez faire attention à choisir le préréglage de l'imprimante (Z9 + M4 Hotend) lors du découpage.

----
### <a id ="a6">Célèbres sites de téléchargement de modèles 3D gratuits</a>
- [thingiverse](https://www.thingiverse.com/)  
- [printables](https://www.printables.com/)  
- [youmagine](https://www.youmagine.com/)   

----