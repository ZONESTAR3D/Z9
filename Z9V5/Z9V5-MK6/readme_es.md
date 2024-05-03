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
# Guía del usuario para la impresora 3D ZONESTAR Z9V5Pro-MK6

----
## :warning: ATENCIÓN POR FAVOR
#### loudspeaker: Antes de utilizar la máquina, lea atentamente [:book:"Precauciones para el uso de M4V6"][M4V6_PRECAUTION].
#### loudspeaker: Debe cargar 4 filamentos en el hotend M4V6 simultáneamente, el funcionamiento incorrecto puede bloquear el hotend de mezcla de colores. Si el bloqueo del extremo caliente es causado por una operación incorrecta, no está cubierto por la garantía. Para saber cómo cargar filamentos, consulte [:book: esta guía][Z9V5MK6_LOADFILAMENT].
#### loudspeaker: Si es principiante en el uso de impresoras 3D, lea atentamente la [Guía paso a paso] [Z9V5MK6_STEPBYSTEP] y siga los pasos a seguir.
- [:book: **Precauciones al usar M4V6**][M4V6_PRECAUTION]
- [:book: **Cómo cargar filamentos correctamente**][Z9V5MK6_LOADFILAMENT]
- [:book: **Guía paso a paso**][Z9V5MK6_STEPBYSTEP]
<!-- - [:blue_book: Archivo PDF de la guía paso a paso](./step_by_step.pdf) -->

------
## :book: Contenido
- [**Guía de instalación**](#A1)
- [**Guía de operación**](#A2)
- [**Probar archivos gcode**](#A3)
- [**Software de corte**](#A4)
- [**Firmware**](#A5)
- [**Solución de problemas**](#A6)
- [**Imprimir archivos stl de piezas**](#A7)
- [**Funciones de actualización opcionales**](#A8)

-----
## <a id="A1"> 1. Guía de instalación </a>
Primero, consulte los siguientes documentos y vídeos para completar la instalación y el cableado de la máquina.
### Instalación
- [:book: Documento en línea de la guía de instalación](./1.Installation/Installation.md)
- [:blue_book: archivo PDF de la guía de instalación](./1.Installation/Installation.pdf)
- [:clapper: Videotutorial de la guía de instalación](https://youtu.be/TGHUVzV1Pg4)
### Alambrado
- [:book: Documento en línea de la guía de cableado](./1.Installation/Wiring.md)
- [:blue_book: Archivo PDF de la guía de cableado](./1.Installation/Wiring.pdf)
- [:art: Diagrama de cableado](./1.Installation/Z9V5Pro_Wiring_Diagram.jpg)
- [:clapper: Videotutorial de cableado](https://youtu.be/tQQNLDOpdQU)

## <a id="A2"> 2. Guía de operación </a>
### **Introducción al panel de control LCD**
Después de completar la instalación y el cableado, consulte la siguiente guía para saber cómo utilizar el panel de control (pantalla LCD) y comprender las funciones del menú LCD en general.
- [:book: Documento en línea del menú LCD](./2.Operation/LCDMENU_Description.md)
- [:blue_book: archivo PDF del menú LCD](./2.Operation/LCDMENU_Description.pdf)
#### **Imprime tus primeros trabajos**
Ahora puedes intentar imprimir tus trabajos de "Hola palabra", antes de comenzar a imprimir, primero debes hacer una simple corrección a la altura de la cama caliente (se llama "nivelación de la cama"), y luego cargar los filamentos en el extrusor. (tenga en cuenta que, independientemente del color de su impresión, debe cargar los 4 filamentos en las extrusoras y en el extremo caliente). A continuación, puede insertar la tarjeta SD en la máquina y elegir un archivo gcode de modelo 3D de prueba en la tarjeta SD. Para obtener más información, consulte los documentos a continuación.
- [:book: Documento en línea de la guía de operación](./2.Operation/Operation.md)
- [:blue_book: archivo PDF de la guía de operación](./2.Operation/Operation.pdf)
#### :page_with_curl: Más funciones
También puede leer los siguientes documentos para obtener una comprensión más profunda del extrusor (extremo caliente y cabezal de impresión) utilizado por su máquina, así como algunas funciones avanzadas de la máquina.
- [:book: Guía de uso de la función Mezclar colores][LINK_MIX_FEATURE]
- [:book: Introducción al hotend M4V6][LINK_M4V6]
- [:book: Imprimir desde PC](./2.Operation/PrintFromPC/readme.md)
- [:book: Guía de uso de funciones avanzadas](./2.Operation/Advance_Features.md)

## <a id="A3"> 3. Pruebe el archivo de código G </a>
**:pencil: ¿Qué es el código G en la impresión 3D?**
El código G es información o instrucciones que la impresora 3D requiere para imprimir un objeto tridimensional, es el lenguaje que la impresora 3D puede entender. Su software de corte genera G-Code, traduciendo un archivo de modelado 3D estándar como STL, objeto, archivo AMF, etc. :page_with_curl: [**Referencia 1**][GCODE_REF1] :page_with_curl: [**Referencia 2**][GCODE_REF2]     
Almacenamos algunos archivos gcode de prueba en la tarjeta SD, para ayudar a verificar si la máquina estaba funcionando correctamente o para demostrar qué funciones de impresión tiene esta máquina. Si no puede encontrar los archivos gcode de prueba en la tarjeta SD, descárguelos desde [:arrow_down: **aquí**](./3.TestGcode/Test_gcode.zip).
- **xyz_cube.gcode**: un archivo gcode de prueba simple utilizado para verificar si la máquina estaba funcionando bien.
- **dog.gcode**: un archivo de prueba de calidad de impresión clásico.
- **Vase.gcode**: Un jarrón de prueba.
   - **GradientMix_Vase.gcode**: un jarrón igual que vase.gcode pero con la función "mezcla de degradado" habilitada.
   - **RandomMix_Vase.gcode**: Un jarrón igual que vase.gcode pero habilitada la función de "mezcla aleatoria".
- **M4_4CTest.gcode**: un archivo de prueba base de 4 colores para impresora 3D con un extremo caliente M4.
- **M4_4C_BODY3D.gcode**: un archivo de prueba de 4 colores más grande.
- **16color_tower.gcode**: un archivo de prueba de color base 16 para mostrar el resultado de la mezcla de filamentos de diferentes colores.
- **level_test_310.gcode**: un archivo de prueba utilizado para verificar la planitud de la cama caliente (sin nivelación automática de la cama).
- **level_test_310-G29.gcode**: un archivo de prueba utilizado para verificar la planitud de la cama caliente (con nivelación automática de la cama).
**[:arrow_down: descargar más archivos gcode de prueba][M4_TEST_GCODE].**
 
## <a id="A4"> 4. Cortar </a>
**[:pencil: ¿Qué es el corte en impresión 3D?](https://en.wikipedia.org/wiki/Slicer_(3D_printing))**
Una cortadora es un software de generación de trayectorias de herramientas que se utiliza en la mayoría de los procesos de impresión 3D para la conversión de un modelo de objeto 3D en instrucciones específicas para la impresora. En particular, la conversión de un modelo en formato STL a comandos de impresora en formato de código g en la fabricación de filamentos fundidos y otros procesos similares.
- [:book:Documento en línea de la Guía del usuario de Slicer](./4.Slicing/readme.md)
- [:blue_book: Archivo PDF de la guía del usuario de Slicer](./4.Slicing/Slicing.pdf)

## <a id="A5"> 5. Firmware </a>
**:pencil: ¿Qué es el archivo bin del firmware y el código fuente?**
El archivo bin de firmware es la memoria exacta que se escribe en la memoria flash integrada.
El código fuente del firmware es la parte central del firmware. Nuestro código fuente de firmware se basa en [**marlin**](https://www.marlinfw.org).     
Puede descargar el archivo bin del firmware o el código fuente desde el siguiente enlace.
- [:arrow_down: archivo contenedor de firmware][LINK_FIRMWARE]
- [:arrow_down: código fuente del firmware][LINK_SOURCECODE]

## <a id="A6"> 6. Solución de problemas </a>
Si tiene algún problema al instalar y utilizar la impresora, primero intente encontrar una solución en el [:book: Documento en línea de solución de problemas][LINK_TROUBLESHOOTING]. Si no puede resolver este problema, contáctenos por correo electrónico (:email: support@zonestar3d.com).

## <a id="A7"> 7. Imprimir piezas </a>
Hay varios componentes de la máquina que están impresos y también hemos preparado algunas actualizaciones para usted. Si lo desea, puede descargarlos e imprimirlos y luego instalarlos en su máquina.

-----
## <a id="A8"> Funciones opcionales </a>
Hemos introducido algunas funciones opcionales para esta máquina; puede actualizar estas funciones en cualquier momento según sus preferencias. Si está interesado en esto, lea la guía de funciones de actualización opcionales para obtener información más detallada.
- [:book: Documento en línea de la guía de funciones de actualización opcional][Z9V5MK6_OPTION]
- [:blue_book: archivo pdf de la guía de funciones de actualización opcionales](./OptionalFeatures.pdf)
