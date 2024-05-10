
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
## Bedienerführung
Bevor Sie mit dem Drucken beginnen, müssen Sie das heiße Bett nivellieren (den Abstand zwischen der Düse und der Druckplattform fein einstellen) und die Filamente in die Extruder und das heiße Ende laden.
## Das heiße Bett nivellieren
#### :warning: Bei einem FDM-3D-Drucker ist der Abstand zwischen der Düse und dem heißen Bett beim Drucken der ersten Schicht sehr wichtig. Ist der Abstand zu gering, können die Filamente nicht aus der Düse fließen und sogar die Düse und das heiße Bett beschädigen. Wenn der Abstand zu groß ist, können die Filamente nicht auf dem heißen Bett kleben, die nächsten Schichten können nicht richtig gestapelt werden und es kommt zu Druckfehlern.
###### [![](https://img.youtube.com/vi/jNf98S0u2VQ/0.jpg)](https://www.youtube.com/watch?v=jNf98S0u2VQ)
- **Schritt 1.** Schalten Sie den 3D-Drucker ein und führen Sie dann ***Prepare>>Auto Home>>Home All*** im LCD-MENÜ aus, warten Sie, bis das Hotend in die HOME-Position geht.
- **Schritt 2.** Ziehen Sie die Handmuttern unter dem Bett fest, um das Bett in die unterste Position zu bewegen (Abb. 1).
- **Schritt 3.** Führen Sie ***Prepare>> Bed leveling>> Point 1*** auf dem Bedienfeld aus (Abb. 2), die Düse geht zu den Ecken des Bettes, lösen Sie die Handmuttern unter dem Heizbett (Abb. 3) und lassen Sie die Düse fast das Brutbett berühren (Abb. 4). Fahren Sie mit ***Point 2/3/4*** fort, bis alle vier Ecken geebnet sind.
- **Schritt 4.** Wiederholen Sie Schritt 3 und machen Sie 2–3 Runden, bis alle vier Ecken auf der gleichen Höhe sind.
![](./Operation/levelbed.png)

-----
### Filamente laden
###### [![](https://img.youtube.com/vi/1rr4dXRxKc4/0.jpg)](https://www.youtube.com/watch?v=1rr4dXRxKc4)
Dieser Drucker ist mit vier Extrudern und einem 4-IN-1-OUT-Farbmisch-Hot-End ausgestattet. Die Extruder und das Hot End sind durch eine Filamentführung (PTFE-Schlauch) verbunden. ***Vor dem Drucken müssen Sie alle 4 Filamente in die Extruder laden und sie unten in das heiße Ende einführen.***
- **Schritt 1.** Führen Sie auf dem Bedienfeld ***Prepare>>Auto Home>>Home All*** aus und führen Sie dann ***Prepare>>Temperature>> Preheat PLA*** aus. Wartende Düsentemperatur erreicht 190 ℃ (Abb. 1).
- **Schritt 2.** Schneiden Sie den Kopf des Filaments mit einer Diagonalzange ab (Abb. 2), drücken Sie dann auf den Griff des Extruders Nr. 1 und führen Sie das Filament ein. Drücken Sie das Filament, bis Sie das Filament im PTFE sehen können Anleitung (Abb. 3). Drehen Sie das Zahnrad von Extruder Nr. 1 (Abb. 4) und beobachten Sie das Filament, bis es unten in das heiße Ende gelangt.
- **Schritt 3.** Verwenden Sie die gleiche Methode wie in Schritt 2, um die Filamente in Extruder Nr. 2 bis Extruder Nr. 4 zu laden, und beobachten Sie die Filamente, bis sie die Unterseite des heißen Endes erreichen.
- **Schritt 4.** Drehen Sie langsam das Zahnrad von Extruder Nr. 1 bis Extruder Nr. 4 nacheinander und beobachten Sie die Düse, bis Sie sehen können, wie das Filament aus der Düse herausfließt (Abb. 5).
![](./Operation/loadfilament.png)

-----
### Drucken Sie Ihre „Hellow World“-Werke aus
#### Drucken Sie eine einzelne Farbtestdatei
###### [![](https://img.youtube.com/vi/NbVy8NjKt_s/0.jpg)](https://www.youtube.com/watch?v=NbVy8NjKt_s)
- **Schritt 1.** Stecken Sie die SD-Karte in den SD-Kartensteckplatz am Drucker (Abb. 1).
- **Schritt 2.** Klicken Sie auf dem Bedienfeld auf das Symbol ***Print*** und wählen Sie ***xyz_cube.gcode*** (Abb. 2). Klicken Sie auf den Knopf, um mit dem Drucken zu beginnen.
- **Schritt 3.** Warten Sie, bis das Hotend und das Hotbed die eingestellte Temperatur erreicht haben (Abb. 3), die Düse kehrt zur Ursprungsposition zurück und bewegt sich dann über die Druckplattform und extrudiert das Filament mithilfe einer Pinzette um den Ausflussfaden zu entfernen (Abb. 4).
- **Schritt 4.** Wenn sich die Düse zum heißen Bett bewegt und mit dem Drucken beginnt, doppelklicken Sie auf den Knopf, um das Menü ***Babystep Z*** zu öffnen (Abb. 5). Drehen Sie den Knopf langsam, um die Höhe der Druckplattform fein einzustellen Beobachten Sie den Abstand von der Düse zum Bett, bis der Abstand gut passt (Abb. 6).
- **Schritt 5.** Warten Sie, bis der Druckvorgang abgeschlossen ist (Abb. 7), warten Sie, bis das Heizbett abgekühlt ist (Abb. 8), und entfernen Sie dann das gedruckte Objekt vom Heizbett (Abb. 9).
![](./Operation/firstprint.png)

#### Drucken Sie eine mehrfarbige Testdatei
###### [![](https://img.youtube.com/vi/iddKadfrdjw/0.jpg)](https://www.youtube.com/watch?v=iddKadfrdjw)
Die Schritte für den Mehrfarbendruck und den Einzelfarbendruck sind grundsätzlich gleich, aber bevor Sie mit dem Drucken beginnen, extrudieren Sie bitte einige Filamente aus allen Extrudern, um sicherzustellen, dass das heiße Ende normal funktioniert.
- **Schritt 1.** Stecken Sie die SD-Karte in den SD-Kartensteckplatz am Drucker.
- **Schritt 2.** Erhitzen Sie die Düse und extrudieren Sie etwas Filament. **Prepare>>Filament: *Preheat Nozzle: 200* -> *Extruder: All* -> *Load Slowly***.
- **Schritt 3.** Klicken Sie auf dem Bedienfeld auf das Symbol „Drucken“ und wählen Sie ***M4_4CTest.gcode***. Klicken Sie auf den Knopf, um mit dem Drucken zu beginnen.
- **Schritt 4.** Passen Sie den Abstand von der Düse zum Bett fein an.
- **Schritt 5.** Warten Sie, bis der Druckvorgang abgeschlossen ist

-----
### :fireworks: Herzlichen Glückwunsch!
Nachdem Sie die ersten Werke gedruckt haben, haben Sie ein grundlegendes Verständnis für die Funktionsweise des 3D-Druckers. Anschließend können Sie weitere Testdateien ausdrucken oder Ihr eigenes 3D-Modell in Scheiben schneiden und mit dem Gerät ausdrucken.
Es wird empfohlen, die Slicing-Software herunterzuladen und zu installieren und das Benutzerhandbuch der Slicing-Software zu lesen, um zu erfahren, wie man sie verwendet. Einzelheiten finden Sie im [:book: **Schnittanleitung**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/4.Slicing).