[LCD_MENU]: https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/LCDMENU_Description.md
[PRUSA_SLICER]: https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer

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
## Guida passo passo
In una parola, dal momento in cui hai ricevuto la macchina al momento in cui puoi stampare il tuo file del modello 3D, sono necessari un totale di 5 passaggi: **Installazione - Livellamento del piano - Caricamento dei filamenti - Stampa del file gcode di prova - Affettatura e stampa il tuo file 3D**.

### <a id ="A1">Passaggio 1. Installazione</a>
- 1.1 **Installazione**. Fare riferimento a [:book: **guida all'installazione**](./1.Installation/Installation.md) e [:clapper: **video tutorial sull'installazione**](https://youtu.be/pdr8nLl3T3w) per completare l'installazione della macchina.
- 1.2 **Cablaggio**. il processo di cablaggio consiste sostanzialmente nell'inserire la spina nella presa corrispondente. Ciò a cui devi prestare attenzione è **assicurarti che i connettori siano inseriti correttamente**, in particolare per le prese docking 2PIN. Inoltre, per il cablaggio della testina di stampa (hot end), tenere presente che esistono più prese uguali ma di colore diverso, prestare attenzione a collegarle in base al colore della presa.
- 1.3 **Accensione**. Una volta completato il cablaggio, puoi [:clapper: **accendere Z9V5**](https://youtu.be/xTlMHtxkGoY). Si prega di notare in particolare che lo Z9V5 dispone di 2 interruttori di alimentazione. quello è ***interruttore CA***(l'interruttore rosso sul retro della macchina) e un altro è ***interruttore CC***(un interruttore a pulsante rotondo in metallo sulla parte anteriore della scatola di controllo della macchina), è necessario prima accendere l'interruttore CA, quindi **tenere premuto** l'interruttore CC per circa 5 secondi per accendere Z9V5.
- 1.4 **Semplicemente prova**. Dopo l'accensione, è possibile utilizzare il menu sullo schermo LCD ([:book: **Descrizione menu LCD**](./2.Operation/LCDMENU_Description.md)) per verificare se la macchina può funzionare normalmente. Di solito questo comporta diversi passaggi:
   - 1.4.1 **Prepara>>Ritorno automatico>>Home tutto**. Questo passaggio serve a far ritornare la testina di stampa della macchina all'origine.
   - 1.4.2 **Prepara>>Temperatura>>Preriscalda PLA**. Questo passaggio serve per verificare che l'hot end e che il letto caldo possa essere riscaldato normalmente. In questo passaggio, quando la temperatura dell'ugello supera i 60 gradi, dovresti vedere una ventola sul lato destro della testina di stampa (hot end) che gira , questa è la ventola di raffreddamento dell'hotend.
   - 1.4.3 **Preparazione>>Temperatura>>Velocità VENTOLA:**. Dopo aver premuto la manopola e impostato la velocità della ventola (impostata su 255), ora dovresti essere in grado di alzare anche la ventola (sul lato sinistro per l'hotend M4V6).
   Dopo questi 3 passaggi, una volta stabilito che la macchina funziona normalmente, è possibile procedere ai passaggi successivi. Se trovi che qualche parte non funziona correttamente, ricontrolla il cablaggio o fai riferimento a[:clapper: **tutorial video sul test automatico della macchina**](https://youtu.be/Mf92BlmKA0A) per eseguire una macchina automatica test.

### <a id ="A2">Passaggio 2. Livellare il letto</a>
Prima di iniziare a stampare, è necessario eseguire un semplice livellamento del letto per impostare l'altezza tra l'ugello e il letto (piattaforma di stampa), in modo che il filamento possa essere incollato bene sul letto. Fare riferimento a [:clapper: **Tutorial video sul livellamento del letto**](https://youtu.be/nxzB7ho1kNo) per farlo.

### <a id ="A3">Passaggio 3. Carica i filamenti</a>
Fai riferimento a questo [:clapper: video tutorial](https://youtu.be/KZQdL7Rgy1s) per caricare tutti e 4 i filamenti negli estrusori e nell'hot end.
#### :warning: ATTENZIONE PER FAVORE :warning:
1. **È necessario caricare tutti e 4 i filamenti sull'hot-end qualunque sia la stampa 3D monocolore o multicolore.**
2. **Assicurarsi che i filamenti siano stati caricati sul fondo dell'hot end, altrimenti potrebbe causare il blocco dell'hot end.**

### <a id ="A4">Passaggio 4. Stampa il file gcode di prova</a>
Le stampanti 3D FDM possono riconoscere solo file gcode, è necessario copiare i file gcode sulla scheda SD, inserire la scheda SD nella presa per scheda SD della stampante 3D e quindi iniziare a stampare.
Poiché Z9V5Pro è una stampante 3D con 4 estrusori, ti suggeriamo di stampare un modello 3D a un colore e un modello 3D a 4 colori per verificare se la macchina funziona correttamente.
#### Stampa stampe 3D a un colore
- **Prepara il file gcode**. Individua il file **xyz_cube.gcode** dalla tua scheda SD o [:arrow_down: fai clic qui per scaricarlo](./3.Test_gcode/xyz_cube.zip) e decomprimilo sul tuo PC, quindi copia il **xyz_cube .gcode** su scheda SD, collegare la scheda SD alla presa SD della macchina.
- **Stampa da scheda SD**. Spostare il cursore sulla voce **Stampa** sullo schermo LCD, fare clic sulla manopola e scegliere il file **xyz_cube**, fare clic sulla manopola per avviare la stampa.
- **Regolazione fine dell'altezza dell'ugello**. Attendere il riscaldamento dell'ugello e del piano caldo e, quando si inizia a stampare il primo strato, fare doppio clic sulla manopola dello schermo LCD e regolare con precisione la distanza dall'ugello al letto (l'ugello è più alto dell'adesivo di circa 0,4 mm), attendere fino al completamento della stampa. finito.
#### Stampa stampe 3D a 4 colori
- **Prepara il file gcode**. Individua il file **M4_4CTest.gcode** dalla tua scheda SD o [:arrow_down: fai clic qui per scaricarlo](./3.Test_gcode/M4_4CTest.zip) e decomprimilo sul tuo PC, quindi copia **M4_4CTest .gcode** su scheda SD, collegare la scheda SD alla presa SD della macchina.
- **Stampa da scheda SD**. Spostare il cursore sulla voce **Stampa** sullo schermo LCD, fare clic sulla manopola e scegliere il file **M4_4CTest**, fare clic sulla manopola per avviare la stampa.
- **Regolazione fine dell'altezza dell'ugello**. Attendere il riscaldamento dell'ugello e del piano caldo e, quando si inizia a stampare il primo strato, fare doppio clic sulla manopola dello schermo LCD e regolare con precisione la distanza dall'ugello al letto (l'ugello è più alto dell'adesivo di circa 0,4 mm), attendere fino al completamento della stampa. finito.

### <a id ="A5">Passaggio 5. Taglia il tuo modello 3D e stampalo</a>
Prima di stampare i tuoi modelli 3D, devi convertire il file del modello 3D (un file in formato stl/obj/AMF [scaricato da Internet](#A6) o disegnato da te) in un file gcode, questo processo è chiamato <u>**affettare**</u>.
- Innanzitutto devi scaricare il software di slicing e installarlo sul tuo computer, quindi impostare i parametri della tua macchina nel software di slicing o caricare il file di preimpostazione della tua macchina impostato dal produttore della stampante 3D.
- Successivamente, è necessario eseguire il software di slicing e potrebbe anche essere necessario impostare alcuni parametri in base alle caratteristiche del file del modello 3D e quindi eseguire lo slicing.
- Al termine dell'affettatura, copia il file gcode generato sulla scheda SD e segui [:point_right:Stpe 4](#A4) per stamparlo con la tua stampante 3D.
#### *PrusaSlicer* è il software di slicing che abbiamo consigliato, fare riferimento a [:point_right:here][PRUSA_SLICER] per scaricare e installare il software PrusaSlicer e leggere la guida per l'utente.
:warning: **ATTENZIONE** :warning:    
Z9V5Pro-MK6 predefinito è dotato di un hotend M4V6 (4-IN-1-OUT mix Color), prestare attenzione a scegliere la preimpostazione della stampante (Z9 + M4 Hotend) durante lo slicing.

----
### <a id ="A6">Famosi siti web per il download gratuito di modelli 3D</a>
- [thingiverse](https://www.thingiverse.com/)  
- [printables](https://www.printables.com/)  
- [youmagine](https://www.youmagine.com/)   

----