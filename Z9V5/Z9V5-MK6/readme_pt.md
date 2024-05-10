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
# Guia do usuário para impressora 3D ZONESTAR Z9V5Pro-MK6

----
## :warning: ATENÇÃO POR FAVOR
#### :loudspeaker: Antes de usar a máquina, leia [:book:"Precauções para usar M4V6"][M4V6_PRECAUTION] com atenção.
#### :loudspeaker: Deve carregar 4 filamentos no hotend M4V6 simultaneamente, a operação incorreta pode bloquear o hotend de cores misturadas. Se o bloqueio do hot end for causado por operação incorreta, não será coberto pela garantia. Para saber como carregar filamentos, consulte [:book: this guide][Z9V5MK6_LOADFILAMENT].
#### :loudspeaker: Se você é iniciante em impressora 3D, leia atentamente o [Guia passo a passo] [Z9V5MK6_STEPBYSTEP] e siga as etapas a seguir.
- [:book: **Precauções para usar M4V6**][M4V6_PRECAUTION]
- [:book: **Como carregar filamentos corretamente**][Z9V5MK6_LOADFILAMENT]
- [:book: **Guia passo a passo**][Z9V5MK6_STEPBYSTEP]
<!-- - [:blue_book: arquivo PDF do guia passo a passo](./step_by_step.pdf) -->

------
## :book: Conteúdo
- [**Guia de instalação**](#a1)
- [**Guia de operação**](#a2)
- [**Teste arquivos gcode**](#a3)
- [**Software de fatiamento**](#a4)
- [**Firmware**](#a5)
- [**Soluções de problemas**](#a6)
- [**Imprimir arquivos stl de peças**](#a7)
- [**Recursos opcionais de atualização**](#a8)

-----
## <a id="a1"> 1. Guia de instalação </a>
Primeiro, consulte os seguintes documentos e vídeos para concluir a instalação e fiação da máquina.
### Instalação
- [:book: Documento on-line do guia de instalação](./1.Installation/Installation.md)
- [:blue_book: Arquivo PDF do guia de instalação](./1.Installation/Installation.pdf)
- [:clapper: Tutorial em vídeo do guia de instalação](https://youtu.be/TGHUVzV1Pg4)
### Fiação
- [:book: Documento on-line do guia de fiação](./1.Installation/Wiring.md)
- [:blue_book: Arquivo PDF do guia de fiação](./1.Installation/Wiring.pdf)
- [:art: Diagrama de fiação](./1.Installation/Z9V5Pro_Wiring_Diagram.jpg)
- [:clapper: Tutorial em vídeo de fiação](https://youtu.be/tQQNLDOpdQU)

## <a id="a2"> 2. Guia de operação </a>
### **Introdução ao painel de controle LCD**
Depois de concluir a instalação e a fiação, consulte o guia abaixo para saber como usar o painel de controle (tela LCD) e entender as funções do menu LCD em geral.
- [:book: Documento on-line do menu LCD](./2.Operation/LCDMENU_Description.md)
- [:blue_book: arquivo PDF do menu LCD](./2.Operation/LCDMENU_Description.pdf)
#### **Imprima seus primeiros trabalhos**
Agora você pode tentar imprimir seus trabalhos de "Hello word", antes de iniciar a impressão, primeiro você precisa fazer uma correção simples na altura da cama quente (é chamada de "nivelamento da cama"), e depois carregar os filamentos na extrusora (observe que independentemente da cor da sua impressão, você precisa carregar todos os 4 filamentos nas extrusoras e no hot end). Em seguida, você pode inserir o cartão SD na máquina e escolher um arquivo gcode do modelo 3D de teste no cartão SD. Para obter detalhes, consulte os documentos abaixo.
- [:book: Documento on-line do guia de operação](./2.Operation/Operation.md)
- [:blue_book: arquivo PDF do guia de operação](./2.Operation/Operation.pdf)
#### :page_with_curl: Mais recursos
Você também pode ler os documentos a seguir para obter uma compreensão mais profunda da extrusora (hot end e cabeçote de impressão) usada pela sua máquina, bem como alguns recursos avançados da máquina.
- [:book: Guia de uso do recurso Mix Color][LINK_MIX_FEATURE]
- [:book: introdução ao Hotend M4V6][LINK_M4V6]
- [:book: Imprimir do PC](./2.Operation/PrintFromPC/readme.md)
- [:book: Guia de uso de recursos avançados](./2.Operation/Advance_Features.md)

## <a id="a3"> 3. Teste o arquivo de código G </a>
**:lápis: O que é código G na impressão 3D?**
Código G são informações ou instruções que a impressora 3D requer para imprimir um objeto tridimensional, é a linguagem que a impressora 3D pode entender. O G-Code é gerado pelo seu software de fatiamento, traduzindo um arquivo de modelagem 3D padrão, como STL, objeto, arquivo AMF etc. **][GCODE_REF2]    
Armazenamos alguns arquivos gcode de teste no cartão SD, para ajudar a verificar se a máquina estava funcionando corretamente ou para demonstrar quais funções de impressão esta máquina possui. Se você não conseguir encontrar os arquivos gcode de teste no cartão SD, faça download em [:arrow_down: **aqui**](./3.TestGcode/Test_gcode.zip).    
- **xyz_cube.gcode**: Um arquivo gcode de teste simples usado para verificar se a máquina estava funcionando bem.
- **dog.gcode**: Um arquivo clássico de teste de qualidade de impressão.
- **Vase.gcode**: um vaso de teste.
   - **GradientMix_Vase.gcode**: Um vaso igual a vase.gcode, mas com o recurso "gradient mix" habilitado.
   - **RandomMix_Vase.gcode**: Um vaso igual a vase.gcode, mas com recurso de "mix aleatório" habilitado.
- **M4_4CTest.gcode**: Um arquivo de teste de base de 4 cores para impressora 3D com hot end M4.
- **M4_4C_BODY3D.gcode**: Um arquivo de teste maior com 4 cores.
- **16color_tower.gcode**: Um arquivo de teste de base de 16 cores para mostrar o resultado da mistura de filamentos de cores diferentes.
- **level_test_310.gcode**: Um arquivo de teste usado para verificar o nivelamento da cama quente (sem nivelamento automático da cama).
- **level_test_310-G29.gcode**: Um arquivo de teste usado para verificar o nivelamento da cama quente (com nivelamento automático da cama).
**[:arrow_down: Baixe mais arquivos gcode de teste][M4_TEST_GCODE].**
 
## <a id="a4"> 4. Fatiar </a>
**[:pencil: O que é fatiar na impressão 3D?](https://en.wikipedia.org/wiki/Slicer_(3D_printing))**
Um fatiador é um software de geração de percurso usado na maioria dos processos de impressão 3D para a conversão de um modelo de objeto 3D em instruções específicas para a impressora. Em particular, a conversão de um modelo em formato STL para comandos de impressora em formato de código G na fabricação de filamentos fundidos e outros processos semelhantes.   
- [:book:Documento on-line do guia do usuário do Slicer](./4.Slicing/readme.md)
- [:blue_book: Arquivo PDF do guia do usuário do Slicer](./4.Slicing/Slicing.pdf)

## <a id="a5"> 5. Firmware </a>
**:pencil: O que é o arquivo bin do firmware e o código-fonte?**
O arquivo bin do firmware é a memória exata gravada no flash incorporado.   
O código-fonte do firmware é a parte central do firmware. Nosso código-fonte de firmware é baseado em [**marlin**](https://www.marlinfw.org).
Você pode baixar o arquivo bin do firmware ou o código-fonte no link abaixo.   
- [:arrow_down: Arquivo bin de firmware][LINK_FIRMWARE]
- [:arrow_down: Código-fonte do firmware][LINK_SOURCECODE]

## <a id="a6"> 6. Solução de problemas </a>
Se você tiver algum problema ao instalar e usar a impressora, tente primeiro encontrar uma solução no [:book: Documento on-line de solução de problemas][LINK_TROUBLESHOOTING]. Se você não conseguir resolver este problema, entre em contato conosco por email (:email: support@zonestar3d.com).   

## <a id="a7"> 7. Imprimir peças </a>
Existem vários componentes na máquina que são impressos e também preparamos algumas atualizações para você. Se desejar, você pode baixá-los e imprimi-los e depois instalá-los em sua máquina.

-----
## <a id="a8"> Recursos opcionais </a>
Introduzimos alguns recursos opcionais para esta máquina. Você pode atualizar esses recursos a qualquer momento de acordo com suas preferências. Se você estiver interessado nisso, leia o guia de recursos de atualização opcionais para obter informações mais detalhadas.
- [:book: Documento on-line do guia de recursos de atualização opcionais][Z9V5MK6_OPTION]
- [:blue_book: arquivo pdf do guia de recursos de atualização opcional](./OptionalFeatures.pdf)

