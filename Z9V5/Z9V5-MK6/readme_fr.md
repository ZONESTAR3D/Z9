[M4V6_PRECAUTION]: https://github.com/ZONESTAR3D/Upgrade-kit-guide/blob/main/HOTEND/M4/M4_V6/M4V6_Precaution.md
[Z9V5MK6_STEPBYSTEP]: https://github.com/ZONESTAR3D/Z9/blob/main/Z9V5/Z9V5-MK6/step_by_step.md
[Z9V5MK6_LOADFILAMENT]: https://github.com/ZONESTAR3D/Z9/blob/main/Z9V5/Z9V5-MK6/2.Operation/Operation.md#load-filaments
[Z9V5MK6_OPTION]: https://github.com/ZONESTAR3D/Z9/blob/main/Z9V5/Z9V5-MK6/OptionalFeatures.md
[LINK_M4V6]: https://github.com/ZONESTAR3D/Upgrade-kit-guide/blob/main/HOTEND/M4/M4_V6
[LINK_MIX_FEATURE]: https://github.com/ZONESTAR3D/Document-and-User-Guide/blob/master/Mixing_Color
[LINK_FIRMWARE]: https://github.com/ZONESTAR3D/Firmware/blob/master/Z9/Z9V5/bin/Z9V5Pro-MK6
[LINK_SOURCECODE]: https://github.com/ZONESTAR3D/source-code-for-3d-printer
[LINK_TROUBLESHOOTING]: https://github.com/ZONESTAR3D/Z9/blob/main/Z9V5/Z9V5_FAQ
[M4_TEST_GCODE]: https://github.com/ZONESTAR3D/Slicing-Guide/blob/master/PrusaSlicer/test_gcode/M4/readme.md
[GCODE_REF1]: https://beginner3dprinting.com/what-is-g-code-in-3d-printing/
[GCODE_REF2]: https://www.reprap.org/wiki/G-code

----
## <a id="choose-language">:globe_with_meridians: Choose language </a>
[![](../lanpic/EN.png)](./readme.md)
[![](../lanpic/ES.png)](./readme_es.md)
[![](../lanpic/PT.png)](./readme_pt.md)
[![](../lanpic/FR.png)](./readme_fr.md)
[![](../lanpic/DE.png)](./readme_de.md)
[![](../lanpic/IT.png)](./readme_it.md)
[![](../lanpic/RU.png)](./readme_ru.md)
[![](../lanpic/JP.png)](./readme_jp.md)
[![](../lanpic/KR.png)](./readme_kr.md)

----
# Guide de l'utilisateur pour l'imprimante 3D ZONESTAR Z9V5Pro-MK6

----
## :warning: ATTENTION S'IL VOUS PLAÎT
#### :loudspeaker: Avant d'utiliser la machine, veuillez lire attentivement [:book:"Précautions d'utilisation du M4V6"][M4V6_PRECAUTION].
#### :loudspeaker: Il faut charger 4 filaments simultanément sur le hotend M4V6, un fonctionnement incorrect peut bloquer le hotend de mélange de couleurs. Si le blocage de l'extrémité chaude est dû à un fonctionnement incorrect, il n'est pas couvert par la garantie. Pour savoir comment charger les filaments, veuillez vous référer à [:book: this guide][Z9V5MK6_LOADFILAMENT].
#### :loudspeaker: Si vous êtes débutant en imprimante 3D, veuillez lire attentivement le [Guide étape par étape][Z9V5MK6_STEPBYSTEP] et suivre les étapes à suivre.
- [:book: **Précautions d'utilisation de M4V6**][M4V6_PRECAUTION]
- [:book: **Comment charger correctement les filaments**][Z9V5MK6_LOADFILAMENT]
- [:book: **Guide étape par étape**][Z9V5MK6_STEPBYSTEP]
<!-- - [:blue_book: Fichier PDF du guide étape par étape](./step_by_step.pdf) -->

------
## :book: Contenu
- [**Guide d'installation**](#a1)
- [**Guide d'utilisation**](#a2)
- [**Tester les fichiers gcode**](#a3)
- [**Logiciel de découpage**](#a4)
- [**Micrologiciel**](#a5)
- [**Dépannage**](#a6)
- [**Imprimer les fichiers stl des pièces**](#a7)
- [**Fonctionnalités de mise à niveau facultatives**](#a8)

-----
## <a id="a1"> 1. Guide d'installation </a>
Tout d'abord, veuillez vous référer aux documents et vidéos suivants pour terminer l'installation et le câblage de la machine.
### Installation
- [:book: Document en ligne du guide d'installation](./1.Installation/Installation.md)
- [:blue_book: fichier PDF du guide d'installation](./1.Installation/Installation.pdf)
- [:clapper: Tutoriel vidéo du guide d'installation](https://youtu.be/TGHUVzV1Pg4)
### Câblage
- [:book: Document en ligne du guide de câblage](./1.Installation/Wiring.md)
- [:blue_book: fichier PDF du guide de câblage](./1.Installation/Wiring.pdf)
- [:art: Schéma de câblage](./1.Installation/Z9V5Pro_Wiring_Diagram.jpg)
- [:clapper: Tutoriel vidéo sur le câblage](https://youtu.be/tQQNLDOpdQU)

## <a id="a2"> 2. Guide d'utilisation </a>
### **Présentation du panneau de commande LCD**
Après avoir terminé l'installation et le câblage, veuillez consulter le guide ci-dessous pour savoir comment utiliser le panneau de commande (écran LCD) et comprendre les fonctions du menu LCD en général.
- [:book: Document en ligne du menu LCD](./2.Operation/LCDMENU_Description.md)
- [:blue_book: Fichier PDF du menu LCD](./2.Operation/LCDMENU_Description.pdf)
#### **Imprimez vos premiers travaux**
Vous pouvez maintenant essayer d'imprimer vos œuvres "Bonjour mot", avant de commencer l'impression, vous devez d'abord faire une simple correction de la hauteur du lit chaud (cela s'appelle "nivellement du lit"), puis charger les filaments dans l'extrudeuse. (veuillez noter que quelle que soit la couleur de votre impression, vous devez charger les 4 filaments dans les extrudeuses et la hot end). Ensuite, vous pouvez insérer la carte SD dans la machine et choisir un fichier gcode de modèle 3D de test dans la carte SD. Pour plus de détails, veuillez vous référer aux documents ci-dessous.  
- [:book: Document en ligne du Guide d'utilisation](./2.Operation/Operation.md)
- [:blue_book: fichier PDF du guide d'utilisation](./2.Operation/Operation.pdf)
#### :page_with_curl: Plus de fonctionnalités
Vous pouvez également lire les documents suivants pour mieux comprendre l'extrudeuse (extrémité chaude et tête d'impression) utilisée par votre machine, ainsi que certaines fonctionnalités avancées de la machine.
- [:book: Guide d'utilisation de la fonctionnalité Mélanger les couleurs][LINK_MIX_FEATURE]
- [:book: Introduction au M4V6 Hotend][LINK_M4V6]
- [:book: Imprimer depuis un PC](./2.Operation/PrintFromPC/readme.md)
- [:book: Guide d'utilisation des fonctionnalités avancées](./2.Operation/Advance_Features.md)

## <a id="a3"> 3. Testez le fichier G-code </a>
**:crayon: Qu'est-ce que le G-code dans l'impression 3D ?**
Le G-code est une information ou des instructions dont l'imprimante 3D a besoin pour imprimer un objet en 3 dimensions, c'est le langage que l'imprimante 3D peut comprendre. Le G-Code est généré par votre logiciel de découpage, en traduisant un fichier de modélisation 3D standard tel qu'un STL, un objet, un fichier AMF, etc. :page_with_curl: [**Referencia 1**][GCODE_REF1] :page_with_curl: [**Referencia 2**][GCODE_REF2]    
Nous avons stocké des fichiers gcode de test sur la carte SD, pour aider à vérifier si la machine fonctionnait correctement ou pour démontrer les fonctions d'impression dont dispose cette machine. Si vous ne trouvez pas les fichiers gcode de test sur la carte SD, veuillez les télécharger depuis [:arrow_down: **ici**](./3.TestGcode/Test_gcode.zip).   
- **xyz_cube.gcode**: Un simple fichier gcode de test utilisé pour vérifier si la machine fonctionnait bien.
- **dog.gcode** : Un fichier de test de qualité d'impression classique.
- **Vase.gcode**: Un vase de test.
   - **GradientMix_Vase.gcode**: Un vase identique à vase.gcode mais activé la fonction "gradient mix".
   - **RandomMix_Vase.gcode**: Un vase identique à vase.gcode mais activé la fonction "mélange aléatoire".
- **M4_4CTest.gcode** : Un fichier de test de base 4 couleurs pour imprimante 3D avec une extrémité chaude M4.
- **M4_4C_BODY3D.gcode**: Un fichier de test 4 couleurs plus grand.
- **16color_tower.gcode**: Un fichier de test de couleurs de base 16 pour montrer le résultat du mélange de filaments de différentes couleurs.
- **level_test_310.gcode**: Un fichier de test utilisé pour vérifier la planéité du lit chaud (sans nivellement automatique du lit).
- **level_test_310-G29.gcode**: Un fichier de test utilisé pour vérifier la planéité du lit chaud (avec nivellement automatique du lit).
**[:arrow_down: Téléchargez plus de fichiers gcode de test][M4_TEST_GCODE].**
 
## <a id="a4"> 4. Découpage </a>
**[:pencil: Qu'est-ce que le découpage en tranches dans l'impression 3D ?](https://en.wikipedia.org/wiki/Slicer_(3D_printing))**   
Un slicer est un logiciel de génération de parcours d'outil utilisé dans la majorité des processus d'impression 3D pour la conversion d'un modèle d'objet 3D en instructions spécifiques pour l'imprimante. En particulier, la conversion d'un modèle au format STL en commandes d'imprimante au format g-code dans la fabrication de filaments fondus et d'autres processus similaires.   
- [:book: Document en ligne du Guide de l'utilisateur de Slicer](./4.Slicing/readme.md)
- [:blue_book: Fichier PDF du guide de l'utilisateur du Slicer](./4.Slicing/Slicing.pdf)

## <a id="a5"> 5. Micrologiciel </a>
**:pencil: Qu'est-ce que le fichier bin du micrologiciel et le code source ?**   
Le fichier bin du micrologiciel est la mémoire exacte écrite sur la mémoire flash intégrée.    
Le code source du micrologiciel constitue la partie essentielle du micrologiciel. Le code source de notre firmware est basé sur [**marlin**](https://www.marlinfw.org).   
Vous pouvez télécharger le fichier bin du micrologiciel ou le code source à partir du lien ci-dessous.   
- [:arrow_down: fichier bin du micrologiciel][LINK_FIRMWARE]
- [:arrow_down: Code source du micrologiciel][LINK_SOURCECODE]

## <a id="a6"> 6. Dépannage </a>
Si vous rencontrez des problèmes lors de l'installation et de l'utilisation de l'imprimante, essayez d'abord de trouver une solution dans le [:book: Dépannage du document en ligne][LINK_TROUBLESHOOTING] d'abord. Si vous ne parvenez pas à résoudre ce problème, veuillez nous contacter par email (:email: support@zonestar3d.com).

## <a id="a7"> 7. Imprimer les pièces </a>
Plusieurs composants de la machine sont imprimés et nous avons également préparé quelques mises à niveau pour vous. Si vous le souhaitez, vous pouvez les télécharger et les imprimer, puis les installer sur votre machine.

-----
## <a id="a8"> Fonctionnalités facultatives </a>
Nous avons introduit quelques fonctionnalités optionnelles pour cette machine, vous pouvez mettre à niveau ces fonctionnalités à tout moment selon vos préférences. Si cela vous intéresse, veuillez lire le guide des fonctionnalités de mise à niveau facultatives pour obtenir des informations plus détaillées.   
- [:book: Document en ligne du guide des fonctionnalités de mise à niveau facultatives][Z9V5MK6_OPTION]
- [:blue_book: fichier pdf du guide des fonctionnalités de mise à niveau facultatives](./OptionalFeatures.pdf)

