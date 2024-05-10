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
## Guia passo a passo
Em uma palavra, desde o momento em que você recebeu a máquina até o momento em que você pode imprimir seu próprio arquivo de modelo 3D, são necessárias 5 etapas no total: **Instalação - Nivelamento da cama - Carregar filamentos - Imprimir arquivo gcode de teste - Fatiar e imprima seu próprio arquivo 3D**.

### <a id ="a1">Etapa 1. Instalação</a>
- 1.1 **Instalação**. Consulte o [:book: **guia de instalação**](./1.Installation/Installation.md) e [:clapper: **tutorial em vídeo de instalação**](https://youtu.be/pdr8nLl3T3w) para conclua a instalação da máquina.
- 1.2 **Fiação**. o processo de fiação consiste basicamente em inserir o plugue na tomada correspondente. O que você precisa prestar atenção é **certificar-se de que os conectores estão bem encaixados**, especialmente para os soquetes de acoplamento de 2 pinos. Além disso, para a fiação da cabeça de impressão (hot end), observe que existem vários soquetes da mesma cor, mas de cores diferentes, preste atenção para conectá-los de acordo com a cor do soquete.
- 1.3 **LIGAR**. Quando a fiação estiver concluída, você pode [:clapper: **ligar o Z9V5**](https://youtu.be/xTlMHtxkGoY). Observe em particular que o Z9V5 possui 2 interruptores liga / desliga. um é o ***interruptor AC*** (o interruptor vermelho na parte traseira da máquina) e o outro é o ***interruptor DC*** (um botão redondo de metal na frente da caixa de controle da máquina), você precisa ligar o interruptor CA primeiro e depois **pressionar e segurar** o interruptor CC por cerca de 5 segundos para ligar o Z9V5.
- 1.4 **Simplesmente teste**. Depois de ligar, você pode operar o menu na tela LCD ([:book: **LCD Menu description**](./2.Operation/LCDMENU_Description.md)) para verificar se a máquina pode funcionar normalmente. Geralmente isso envolve várias etapas:
   - 1.4.1 **Preparar>>Auto Home>>Home All**. Esta etapa serve para fazer com que o cabeçote de impressão da máquina retorne à origem.
   - 1.4.2 **Preparar>>Temperatura>>Pré-aquecer PLA**. Esta etapa é verificar se a extremidade quente e a cama quente podem ser aquecidas normalmente. Nesta etapa, quando a temperatura do bico exceder 60 graus, você deverá ver um ventilador no lado direito da cabeça de impressão (extremidade quente) girando. , este é o ventilador de resfriamento hot end.
   - 1.4.3 **Preparar>>Temperatura>>Velocidade do VENTILADOR:**. Depois de pressionar o botão e definir a velocidade do ventilador (definida para 255), agora você também poderá aumentar o ventilador (no lado esquerdo do hotend M4V6).
   Após essas 3 etapas, é basicamente determinado que a máquina está funcionando normalmente, você pode prosseguir para as etapas seguintes. Se você achar que alguma peça não está funcionando corretamente, verifique novamente a fiação ou consulte [:clapper: **tutorial em vídeo de teste automático de máquina**](https://youtu.be/Mf92BlmKA0A) para fazer uma máquina automática testando.

### <a id ="a2">Etapa 2. Nivelamento da cama</a>
Antes de iniciar a impressão, é necessário fazer um simples nivelamento da cama para definir a altura entre o bico e a mesa (plataforma de impressão), para que o filamento possa ficar bem colado na mesa. Consulte [:clapper: **Tutorial em vídeo sobre nivelamento da cama**](https://youtu.be/nxzB7ho1kNo) para fazer isso.

### <a id ="a3">Etapa 3. Carregar filamentos</a>
Consulte este [:clapper: vídeo tutorial](https://youtu.be/KZQdL7Rgy1s) para carregar todos os 4 filamentos nas extrusoras e no hot end.
#### :warning: ATENÇÃO POR FAVOR :warning:
1. **Você precisa carregar todos os 4 filamentos no hot end, independentemente de imprimir em uma cor ou em impressões 3D multicoloridas.**
2. **Certifique-se de que os filamentos foram carregados na parte inferior da extremidade quente, caso contrário, isso pode causar o bloqueio da extremidade quente.**

### <a id ="a4">Etapa 4. Imprimir arquivo gcode de teste</a>
As impressoras 3D FDM só podem reconhecer arquivos gcode, você precisa copiar os arquivos gcode para o cartão SD, inserir o cartão SD no soquete do cartão SD da impressora 3D e então começar a imprimir.
Como a Z9V5Pro é uma impressora 3D com 4 extrusoras, sugerimos que você imprima um modelo 3D de uma cor e um modelo 3D de 4 cores para testar se a máquina está funcionando corretamente.
#### Imprima impressões 3D em uma cor
- **Prepare o arquivo gcode**. Localize o arquivo **xyz_cube.gcode** em seu cartão SD ou [:arrow_down: clique aqui para baixá-lo](./3.Test_gcode/xyz_cube.zip) e descompacte-o em seu PC e copie o arquivo **xyz_cube .gcode** para cartão SD, conecte o cartão SD ao soquete SD da máquina.
- **Imprimir do cartão SD**. Mova o cursor para o item **Imprimir** na tela LCD e clique no botão e escolha o arquivo **xyz_cube**, clique no botão para iniciar a impressão.
- **Ajuste a altura do bico**. Aguarde o aquecimento do bico e do viveiro, e ao iniciar a impressão da primeira camada, clique duas vezes no botão da tela LCD e ajuste a distância do bico à base (o bico é superior ao adesivo cerca de 0,4 mm), aguarde até que a impressão seja finalizado.
#### Imprimir impressões 3D em 4 cores
- **Prepare o arquivo gcode**. Localize o arquivo **M4_4CTest.gcode** em seu cartão SD ou [:arrow_down: clique aqui para baixá-lo](./3.Test_gcode/M4_4CTest.zip) e descompacte-o em seu PC e copie o **M4_4CTest.zip .gcode** para cartão SD, conecte o cartão SD ao soquete SD da máquina.
- **Imprimir do cartão SD**. Mova o cursor para o item **Imprimir** na tela LCD e clique no botão e escolha o arquivo **M4_4CTest**, clique no botão para iniciar a impressão.
- **Ajuste a altura do bico**. Aguarde o aquecimento do bico e do viveiro, e ao iniciar a impressão da primeira camada, clique duas vezes no botão da tela LCD e ajuste a distância do bico à base (o bico é superior ao adesivo cerca de 0,4 mm), aguarde até que a impressão seja finalizado.

### <a id ="a5">Etapa 5. Fatiar seu próprio modelo 3D e imprimi-lo</a>
Antes de imprimir seus próprios modelos 3D, você precisa converter o arquivo do modelo 3D (um arquivo no formato stl/obj/AMF que [baixado da internet](#a6) ou desenhado por você mesmo) em um arquivo gcode, este processo é chamado < u>"**cortando**"</u>.
- Primeiramente você precisa baixar o software de fatiamento e instalá-lo em seu computador, e definir os parâmetros de sua máquina no software de fatiamento ou carregar o arquivo predefinido de sua máquina definido pelo fabricante da impressora 3D.
- Em seguida, você precisa executar o software de fatiamento, podendo também definir alguns parâmetros de acordo com as características do seu arquivo de modelo 3D e então executar o fatiamento.
- Após terminar o fatiamento, copie o arquivo gcode gerado para o cartão SD e siga o [:point_right:Stpe 4](#a4) para imprimi-lo em sua impressora 3D.
#### *PrusaSlicer* é o software de fatiamento que recomendamos. Consulte [:point_right:here][PRUSA_SLICER] para baixar e instalar o software PrusaSlicer e ler o guia do usuário.
:warning: **ATENÇÃO POR FAVOR** :warning:     
Z9V5Pro-MK6 padrão equipado com um hot end M4V6 (4-IN-1-OUT mix Color), preste atenção para escolher a predefinição da impressora (Z9 + M4 Hotend) ao fatiar.

----
### <a id ="a6">Sites famosos para download gratuito de modelos 3D</a>
- [thingiverse](https://www.thingiverse.com/)  
- [printables](https://www.printables.com/)  
- [youmagine](https://www.youmagine.com/)   
----