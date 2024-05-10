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
## Guía paso por paso
En una palabra, desde el momento en que recibe la máquina hasta el momento en que puede imprimir su propio archivo de modelo 3D, se requieren un total de 5 pasos: **Instalación - Nivelación de la cama - Cargar filamentos - Imprimir el archivo gcode de prueba - Cortar y Imprima su propio archivo 3D**.
#### Instalación (Igual que Z9V5-MK5)
[![](https://img.youtube.com/vi/pdr8nLl3T3w/0.jpg)](https://www.youtube.com/watch?v=pdr8nLl3T3w)
#### Operaciones básicas
[![](https://img.youtube.com/vi/GrCOZ4ADHeA/0.jpg)](https://www.youtube.com/watch?v=GrCOZ4ADHeA)
#### Impresión multicolor
[![](https://img.youtube.com/vi/iddKadfrdjw/0.jpg)](https://www.youtube.com/watch?v=iddKadfrdjw)

### <a id ="a1">Paso 1. Instalación</a>
- 1.1 **Instalación**. Consulte el [:book: **guía de instalación**](./1.Installation/Installation.md) y el [:clapper: **tutorial de instalación en vídeo**](https://youtu.be/pdr8nLl3T3w) para completar la instalación de la máquina.
- 1.2 **Cableado**. El proceso de cableado consiste básicamente en introducir el enchufe en el enchufe correspondiente. Lo que debe prestar atención es **asegurarse de que los conectores estén bien enchufados**, especialmente para los enchufes de acoplamiento de 2 pines. Además, para el cableado del cabezal de impresión (extremo caliente), tenga en cuenta que hay varios enchufes del mismo pero de diferentes colores; preste atención para enchufarlos según el color del enchufe.
- 1.3 **Encendido**. Cuando se complete el cableado, puede [:clapper: **encender Z9V5**][VIDEO_POWERON]. Tenga en cuenta en particular que el Z9V5 tiene 2 interruptores de alimentación. uno es ***interruptor de CA*** (el interruptor rojo en la parte posterior de la máquina) y otro es ***interruptor de CC*** (un interruptor de botón redondo de metal en la parte frontal de la caja de control de la máquina), primero debe encender el interruptor de CA y luego **mantener presionado** el interruptor de CC durante aproximadamente 5 segundos para encender Z9V5.
- 1.4 **Simplemente prueba**. Después del encendido, puede operar el menú en la pantalla LCD ([:book: **LCD Menu description**](./2.Operation/LCDMENU_Description.md)) para verificar si la máquina puede funcionar normalmente. Normalmente esto implica varios pasos:
   - 1.4.1 **Preparar>>Inicio automático>>Inicio todo**. Este paso es para hacer que el cabezal de impresión de la máquina regrese al origen.
   - 1.4.2 **Preparar>>Temperatura>>Precalentar PLA**. Este paso es para verificar que el extremo caliente y la cama caliente se puedan calentar normalmente. En este paso, cuando la temperatura de la boquilla excede los 60 grados, debería ver un ventilador en el lado derecho del cabezal de impresión (extremo caliente) girar. , este es el ventilador de refrigeración del extremo caliente.
   - 1.4.3 **Preparar>>Temperatura>>Velocidad del VENTILADOR:**. Después de presionar la perilla y configurar la velocidad del ventilador (establecida en 255), ahora también debería poder subir el ventilador (en el lado izquierdo para el hotend M4V6).
   Después de estos 3 pasos, básicamente se determina que la máquina está funcionando normalmente, puede continuar con los siguientes pasos. Si descubre que alguna pieza no funciona correctamente, verifique nuevamente el cableado o consulte [:clapper: **vídeotutorial de prueba automática de la máquina**](https://youtu.be/Mf92BlmKA0A) para realizar una máquina automática. pruebas.

### <a id ="a2">Paso 2. Nivelar la cama</a>
Antes de comenzar a imprimir, debe realizar una simple nivelación de la cama para establecer la altura entre la boquilla y la cama (plataforma de impresión), de modo que el filamento se pueda pegar bien en la cama. Consulte [:clapper: **Videotutorial de nivelación de la cama**][VIDEO_BEDLEVEL] para hacerlo.

### <a id ="a3">Paso 3. Cargar filamentos</a>
Consulte este [:clapper: vídeo tutorial][VIDEO_LOADFILAMENT] para cargar los 4 filamentos en las extrusoras y el extremo caliente.
#### :warning: ATENCIÓN POR FAVOR :warning:
1. **Necesita cargar los 4 filamentos en el extremo caliente, independientemente de lo que imprima en un color o en impresiones 3D de varios colores.**
2. **Asegúrese de que los filamentos se hayan cargado hasta la parte inferior del extremo caliente; de lo contrario, podría bloquear el extremo caliente.**

### <a id ="a4">Paso 4. Imprima el archivo gcode de prueba</a>
Las impresoras 3D FDM solo pueden reconocer archivos gcode; debe copiar los archivos gcode a la tarjeta SD, insertar la tarjeta SD en el zócalo para tarjetas SD de la impresora 3D y luego comenzar a imprimir.
Dado que Z9V5Pro es una impresora 3D con 4 extrusoras, le sugerimos que imprima un modelo 3D de un color y un modelo 3D de 4 colores para probar si la máquina funciona correctamente.
#### Imprimir impresiones 3D de un color
##### [:clapper: vídeo tutorial][VIDEO_PRINT1C]
- **Preparar archivo gcode**. Localice el archivo **xyz_cube.gcode** de su tarjeta SD o [:arrow_down: haga clic aquí para descargarlo](./3.Test_gcode/xyz_cube.zip) y descomprímalo en su PC, y luego copie el archivo **xyz_cube .gcode** a la tarjeta SD, conecte la tarjeta SD al conector SD de la máquina.
- **Imprimir desde tarjeta SD**. Mueva el cursor al elemento **Imprimir** en la pantalla LCD y haga clic en la perilla y elija el archivo **xyz_cube**, haga clic en la perilla para comenzar a imprimir.
- **Ajuste la altura de la boquilla**. Espere a que se calienten la boquilla y la cama, y cuando comience a imprimir la primera capa, haga doble clic en la perilla de la pantalla LCD y ajuste la distancia desde la boquilla hasta la cama (la boquilla es más alta que la etiqueta adhesiva aproximadamente 0,4 mm), espere hasta que finalice la impresión. finalizado.
#### Imprimir impresiones 3D en 4 colores
##### [:clapper: vídeo tutorial][VIDEO_PRINT4C]
- **Preparar archivo gcode**. Localice el archivo **M4_4CTest.gcode** de su tarjeta SD o [:arrow_down: haga clic aquí para descargarlo](./3.Test_gcode/M4_4CTest.zip) y descomprímalo en su PC, y luego copie el archivo **M4_4CTest .gcode** a la tarjeta SD, conecte la tarjeta SD al conector SD de la máquina.
- **Imprimir desde tarjeta SD**. Mueva el cursor al elemento **Imprimir** en la pantalla LCD, haga clic en la perilla y elija el archivo **M4_4CTest**, haga clic en la perilla para comenzar a imprimir.
- **Ajuste la altura de la boquilla**. Espere a que se calienten la boquilla y la cama, y cuando comience a imprimir la primera capa, haga doble clic en la perilla de la pantalla LCD y ajuste la distancia desde la boquilla hasta la cama (la boquilla es más alta que la etiqueta adhesiva aproximadamente 0,4 mm), espere hasta que finalice la impresión. finalizado.

### <a id ="a5">Paso 5. Corta tu propio modelo 3D e imprímelo</a>
Antes de imprimir sus propios modelos 3D, necesita convertir el archivo del modelo 3D (un archivo de formato stl/obj/AMF [descargado de Internet](#a6) o dibujado por usted mismo) a un archivo gcode, este proceso se llama < u>"**rebanar**"</u>.
- En primer lugar, debe descargar el software de corte e instalarlo en su computadora, y configurar los parámetros de su máquina en el software de corte o cargar el archivo preestablecido de su máquina establecido por el fabricante de la impresora 3D.
- A continuación, debe ejecutar el software de corte y es posible que también deba establecer algunos parámetros de acuerdo con las características de su archivo de modelo 3D y luego ejecutar el corte.
- Una vez finalizado el corte, copie el archivo gcode generado en la tarjeta SD y siga el [:point_right:Stpe 4](#a4) para imprimirlo en su impresora 3D.
#### *PrusaSlicer* es el software de corte que recomendamos; consulte [:point_right:aquí][PRUSA_SLICER] para descargar e instalar el software PrusaSlicer y leer la guía del usuario.
:warning: **ATENCIÓN POR FAVOR** :warning:     
El Z9V5Pro-MK6 predeterminado está equipado con un hotend M4V6 (mezcla de colores 4 en 1, salida), preste atención para elegir el ajuste preestablecido de la impresora (Z9 + M4 Hotend) al cortar.

----
### <a id ="a6">Sitios web famosos de descarga gratuita de modelos 3D</a>
- [thingiverse](https://www.thingiverse.com/)  
- [printables](https://www.printables.com/)  
- [youmagine](https://www.youmagine.com/)   

----
