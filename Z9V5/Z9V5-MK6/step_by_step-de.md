[LCD_MENU]: https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/LCDMENU_Description.md
[PRUSA_SLICER]: https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer
[VIDEO_POWERON]: https://github.com/ZONESTAR3D/Z9/assets/29502731/02fa8e57-a292-4aa5-bb7b-eaa703e3fc1b
[VIDEO_BEDLEVEL]: https://youtu.be/jNf98S0u2VQ
[VIDEO_LOADFILAMENT]: https://youtu.be/1rr4dXRxKc4

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
## Schritt für Schritt Anleitung
Kurz gesagt, von dem Moment an, an dem Sie das Gerät erhalten haben, bis zu dem Moment, an dem Sie Ihre eigene 3D-Modelldatei drucken können, sind insgesamt 5 Schritte erforderlich: **Installation – Nivellieren des Bettes – Laden von Filamenten – Drucken der Test-Gcode-Datei – Schneiden und Drucken Sie Ihre eigene 3D-Datei**.
#### Installation
[![](https://img.youtube.com/vi/pdr8nLl3T3w/0.jpg)](https://www.youtube.com/watch?v=pdr8nLl3T3w)
#### Basic Operations
[![](https://img.youtube.com/vi/GrCOZ4ADHeA/0.jpg)](https://www.youtube.com/watch?v=GrCOZ4ADHeA)

### <a id ="a1">Schritt 1. Installation</a>
- 1.1 **Installation**. Weitere Informationen finden Sie im [:book: **Installationshandbuch**](./1.Installation/Installation.md) und im [:clapper: **Installationsvideo-Tutorial**](https://youtu.be/pdr8nLl3T3w). Schließen Sie die Installation der Maschine ab.
- 1.2 **Verkabelung**. Bei der Verkabelung wird grundsätzlich der Stecker in die entsprechende Steckdose gesteckt. Sie müssen darauf achten, **sicherzustellen, dass die Anschlüsse richtig eingesteckt sind**, insbesondere bei den 2PIN-Docking-Buchsen. Darüber hinaus ist bei der Verkabelung des Druckkopfes (Hot End) zu beachten, dass es mehrere Buchsen gleicher, aber unterschiedlicher Farbe gibt, bitte achten Sie darauf, diese entsprechend der Farbe der Buchse zu stecken.
- 1.3 **Einschalten**. Wenn die Verkabelung abgeschlossen ist, können Sie [:clapper: **Z9V5 einschalten**][VIDEO_POWERON]. Bitte beachten Sie insbesondere, dass der Z9V5 über 2 Netzschalter verfügt. Der eine ist der ***Wechselstromschalter*** (der rote Schalter auf der Rückseite der Maschine) und der andere ist der ***Gleichstromschalter*** (ein runder Druckknopfschalter aus Metall an der Vorderseite des Maschinensteuerkastens). Sie müssen zuerst den AC-Schalter einschalten und dann den DC-Schalter etwa 5 Sekunden lang **drücken und gedrückt halten**, um Z9V5 einzuschalten.
- 1.4 **Einfach testen**. Nach dem Einschalten können Sie das Menü auf dem LCD-Bildschirm bedienen ([:book: **LCD-Menübeschreibung**](./2.Operation/LCDMENU_Description.md)), um zu überprüfen, ob das Gerät normal funktioniert. Normalerweise umfasst dies mehrere Schritte:
   - 1.4.1 **Vorbereiten>>Auto Home>>Home All**. Dieser Schritt dient dazu, den Druckkopf des Geräts zum Ursprung zurückzukehren.
   - 1.4.2 **Vorbereiten>>Temperatur>>PLA vorheizen**. In diesem Schritt wird das heiße Ende überprüft und das heiße Bett kann normal erhitzt werden. Wenn in diesem Schritt die Temperatur der Düse 60 Grad übersteigt, sollten Sie sehen, wie sich ein Lüfter auf der rechten Seite des Druckkopfs (heißes Ende) dreht , das ist der Hot-End-Lüfter.
   - 1.4.3 **Vorbereiten>>Temperatur>>Lüftergeschwindigkeit:**. Nachdem Sie den Knopf gedrückt und die Lüftergeschwindigkeit eingestellt haben (auf 255 eingestellt), sollten Sie nun auch den Lüfter (auf der linken Seite für M4V6-Hotend) hochdrehen können.
   Nachdem diese 3 Schritte grundsätzlich festgestellt wurden, dass die Maschine normal funktioniert, können Sie mit den folgenden Schritten fortfahren. Wenn Sie feststellen, dass ein Teil nicht ordnungsgemäß funktioniert, überprüfen Sie bitte die Verkabelung noch einmal oder lesen Sie [:clapper: **Video-Tutorial zum automatischen Testen von Maschinen**](https://youtu.be/Mf92BlmKA0A), um eine automatische Maschine zu testen testen.

### <a id ="a2">Schritt 2. Das Bett nivellieren</a>
Bevor Sie mit dem Drucken beginnen, müssen Sie eine einfache Bettnivellierung durchführen, um die Höhe zwischen der Düse und dem Bett (Druckplattform) einzustellen, damit das Filament gut auf dem Bett haften kann. Weitere Informationen finden Sie unter [:clapper: **Video-Tutorial zur Bettnivellierung**][VIDEO_BEDLEVEL].

### <a id ="a3">Schritt 3. Filamente laden</a>
Sehen Sie sich dieses [:clapper: Video-Tutorial][VIDEO_LOADFILAMENT] an, um alle 4 Filamente in die Extruder und das heiße Ende zu laden.
#### :warning: ACHTUNG BITTE :warning:
1. **Sie müssen alle 4 Filamente am heißen Ende laden, unabhängig davon, ob Sie ein- oder mehrfarbige 3D-Drucke drucken.**
2. **Stellen Sie sicher, dass die Filamente bis zum unteren Ende des heißen Endes geladen wurden, andernfalls kann es zu einer Blockierung des heißen Endes kommen.**

### <a id ="a4">Schritt 4. Test-Gcode-Datei drucken</a>
FDM-3D-Drucker können nur Gcode-Dateien erkennen. Sie müssen die Gcode-Dateien auf die SD-Karte kopieren, die SD-Karte in den SD-Kartensteckplatz des 3D-Druckers einstecken und dann mit dem Drucken beginnen.
Da es sich beim Z9V5Pro um einen 3D-Drucker mit 4 Extrudern handelt, empfehlen wir Ihnen, ein einfarbiges 3D-Modell und ein 4-Farben-3D-Modell zu drucken, um zu testen, ob die Maschine ordnungsgemäß funktioniert.
#### Drucken Sie einfarbige 3D-Drucke
- **Gcode-Datei vorbereiten**. Suchen Sie die Datei **xyz_cube.gcode** auf Ihrer SD-Karte oder [:arrow_down: klicken Sie hier, um sie herunterzuladen](./3.Test_gcode/xyz_cube.zip), entpacken Sie sie auf Ihrem PC und kopieren Sie dann den **xyz_cube .gcode** auf die SD-Karte übertragen, stecken Sie die SD-Karte in den SD-Anschluss des Geräts.
- **Drucken von SD-Karte**. Bewegen Sie den Cursor auf das Element **Drucken** auf dem LCD-Bildschirm, klicken Sie auf den Knopf und wählen Sie die Datei **xyz_cube** aus. Klicken Sie auf den Knopf, um den Druck zu starten.
- **Düsenhöhe fein einstellen**. Warten Sie, bis sich die Düse und das Heizbett erwärmt haben. Wenn Sie mit dem Drucken der ersten Schicht beginnen, doppelklicken Sie auf den Knopf des LCD-Bildschirms und stellen Sie den Abstand von der Düse zum Bett fein ein (Düse ist etwa 0,4 mm höher als der Aufkleber). Warten Sie, bis der Druckvorgang abgeschlossen ist fertig.
#### Drucken Sie 4-farbige 3D-Drucke
- **Gcode-Datei vorbereiten**. Suchen Sie die Datei **M4_4CTest.gcode** auf Ihrer SD-Karte oder [:arrow_down: klicken Sie hier, um sie herunterzuladen](./3.Test_gcode/M4_4CTest.zip), entpacken Sie sie auf Ihrem PC und kopieren Sie dann die Datei **M4_4CTest .gcode** auf die SD-Karte übertragen, stecken Sie die SD-Karte in den SD-Anschluss des Geräts.
- **Drucken von SD-Karte**. Bewegen Sie den Cursor auf das Element **Drucken** auf dem LCD-Bildschirm, klicken Sie auf den Knopf und wählen Sie die Datei **M4_4CTest**. Klicken Sie auf den Knopf, um den Druck zu starten.
- **Düsenhöhe fein einstellen**. Warten Sie, bis sich die Düse und das Heizbett erwärmt haben. Wenn Sie mit dem Drucken der ersten Schicht beginnen, doppelklicken Sie auf den Knopf des LCD-Bildschirms und stellen Sie den Abstand von der Düse zum Bett fein ein (Düse ist etwa 0,4 mm höher als der Aufkleber). Warten Sie, bis der Druckvorgang abgeschlossen ist fertig.

### <a id ="a5">Schritt 5. Schneiden Sie Ihr eigenes 3D-Modell und drucken Sie es aus</a>
Bevor Sie Ihre eigenen 3D-Modelle drucken, müssen Sie die 3D-Modelldatei (eine Datei im stl/obj/AMF-Format, die [aus dem Internet heruntergeladen wurde] (#a6) oder eine eigene Zeichnung) in eine GCode-Datei konvertieren. Dieser Vorgang wird < genannt u>"**Schneiden**"</u>.
- Zuerst müssen Sie die Slicing-Software herunterladen und auf Ihrem Computer installieren und die Parameter Ihrer Maschine in der Slicing-Software einstellen oder die voreingestellte Datei Ihrer Maschine laden, die vom Hersteller des 3D-Druckers festgelegt wurde.
- Als nächstes müssen Sie die Slicing-Software ausführen und möglicherweise auch einige Parameter entsprechend den Eigenschaften Ihrer 3D-Modelldatei festlegen und dann das Slicing ausführen.
- Nachdem das Schneiden abgeschlossen ist, kopieren Sie die generierte Gcode-Datei auf die SD-Karte und folgen Sie den [:point_right:Schritt 4](#a4), um sie mit Ihrem 3D-Drucker auszudrucken.
#### *PrusaSlicer* ist die von uns empfohlene Slicing-Software. Bitte besuchen Sie [:point_right:here][PRUSA_SLICER], um die PrusaSlicer-Software herunterzuladen und zu installieren und das Benutzerhandbuch zu lesen.
:warning: **ACHTUNG BITTE** :warning:    
Standardmäßig ist der Z9V5Pro-MK6 mit einem M4V6-Hotend (4-IN-1-OUT-Mischfarbe) ausgestattet. Bitte achten Sie beim Schneiden darauf, die Druckervoreinstellung (Z9 + M4 Hotend) auszuwählen.

----
### <a id ="a6">Berühmte Websites zum kostenlosen Herunterladen von 3D-Modellen</a>
- [thingiverse](https://www.thingiverse.com/)  
- [printables](https://www.printables.com/)  
- [youmagine](https://www.youmagine.com/)   

----