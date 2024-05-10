
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
## Guida operativa
Prima di iniziare a stampare, è necessario livellare il letto caldo (regolare con precisione la distanza tra l'ugello e la piattaforma di stampa) e caricare i filamenti negli estrusori e nell'estremità calda.
## Livellamento del letto caldo
#### :warning: per le stampanti 3D FDM, la distanza tra l'ugello e il letto caldo è molto importante quando si stampa il primo strato. Se la distanza è troppo ravvicinata, i filamenti non potranno fuoriuscire dall'ugello e potrebbero addirittura danneggiare l'ugello e il letto caldo. Se la distanza è eccessiva, i filamenti non possono incollarsi sul letto caldo, gli strati successivi non possono essere impilati correttamente e la stampa fallisce.
###### [![](https://img.youtube.com/vi/jNf98S0u2VQ/0.jpg)](https://www.youtube.com/watch?v=jNf98S0u2VQ)
- **Passaggio 1.** Accendi la stampante 3D e poi esegui ***Prepara>>Auto Home>>Home All*** sul MENU LCD, attendi che l'hotend raggiunga la posizione HOME.
- **Passaggio 2.** Stringere i dadi a mano sotto il letto per abbassare il letto nella posizione più bassa (Fig. 1).
- **Passaggio 3.** Eseguire ***Preparazione>> Livellamento del letto>> Punto 1*** sul pannello di controllo (Fig 2), l'ugello andrà agli angoli del letto, allentare i dadi a mano sotto il piano caldo (Fig 3) e lasciare che l'ugello quasi tocchi il piano caldo (Fig 4). Continua a fare ***Punto 2/3/4*** finché tutti e 4 gli angoli non saranno stati livellati.
- **Passaggio 4.** Ripeti il passaggio 3 ed esegui 2 ~ 3 giri, fino a quando tutti e quattro gli angoli sono alla stessa altezza.
![](./Operation/levelbed.png)

----
### Caricare i filamenti
###### [![](https://img.youtube.com/vi/1rr4dXRxKc4/0.jpg)](https://www.youtube.com/watch?v=1rr4dXRxKc4)
Questa stampante è dotata di quattro estrusori e un hot end per la miscelazione dei colori 4-IN-1-OUT. Gli estrusori e l'hot end sono collegati da una guida del filamento (tubo in PTFE). ***Prima di stampare, è necessario caricare tutti e 4 i filamenti negli estrusori e inserirli nella parte inferiore dell'hot end.***
- **Passaggio 1.** Eseguire ***Preparazione>>Auto Home>>Home All*** sul pannello di controllo, quindi eseguire ***Preparazione>>Temperatura>> Preriscaldamento PLA***, in attesa che venga raggiunta la temperatura dell'ugello a 190 ℃ (Fig. 1).
- **Passaggio 2.** Utilizzare una pinza diagonale per tagliare la testa del filamento (Fig 2), quindi premere la maniglia dell'estrusore n. 1 e inserire il filamento, spingere il filamento finché non si vede il filamento nel PTFE guida (Fig. 3). Ruota l'ingranaggio dell'estrusore n. 1 (Fig. 4), osserva il filamento finché non entra nella parte inferiore dell'hot end.
- **Passaggio 3.** Utilizzando lo stesso metodo del passaggio 2 per caricare i filamenti nell'estrusore n. 2 ~ estrusore n. 4, osservare i filamenti finché non entrano nella parte inferiore dell'hot end.
- **Passaggio 4.** Ruota lentamente l'ingranaggio dell'estrusore n. 1 ~ dell'estrusore n. 4 uno alla volta e osserva l'ugello, finché non vedi il filamento fuoriuscire dall'ugello (Fig 5).
![](./Operation/loadfilament.png)

----
### Stampa i tuoi lavori "Hellow World".
#### Stampa un file di prova a colore singolo
###### [![](https://img.youtube.com/vi/NbVy8NjKt_s/0.jpg)](https://www.youtube.com/watch?v=NbVy8NjKt_s)
- **Passaggio 1.** Inserire la scheda SD nell'apposita presa sulla stampante (Fig. 1).
- **Passaggio 2.** Fare clic sull'ICONA ***Stampa*** sul pannello di controllo e scegliere ***xyz_cube.gcode*** (Fig 2), fare clic sulla manopola per avviare la stampa.
- **Passaggio 3.** Attendere fino a quando l'hotend e il piano caldo raggiungono la temperatura impostata (Fig 3), l'ugello si posizionerà nella posizione di origine, quindi si sposterà sopra la piattaforma di stampa ed estruderà il filamento, utilizzare una pinzetta per rimuovere il filamento in uscita (Fig 4).
- **Passaggio 4.** Quando l'ugello si è spostato sul letto caldo e ha iniziato a stampare, fare doppio clic sulla manopola per aprire il menu **Babystep Z** (Fig. 5), ruotare lentamente la manopola per regolare con precisione l'altezza di stampa piattaforma, osservare la distanza dall'ugello al letto, fino a quando la distanza non risulta ottimale (Fig. 6).
- **Passaggio 5.** Attendi che la stampa sia terminata (Fig 7), quindi attendi che il piano caldo si raffreddi (Fig 8), quindi rimuovi l'oggetto stampato dal piano caldo (Fig 9).
![](./Operation/firstprint.png)

#### Stampa un file di prova a più colori
###### [![](https://img.youtube.com/vi/iddKadfrdjw/0.jpg)](https://www.youtube.com/watch?v=iddKadfrdjw)
I passaggi per la stampa multicolore e per la stampa a colore singolo sono sostanzialmente gli stessi, ma prima di iniziare la stampa, estrudere alcuni filamenti da tutti gli estrusori per verificare che l'hot end funzioni normalmente.
- **Passaggio 1.** Inserire la scheda SD nella presa per scheda SD sulla stampante.
- **Passaggio 2.** Riscalda l'ugello ed estrudi del filamento. **Prepara >>Filamento: *Preriscalda ugello: 200* -> *Estrusore: Tutto* -> *Carica lentamente***.
- **Passaggio 3.** Fai clic sull'ICONA "Stampa" sul pannello di controllo e scegli ***M4_4CTest.gcode***, fai clic sulla manopola per avviare la stampa.
- **Passaggio 4.** Regola con precisione la distanza dall'ugello al letto.
- **Passaggio 5.** Attendi il completamento della stampa.

-----
### :fireworks: Congratulazioni!
Dopo aver stampato i primi lavori, hai una conoscenza di base di come funziona la stampante 3d. Successivamente, puoi stampare altri file di prova o tagliare il tuo modello 3D e utilizzare la macchina per stamparlo.
Si consiglia di scaricare e installare il software di slicing e di leggere la guida utente del software di slicing per sapere come utilizzarlo. Per i dettagli, fare riferimento al [:book: **Guida allo slicing**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/4.Slicing).