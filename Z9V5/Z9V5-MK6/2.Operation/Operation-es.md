
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
## Manual de operaciones
Antes de comenzar a imprimir, debe nivelar la cama caliente (ajustar la distancia entre la boquilla y la plataforma de impresión) y cargar los filamentos en las extrusoras y el extremo caliente.
## Nivelar la cama caliente
#### :warning: Para impresoras 3D FDM, la distancia entre la boquilla y la cama caliente es muy importante al imprimir la primera capa. Si la distancia es demasiado corta, los filamentos no pueden salir de la boquilla e incluso dañan la boquilla y la cama caliente. Si la distancia es demasiado grande, los filamentos no se pueden pegar en la cama caliente, las siguientes capas no se pueden apilar correctamente y provocan errores de impresión.
###### [![](https://img.youtube.com/vi/jNf98S0u2VQ/0.jpg)](https://www.youtube.com/watch?v=jNf98S0u2VQ)
- **Paso 1.** Encienda la impresora 3D y luego haga ***Preparar>>Inicio automático>>Inicio todo*** en el MENÚ LCD, espere que el hotend vaya a la posición INICIO.
- **Paso 2.** Apriete las tuercas manuales debajo de la cama para bajar la cama a la posición más baja (Fig. 1).
- **Paso 3.** Haga ***Preparar>> Nivelación de la cama>> Punto 1*** en el panel de control (Fig. 2), la boquilla irá a las esquinas de la cama, afloje las tuercas manuales debajo de la cama caliente. (Fig. 3) y deje que la boquilla casi toque el foco (Fig. 4). Continúe haciendo el ***Punto 2/3/4*** hasta que se hayan nivelado las 4 esquinas.
- **Paso 4.** Repita el paso 3 y haga 2 ~ 3 rondas, hasta que las cuatro esquinas estén a la misma altura.
![](./Operation/levelbed.png)

----
### Cargar filamentos
###### [![](https://img.youtube.com/vi/1rr4dXRxKc4/0.jpg)](https://www.youtube.com/watch?v=1rr4dXRxKc4)
Esta impresora está equipada con cuatro extrusoras y un extremo caliente de mezcla de colores 4 EN 1 SALIDA. Los extrusores y el hot end están conectados mediante una guía de filamento (tubo de PTFE). ***Antes de imprimir, debes cargar los 4 filamentos en los extrusores e introducirlos en la parte inferior del extremo caliente.***
- **Paso 1.** Haga ***Preparar>>Inicio automático>>Inicio todo*** en el panel de control, y luego haga ***Preparar>>Temperatura>> Precalentar PLA***, esperando que se alcance la temperatura de la boquilla. a 190 ℃ (Figura 1).
- **Paso 2.** Utilice unos alicates diagonales para cortar la cabeza del filamento (Fig. 2), y luego presione el mango del extrusor n.º 1 e inserte el filamento, empuje el filamento hasta que pueda ver el filamento en el PTFE. guía (Figura 3). Gire el engranaje del extrusor n.º 1 (Fig. 4), observe el filamento hasta que entre en la parte inferior del extremo caliente.
- **Paso 3.** Usando el mismo método que en el paso 2 para cargar los filamentos en el extrusor n.° 2 ~ extrusor n.° 4, observe los filamentos hasta que entren en la parte inferior del extremo caliente.
- **Paso 4.** Gire lentamente los engranajes del extrusor n.° 1 ~ extrusor n.° 4 uno por uno y observe la boquilla, hasta que pueda ver que el filamento sale de la boquilla (Fig. 5).
![](./Operation/loadfilament.png)

----
### Imprime tus obras de "Hellow World"
#### Imprimir un archivo de prueba de un solo color
###### [![](https://img.youtube.com/vi/NbVy8NjKt_s/0.jpg)](https://www.youtube.com/watch?v=NbVy8NjKt_s)
- **Paso 1.** Inserte la tarjeta SD en el zócalo para tarjetas SD de la impresora (Fig. 1).
- **Paso 2.** Haga clic en el ICONO ***Imprimir*** en el panel de control y elija ***xyz_cube.gcode*** (Fig. 2), haga clic en la perilla para comenzar a imprimir.
- **Paso 3.** Espere hasta que el hotend y el hotend alcancen la temperatura establecida (Fig. 3), la boquilla regresará a la posición de origen y luego se moverá hacia arriba de la plataforma de impresión y extruirá el filamento, use unas pinzas. para retirar el filamento de salida (Fig. 4).
- **Paso 4.** Cuando la boquilla se movió a la cama caliente y comenzó a imprimir, haga doble clic en la perilla para abrir un menú **Babystep Z** (Fig. 5), gire la perilla lentamente para ajustar la altura de impresión. plataforma, observar la distancia desde la boquilla hasta la cama, hasta que la distancia sea buena (Fig. 6).
- **Paso 5.** Espere a que finalice la impresión (Fig. 7), espere a que se enfríe la base (Fig. 8) y luego retire el objeto impreso de la base (Fig. 9).
![](./Operation/firstprint.png)

#### Imprimir un archivo de prueba multicolor
###### [![](https://img.youtube.com/vi/iddKadfrdjw/0.jpg)](https://www.youtube.com/watch?v=iddKadfrdjw)
Los pasos para la impresión multicolor y la impresión de un solo color son básicamente los mismos, pero antes de comenzar a imprimir, extruya algunos filamentos de todas las extrusoras para confirmar que el extremo caliente funciona normalmente.
- **Paso 1.** Inserte la tarjeta SD en el zócalo para tarjetas SD de la impresora.
- **Paso 2.** Calentar la boquilla y extruir un poco de filamento. **Preparar>>Filamento: *Precalentar boquilla: 200* -> *Extrusora: Todo* -> *Cargar lentamente***.
- **Paso 3.** Haga clic en el ICONO "Imprimir" en el panel de control y elija ***M4_4CTest.gcode***, haga clic en la perilla para comenzar a imprimir.
- **Paso 4.** Ajuste con precisión la distancia entre la boquilla y la cama.
- **Paso 5.** Espere a que finalice la impresión.

----
### :fireworks: ¡Felicitaciones!
Después de imprimir los primeros trabajos, tendrá una comprensión básica de cómo funciona la impresora 3D. A continuación, puede imprimir otros archivos de prueba o cortar su propio modelo 3D y utilizar la máquina para imprimirlo.
Se recomienda descargar e instalar el software de corte y leer la guía del usuario del software de corte para saber cómo usarlo. Para obtener más detalles, consulte el [:book: **Guía de corte**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/4.Slicing).