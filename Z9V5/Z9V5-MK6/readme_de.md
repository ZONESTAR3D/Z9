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
# Benutzerhandbuch für den ZONESTAR Z9V5Pro-MK6 3D-Drucker

----
## :warning: BITTE ACHTUNG
#### :loudspeaker: Bevor Sie das Gerät verwenden, lesen Sie bitte [:book:"Vorsichtsmaßnahmen für die Verwendung von M4V6"][M4V6_PRECAUTION] sorgfältig durch.
#### :loudspeaker: Es müssen 4 Filamente gleichzeitig auf das M4V6-Hotend geladen werden. Bei falscher Bedienung kann das Mischfarben-Hotend blockiert werden. Wenn die Blockierung des heißen Endes auf eine fehlerhafte Bedienung zurückzuführen ist, fällt sie nicht unter die Garantie. Informationen zum Laden von Filamenten finden Sie in [:book: dieser Anleitung][Z9V5MK6_LOADFILAMENT].
#### :loudspeaker: Wenn Sie ein Anfänger im Umgang mit 3D-Druckern sind, lesen Sie bitte sorgfältig die [:book: Schritt-für-Schritt-Anleitung][Z9V5MK6_STEPBYSTEP] und befolgen Sie die erforderlichen Schritte.
- [:book: **Vorsichtsmaßnahmen für die Verwendung von M4V6**][M4V6_PRECAUTION]
- [:book: **So laden Sie Filamente richtig**][Z9V5MK6_LOADFILAMENT]
- [:book: **Schritt-für-Schritt-Anleitung**][Z9V5MK6_STEPBYSTEP]

------
## :book: Inhalt
- [**Installationsanleitung**](#A1)
- [**Bedienungsanleitung**](#A2)
- [**Gcode-Dateien testen**](#A3)
- [**Slicing-Software**](#A4)
- [**Firmware**](#A5)
- [**Fehlerbehebung**](#A6)
- [**Teile-STL-Dateien drucken**](#A7)
- [**Optionale Upgrade-Funktionen**](#A8)

-----
## <a id="A1"> 1. Installationsanleitung </a>
Bitte beachten Sie zunächst die folgenden Dokumente und Videos, um die Installation und Verkabelung der Maschine abzuschließen.
### Installation
- [:book: Installationshandbuch Online-Dokument](./1.Installation/Installation.md)
- [:blue_book: Installationsanleitung PDF-Datei](./1.Installation/Installation.pdf)
- [:clapper: Installationsanleitung, Video-Tutorial](https://youtu.be/TGHUVzV1Pg4)
### Verkabelung
- [:book: Wiring Guide Online Document](./1.Installation/Wiring.md)
- [:blue_book: Verkabelungsanleitung PDF-Datei](./1.Installation/Wiring.pdf)
- [:art: Schaltplan](./1.Installation/Z9V5Pro_Wiring_Diagram.jpg)
- [:clapper: Video-Tutorial zur Verkabelung](https://youtu.be/tQQNLDOpdQU)

## <a id="A2"> 2. Bedienungsanleitung </a>
### **Einführung in das LCD-Bedienfeld**
Nachdem Sie die Installation und Verkabelung abgeschlossen haben, sehen Sie sich bitte die folgende Anleitung an, um zu erfahren, wie Sie das Bedienfeld (LCD-Bildschirm) verwenden und die Funktionen des LCD-Menüs im Allgemeinen verstehen.
- [:book: LCD Menu Online Document](./2.Operation/LCDMENU_Description.md)
- [:blue_book: LCD-Menü-PDF-Datei](./2.Operation/LCDMENU_Description.pdf)
#### **Drucken Sie Ihre ersten Werke**
Jetzt können Sie versuchen, Ihre „Hallo Wort“-Werke zu drucken. Bevor Sie mit dem Drucken beginnen, müssen Sie zunächst eine einfache Korrektur der Höhe des heißen Betts vornehmen (dies wird als „Bettnivellierung“ bezeichnet) und dann die Filamente in den Extruder laden (Bitte beachten Sie, dass Sie unabhängig von der Farbe Ihres Drucks alle 4 Filamente in die Extruder und das Hot-End laden müssen.) Als Nächstes können Sie die SD-Karte in das Gerät einlegen und auf der SD-Karte eine zu testende 3D-Modell-Gcode-Datei auswählen. Einzelheiten entnehmen Sie bitte den untenstehenden Dokumenten.   
- [:book: Operation Guide Online Document](./2.Operation/Operation.md)
- [:blue_book: Bedienungsanleitung im PDF-Format](./2.Operation/Operation.pdf)
#### :page_with_curl: Weitere Funktionen
Sie können auch die folgenden Dokumente lesen, um ein tieferes Verständnis des von Ihrem Gerät verwendeten Extruders (Hot-End und Druckkopf) sowie einiger erweiterter Funktionen des Geräts zu erlangen.  
- [:book: Anleitung zur Verwendung der Farbmischungsfunktion][LINK_MIX_FEATURE]
- [:Buch: M4V6 Hotend-Einführung][LINK_M4V6]
- [:book: Drucken vom PC](./2.Operation/PrintFromPC/readme.md)
- [:book: Gebrauchsanleitung für erweiterte Funktionen](./2.Operation/Advance_Features.md)

## <a id="A3"> 3. G-Code-Datei testen </a>
**:pencil: Was ist G-Code im 3D-Druck?**
Bei G-Code handelt es sich um Informationen oder Anweisungen, die ein 3D-Drucker benötigt, um ein dreidimensionales Objekt zu drucken. Dabei handelt es sich um die Sprache, die der 3D-Drucker verstehen kann. G-Code wird von Ihrer Slicing-Software generiert, indem eine Standard-3D-Modellierungsdatei wie STL, Objekt, AMF-Datei usw. übersetzt wird. :page_with_curl: [**Referenz 1**][GCODE_REF1] :page_with_curl: [**Referenz 2 **][GCODE_REF2]
Wir haben einige Test-Gcode-Dateien auf der SD-Karte gespeichert, um zu überprüfen, ob das Gerät ordnungsgemäß funktioniert, oder um zu demonstrieren, über welche Druckfunktionen dieses Gerät verfügt. Wenn Sie die Test-Gcode-Dateien nicht auf der SD-Karte finden können, laden Sie sie bitte von [:arrow_down: **hier**](./3.TestGcode/Test_gcode.zip) herunter.
- **xyz_cube.gcode**: Eine einfache Test-Gcode-Datei, mit der überprüft wird, ob die Maschine ordnungsgemäß funktioniert.
- **dog.gcode**: Eine klassische Druckqualitätstestdatei.
- **Vase.gcode**: Eine Testvase.
   - **GradientMix_Vase.gcode**: Eine Vase wie bei vase.gcode, aber mit aktivierter Funktion „Gradientenmix“.
   - **RandomMix_Vase.gcode**: Eine Vase wie bei vase.gcode, aber mit aktivierter Funktion „Zufallsmischung“.
- **M4_4CTest.gcode**: Eine Basis-4-Farben-Testdatei für 3D-Drucker mit einem M4-Hot-End.
- **M4_4C_BODY3D.gcode**: Eine größere 4-Farben-Testdatei.
- **16color_tower.gcode**: Eine Basis-16-Farbtestdatei, um das Ergebnis gemischter Filamente unterschiedlicher Farbe anzuzeigen.
- **level_test_310.gcode**: Eine Testdatei zur Überprüfung der Ebenheit des Hot-Bettes (ohne automatische Bettnivellierung).
- **level_test_310-G29.gcode**: Eine Testdatei zur Überprüfung der Ebenheit des Hot-Bettes (mit automatischer Bettnivellierung).
**[:arrow_down: Weitere Test-Gcode-Dateien herunterladen][M4_TEST_GCODE].**
 
## <a id="A4"> 4. Schneiden </a>
**[:pencil: Was ist Schneiden im 3D-Druck?](https://en.wikipedia.org/wiki/Slicer_(3D_printing))**
Ein Slicer ist eine Software zur Werkzeugweggenerierung, die in den meisten 3D-Druckverfahren zur Konvertierung eines 3D-Objektmodells in spezifische Anweisungen für den Drucker verwendet wird. Insbesondere die Konvertierung von einem Modell im STL-Format in Druckerbefehle im G-Code-Format bei der Herstellung von geschmolzenem Filament und anderen ähnlichen Prozessen.
- [:book:Slicer User Guide Online Document](./4.Slicing/readme.md)
- [:blue_book: Slicer-Benutzerhandbuch im PDF-Format](./4.Slicing/Slicing.pdf)

## <a id="A5"> 5. Firmware </a>
**:pencil: Was ist Firmware-Bin-Datei und Quellcode?**
Die Firmware-Bin-Datei ist der genaue Speicher, der in den eingebetteten Flash geschrieben wird.
Der Firmware-Quellcode ist der Kernbestandteil der Firmware. Unser Firmware-Quellcode basiert auf [**marlin**](https://www.marlinfw.org).
Sie können die Firmware-Bin-Datei oder den Quellcode über den folgenden Link herunterladen.
- [:arrow_down: Firmware-Bin-Datei][LINK_FIRMWARE]
- [:arrow_down: Firmware-Quellcode][LINK_SOURCECODE]

## <a id="A6"> 6. Fehlerbehebung </a>
Wenn Sie Probleme bei der Installation und Verwendung des Druckers haben, versuchen Sie bitte zunächst, eine Lösung im [:book: Online-Dokument zur Fehlerbehebung][LINK_TROUBLESHOOTING] zu finden. Wenn Sie dieses Problem nicht lösen können, kontaktieren Sie uns bitte per E-Mail (:email: support@zonestar3d.com).

## <a id="A7"> 7. Teile drucken </a>
Es gibt mehrere Komponenten der Maschine, die gedruckt werden, und wir haben auch einige Upgrades für Sie vorbereitet. Wenn Sie möchten, können Sie sie herunterladen, ausdrucken und dann auf Ihrem Computer installieren.

-----
## <a id="A8">Optionale Funktionen </a>
Wir haben einige optionale Funktionen für dieses Gerät eingeführt. Sie können diese Funktionen jederzeit nach Ihren Wünschen aktualisieren. Wenn Sie daran interessiert sind, lesen Sie bitte den Leitfaden zu optionalen Upgrade-Funktionen, um detailliertere Informationen zu erhalten.
- [:book: Leitfaden für optionale Upgrade-Funktionen, Online-Dokument][Z9V5MK6_OPTION]
- [:blue_book: Leitfaden für optionale Upgrade-Funktionen, PDF-Datei](./OptionalFeatures.pdf)