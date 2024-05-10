
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
## 운영안내
프린팅을 시작하기 전에 핫베드의 수평을 맞추고(노즐과 프린팅 플랫폼 사이의 거리를 미세 조정) 필라멘트를 압출기와 핫엔드에 로드해야 합니다.
## 핫베드 수평 맞추기
#### :warning: FDM 3D 프린터의 경우 첫 번째 레이어를 인쇄할 때 노즐과 핫베드 사이의 거리가 매우 중요합니다. 거리가 너무 가까우면 노즐 밖으로 필라멘트가 흘러나오지 못하고, 심지어 노즐과 핫베드가 손상될 수 있습니다. 거리가 너무 멀면 필라멘트가 핫베드에 붙지 못하고 다음 레이어가 제대로 쌓이지 않아 프린팅이 실패할 수 있습니다.
###### [![](https://img.youtube.com/vi/jNf98S0u2VQ/0.jpg)](https://www.youtube.com/watch?v=jNf98S0u2VQ)
- **1단계.** 3D 프린터의 전원을 켜고 LCD 메뉴에서 ***Prepare>>Auto Home>>Home All*** 을 수행하고 핫엔드가 홈 위치로 이동하기를 기다립니다.
- **2단계.** 침대 아래 핸드 너트를 조여 침대를 가장 낮은 위치로 이동합니다(Fig 1).
- **3단계.** ***Prepare>> Bed leveling>> Point 1*** 지점(Fig 2)을 수행하면 노즐이 베드 모서리로 이동하고 온상 아래의 핸드 너트를 푼다. (Fig 3) 그리고 노즐이 온상에 거의 닿도록 합니다(Fig 4). 4개의 모서리가 모두 수평이 될 때까지 ***Point 2/3/4***을 계속 수행하세요.
- **4단계.** 네 모서리가 모두 같은 높이가 될 때까지 3단계를 반복하고 2~3회 반복합니다.
![](./Operation/levelbed.png)

----
### 필라멘트 로드
###### [![](https://img.youtube.com/vi/1rr4dXRxKc4/0.jpg)](https://www.youtube.com/watch?v=1rr4dXRxKc4)
이 프린터에는 4개의 압출기와 1개의 4-IN-1-OUT 색상 혼합 핫엔드가 장착되어 있습니다. 압출기와 핫 엔드는 필라멘트 가이드(PTFE 튜브)로 연결됩니다. ***프린팅하기 전에 필라멘트 4개를 모두 압출기에 로드하고 핫엔드 바닥에 공급해야 합니다.***
- **1단계.** 제어판에서 ***Prepare>>Auto Home>>Home All*** 을 수행한 다음 ***Prepare>>Temperature>> Preheat PLA*** 을 수행하고 노즐 온도 도달 대기 190℃까지(Fig 1).
- **Step 2.** 대각선 펜치를 사용하여 필라멘트 헤드를 잘라낸 후(Fig 2), Extruder#1의 손잡이를 누르고 필라멘트를 삽입한 후 PTFE에 필라멘트가 보일 때까지 밀어 넣습니다. 가이드(Fig 3). 압출기 #1(Fig 4)의 기어를 회전하고 필라멘트가 핫 엔드 바닥에 들어갈 때까지 지켜봅니다.
- **Step 3.** 2단계와 동일한 방법으로 필라멘트를 Extruder#2 ~ Extruder#4에 로딩하여 필라멘트가 핫엔드 하단으로 들어갈 때까지 지켜봅니다.
- **Step 4.** Extruder#1 ~ Extruder#4의 기어를 하나씩 천천히 돌리면서 필라멘트가 노즐에서 흘러나오는 것을 볼 수 있을 때까지 노즐을 관찰합니다(Fig 5).
![](./Operation/loadfilment.png)

----
### "Hello World"" 작품을 인쇄하세요.
#### 단일 색상 테스트 파일 인쇄
###### [![](https://img.youtube.com/vi/NbVy8NjKt_s/0.jpg)](https://www.youtube.com/watch?v=NbVy8NjKt_s)
- **1단계.** SD 카드를 프린터의 SD 카드 소켓에 삽입합니다(Fig 1).
- **2단계.** 제어판에서 ***Print*** 아이콘을 클릭하고 ***xyz_cube.gcode***(Fig 2)를 선택한 다음 손잡이를 클릭하여 인쇄를 시작합니다.
- **3단계.** 핫엔드와 핫베드가 설정 온도에 도달할 때까지 기다리면(Fig 3), 노즐이 원점 위치로 이동한 다음 프린팅 플랫폼 위로 이동하여 필라멘트를 압출하고 핀셋을 사용합니다. 유출 필라멘트를 제거합니다(Fig 4).
- **Step 4.** 노즐이 핫베드로 이동하고 인쇄가 시작되면 손잡이를 두 번 클릭하여 **Babystep Z** 메뉴(Fig 5)를 열고 손잡이를 천천히 돌려 인쇄 높이를 미세 조정합니다. 플랫폼에서 거리가 잘 나올 때까지 노즐에서 베드까지의 거리를 관찰합니다(Fig 6).
- **5단계.** 프린팅이 완료되기를 기다리고(Fig 7), 핫베드가 식을 때까지 기다린 후(Fig 8), 프린팅된 대상물을 핫베드에서 꺼냅니다(Fig 9).
![](./Operation/firstprint.png)

#### 멀티 컬러 테스트 파일 인쇄
###### [![](https://img.youtube.com/vi/iddKadfrdjw/0.jpg)](https://www.youtube.com/watch?v=iddKadfrdjw)
다색 인쇄 및 단색 인쇄 단계는 기본적으로 동일하지만 인쇄를 시작하기 전에 모든 압출기에서 일부 필라멘트를 압출하여 핫 엔드가 정상적으로 작동하는지 확인하십시오.
- **1단계.** SD 카드를 프린터의 SD 카드 소켓에 삽입합니다.
- **2단계.** 노즐을 가열하고 필라멘트를 압출합니다. **Prepare>>Filament: *Preheat Nozzle: 200* -> *Extruder: All* -> *Load Slowly***.
- **3단계.** 제어판에서 "인쇄" 아이콘을 클릭하고 ***M4_4CTest.gcode***를 선택한 후 손잡이를 클릭하여 인쇄를 시작합니다.
- **4단계.** 노즐에서 베드까지의 거리를 미세 조정합니다.
- **5단계.** 인쇄가 완료될 때까지 기다립니다.

-----
### :fireworks: 축하합니다!
첫 번째 작품을 프린트한 후에는 3D 프린터의 작동 방식에 대한 기본적인 이해를 갖게 됩니다. 다음으로, 다른 테스트 파일을 인쇄하거나 자신의 3D 모델을 슬라이스하고 기계를 사용하여 인쇄할 수 있습니다.
슬라이싱 소프트웨어를 다운로드하여 설치하는 것이 좋으며, 슬라이싱 소프트웨어의 사용자 가이드를 읽어 사용법을 숙지하시기 바랍니다. 자세한 내용은 [:book: **슬라이싱 가이드**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/4.Slicing).
