
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
## Guia de operação
Antes de iniciar a impressão, é necessário nivelar a cama quente (ajustar a distância entre o bico e a plataforma de impressão) e carregar os filamentos nas extrusoras e na extremidade quente.
## Nivelando a cama quente
#### :warning: Para impressoras 3D FDM, a distância entre o bico e a cama quente é muito importante ao imprimir a primeira camada. Se a distância for muito próxima, os filamentos não podem fluir para fora do bico e até danificar o bico e a cama quente. Se a distância for muito grande, os filamentos não poderão ser colados na cama quente, as próximas camadas não poderão ser empilhadas corretamente e causarão falha na impressão.
###### [![](https://img.youtube.com/vi/jNf98S0u2VQ/0.jpg)](https://www.youtube.com/watch?v=jNf98S0u2VQ)
- **Etapa 1.** Ligue a impressora 3D e então faça ***Prepare>>Auto Home>>Home All*** no LCD MENU, espere o hotend ir para a posição HOME.
- **Etapa 2.** Aperte as porcas manuais sob a cama para descer a cama até a posição mais baixa (Fig 1).
- **Etapa 3.** Faça ***Preparar>> Nivelamento da cama>> Ponto 1*** no painel de controle (Fig 2), o bico irá para os cantos da cama, afrouxe as porcas manuais sob o viveiro (Fig 3) e deixe o bico quase tocar no viveiro (Fig 4). Continue fazendo ***Ponto 2/3/4*** até que todos os 4 cantos estejam nivelados.
- **Etapa 4.** Repita a Etapa 3 e faça 2 a 3 voltas, até que todos os quatro cantos estejam na mesma altura.
![](./Operation/levelbed.png)

----
### Carregar filamentos
###### [![](https://img.youtube.com/vi/1rr4dXRxKc4/0.jpg)](https://www.youtube.com/watch?v=1rr4dXRxKc4)
Esta impressora está equipada com quatro extrusoras e um hot end de mistura de cores 4-IN-1-OUT. As extrusoras e o hot end são conectados por uma guia de filamento (tubo de PTFE). ***Antes de imprimir, você precisa carregar todos os 4 filamentos nas extrusoras e alimentá-los na parte inferior da extremidade quente.***
- **Etapa 1.** Faça ***Prepare>>Auto Home>>Home All*** no painel de controle e, em seguida, faça ***Prepare>>Temperature>> Preheat PLA***, aguardando que a temperatura do bico seja atingida a 190 ℃ (Fig. 1).
- **Etapa 2.** Use um alicate diagonal para cortar a cabeça do filamento (Fig 2) e, em seguida, pressione a alça da extrusora nº 1 e insira o filamento, empurre o filamento até poder ver o filamento no PTFE guia (Fig. 3). Gire a engrenagem da extrusora nº 1 (Fig 4), observe o filamento até que ele entre na parte inferior do hot end.
- **Etapa 3.** Usando o mesmo método da etapa 2 para carregar os filamentos na extrusora#2 ~ extrusora#4, observe os filamentos até que eles entrem na parte inferior da extremidade quente.
- **Etapa 4.** Gire lentamente a engrenagem da extrusora#1 ~ extrusora#4 uma por uma e observe o bico, até que você possa ver o filamento fluindo para fora do bico (Fig 5).
![](./Operation/loadfilament.png)

----
### Imprima seus trabalhos do "Hellow World""
#### Imprimir um arquivo de teste de cor única
###### [![](https://img.youtube.com/vi/NbVy8NjKt_s/0.jpg)](https://www.youtube.com/watch?v=NbVy8NjKt_s)
- **Etapa 1.** Insira o cartão SD no slot de cartão SD da impressora (Fig 1).
- **Etapa 2.** Clique no ÍCONE ***Imprimir*** no painel de controle e escolha ***xyz_cube.gcode*** (Fig 2), clique no botão para iniciar a impressão.
- **Etapa 3.** Espere até que o hotend e o hotbed atinjam a temperatura definida (Fig 3), o bico retornará à posição de origem e então se moverá para cima da plataforma de impressão e extrusará o filamento, use uma pinça para remover o filamento de saída (Fig 4).
- **Etapa 4.** Quando o bico for movido para a cama quente e começar a imprimir, clique duas vezes no botão para abrir o menu **Babystep Z** (Fig 5), gire o botão lentamente para ajustar a altura de impressão plataforma, observe a distância do bocal ao leito, até que a distância fique boa (Fig 6).
- **Etapa 5.** Aguarde o término da impressão (Fig 7), e espere o viveiro esfriar (Fig 8), e então remova o objeto impresso do viveiro (Fig 9).
![](./Operation/firstprint.png)

#### Imprimir um arquivo de teste multicolorido
###### [![](https://img.youtube.com/vi/iddKadfrdjw/0.jpg)](https://www.youtube.com/watch?v=iddKadfrdjw)
As etapas para impressão multicolorida e impressão em cor única são basicamente as mesmas, mas antes de iniciar a impressão, extrude alguns filamentos de todas as extrusoras para confirmar se o hot end funciona normalmente.
- **Etapa 1.** Insira o cartão SD no soquete de cartão SD da impressora.
- **Etapa 2.** Aqueça o bico e faça a extrusão de alguns filamentos. **Preparar>>Filamento: *Bocal de pré-aquecimento: 200* -> *Extrusora: Todos* -> *Carregar lentamente***.
- **Etapa 3.** Clique no ÍCONE “Imprimir” no painel de controle e escolha ***M4_4CTest.gcode***, clique no botão para iniciar a impressão.
- **Etapa 4.** Ajuste a distância do bocal ao leito.
- **Etapa 5.** Aguarde o término da impressão.

-----
### :fireworks: Parabéns!
Após imprimir os primeiros trabalhos, você terá um entendimento básico de como funciona a impressora 3D. Em seguida, você pode imprimir outros arquivos de teste ou fatiar seu próprio modelo 3D e usar a máquina para imprimi-lo.
É recomendável que você baixe e instale o software de fatiamento e leia o guia do usuário do software de fatiamento para saber como usá-lo. Para obter detalhes, consulte o [:book: **Guia de fatiamento**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/4.Slicing).