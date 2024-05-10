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
# Guida per l'utente per la stampante 3D ZONESTAR Z9V5Pro-MK6

----
## :warning: ATTENZIONE PER FAVORE
#### :loudspeaker: Prima di utilizzare la macchina, leggere attentamente [:book:"Precauzioni per l'utilizzo di M4V6"][M4V6_PRECAUTION].
#### :loudspeaker: È necessario caricare 4 filamenti sull'hotend M4V6 contemporaneamente, un funzionamento errato potrebbe bloccare l'hotend del colore misto. Se il blocco dell'hotend è causato da un funzionamento errato, non è coperto dalla garanzia. Per come caricare i filamenti, fare riferimento a [:book: questa guida][Z9V5MK6_LOADFILAMENT].
#### :loudspeaker: Se sei un principiante della stampante 3D, leggi attentamente il [:book: Guida passo passo][Z9V5MK6_STEPBYSTEP] e segui i passaggi da eseguire.
- [:book: **Precauzioni per l'utilizzo di M4V6**][M4V6_PRECAUTION]
- [:book: **Come caricare correttamente i filamenti**][Z9V5MK6_LOADFILAMENT]
- [:book: **Guida passo passo**][Z9V5MK6_STEPBYSTEP]
<!-- - [:blue_book: file PDF della guida passo passo](./step_by_step.pdf) -->

------
## :book: Contenuto
- [**Guida all'installazione**](#a1)
- [**Guida operativa**](#a2)
- [**Prova file gcode**](#a3)
- [**Software di slicing**](#a4)
- [**Firmware**](#a5)
- [**Risoluzione dei problemi**](#a6)
- [**Stampa file stl delle parti**](#a7)
- [**Funzioni di aggiornamento opzionali**](#a8)

-----
## <a id="a1"> 1. Guida all'installazione </a>
Innanzitutto, fare riferimento ai seguenti documenti e video per completare l'installazione e il cablaggio della macchina.
### Installazione
- [:book: Documento online della Guida all'installazione](./1.Installation/Installation.md)
- [:blue_book: file PDF della guida all'installazione](./1.Installation/Installation.pdf)
- [:clapper: Guida all'installazione Video tutorial](https://youtu.be/TGHUVzV1Pg4)
### Cablaggio
- [:book: Documento online della guida al cablaggio](./1.Installation/Wiring.md)
- [:blue_book: file PDF della guida al cablaggio](./1.Installazione/Wiring.pdf)
- [:art: Schema elettrico](./1.Installation/Z9V5Pro_Wiring_Diagram.jpg)
- [:clapper: Video tutorial sul cablaggio](https://youtu.be/tQQNLDOpdQU)

## <a id="a2"> 2. Guida operativa </a>
### **Introduzione al pannello di controllo LCD**
Dopo aver completato l'installazione e il cablaggio, dare un'occhiata alla guida seguente per sapere come utilizzare il pannello di controllo (schermo LCD) e comprendere le funzioni del menu LCD in generale.  
- [:book: Documento online del menu LCD](./2.Operation/LCDMENU_Description.md)
- [:blue_book: file PDF del menu LCD](./2.Operation/LCDMENU_Description.pdf)
#### **Stampa i tuoi primi lavori**
Adesso puoi provare a stampare i tuoi lavori "Hello word", prima di iniziare la stampa, devi prima fare una semplice correzione all'altezza del letto caldo (si chiama "bed leveling"), e poi caricare i filamenti nell'estrusore (tieni presente che, indipendentemente dal colore della stampa, è necessario caricare tutti e 4 i filamenti negli estrusori e nell'hot end). Successivamente, puoi inserire la scheda SD nella macchina e scegliere un file gcode del modello 3D di prova nella scheda SD. Per i dettagli fare riferimento ai documenti sottostanti.
- [:book: Documento online della Guida operativa](./2.Operation/Operation.md)
- [:blue_book: file PDF della Guida operativa](./2.Operazione/Operazione.pdf)
#### :page_with_curl: Altre funzionalità
È inoltre possibile leggere i seguenti documenti per acquisire una comprensione più approfondita dell'estrusore (estremità calda e testina di stampa) utilizzato dalla macchina, nonché di alcune funzionalità avanzate della macchina.
- [:book: Guida all'uso della funzione Mix Color][LINK_MIX_FEATURE]
- [:book: Introduzione all'hotend M4V6][LINK_M4V6]
- [:book: Stampa da PC](./2.Operation/PrintFromPC/readme.md)
- [:book: Guida all'uso delle funzionalità Advance](./2.Operation/Advance_Features.md)

## <a id="a3"> 3. Testare il file del codice G </a>
**:matita: cos'è il codice G nella stampa 3D?**
Il codice G è un'informazione o un'istruzione richiesta dalla stampante 3D per stampare un oggetto tridimensionale, è il linguaggio che la stampante 3D può comprendere. Il G-Code viene generato dal tuo software di slicing, traducendo un file di modellazione 3D standard come STL, oggetto, file AMF ecc.. :page_with_curl: [**Referencia 1**][GCODE_REF1] :page_with_curl: [**Referencia 2**][GCODE_REF2]     
Abbiamo memorizzato alcuni file gcode di prova nella scheda SD, per verificare se la macchina funzionava correttamente o per dimostrare quali funzioni di stampa ha questa macchina. Se non riesci a trovare i file gcode di prova nella scheda SD, scaricali da [:arrow_down: **qui**](./3.TestGcode/Test_gcode.zip).    
- **xyz_cube.gcode**: un semplice file gcode di prova utilizzato per verificare se la macchina funzionava bene.
- **dog.gcode**: un classico file di test della qualità di stampa.
- **Vase.gcode**: un vaso di prova.
   - **GradientMix_Vase.gcode**: un vaso uguale a vase.gcode ma abilitata la funzione "gradient mix".
   - **RandomMix_Vase.gcode**: un vaso uguale a vase.gcode ma abilitata la funzione "mix casuale".
- **M4_4CTest.gcode**: un file di test dei colori base 4 per stampante 3D con hot end M4.
- **M4_4C_BODY3D.gcode**: un file di prova a 4 colori più grande.
- **16color_tower.gcode**: un file di test del colore base 16 per mostrare il risultato di filamenti di colore diverso mescolati.
- **level_test_310.gcode**: un file di test utilizzato per verificare la planarità del letto caldo (senza livellamento automatico del letto).
- **level_test_310-G29.gcode**: un file di test utilizzato per verificare la planarità del letto caldo (con livellamento automatico del letto).
**[:arrow_down: Scarica altri file gcode di prova][M4_TEST_GCODE].**
 
## <a id="a4"> 4. Affettare </a>
**[:matita: cos'è l'affettamento nella stampa 3D?](https://en.wikipedia.org/wiki/Slicer_(3D_printing))**
Uno slicer è un software di generazione del percorso utensile utilizzato nella maggior parte dei processi di stampa 3D per la conversione di un modello di oggetto 3D in istruzioni specifiche per la stampante. In particolare, la conversione da un modello in formato STL a comandi di stampante in formato g-code nella fabbricazione di filamenti fusi e altri processi simili.    
- [:book:Documento online della Guida per l'utente di Slicer](./4.Slicing/readme.md)
- [:blue_book: File PDF della guida per l'utente di Slicer](./4.Slicing/Slicing.pdf)

## <a id="a5"> 5. Firmware </a>
**:matita: Cos'è il file bin del firmware e il codice sorgente?**
Il file bin del firmware è la memoria esatta che viene scritta nella flash incorporata.
Il codice sorgente del firmware è la parte principale del firmware. Il nostro codice sorgente del firmware è basato su [**marlin**](https://www.marlinfw.org).    
È possibile scaricare il file bin del firmware o il codice sorgente dal collegamento sottostante.   
- [:arrow_down: file bin del firmware][LINK_FIRMWARE]
- [:arrow_down: codice sorgente del firmware][LINK_SOURCECODE]

## <a id="a6"> 6. Risoluzione dei problemi </a>
In caso di problemi durante l'installazione e l'utilizzo della stampante, provare prima a trovare una soluzione nel [:book: Documento online sulla risoluzione dei problemi][LINK_TROUBLESHOOTING]. Se non riesci a risolvere questo problema, contattaci via email (:email: support@zonestar3d.com).

## <a id="a7"> 7. Stampa parti </a>
Sulla macchina sono presenti diversi componenti che vengono stampati e abbiamo anche preparato alcuni aggiornamenti per te. Se vuoi, puoi scaricarli, stamparli e poi installarli sul tuo computer.

-----
## <a id="a8"> Funzionalità opzionali </a>
Abbiamo introdotto alcune funzionalità opzionali per questa macchina, puoi aggiornare queste funzionalità in qualsiasi momento in base alle tue preferenze. Se sei interessato a questo, leggi la guida alle funzionalità di aggiornamento opzionali per ottenere informazioni più dettagliate.
- [:book: documento online della guida alle funzionalità di aggiornamento opzionali][Z9V5MK6_OPTION]
- [:blue_book: file pdf della guida alle funzionalità di aggiornamento opzionali](./OptionalFeatures.pdf)
