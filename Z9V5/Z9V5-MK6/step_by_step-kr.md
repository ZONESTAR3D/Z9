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
## 단계별 가이드
한마디로, 기계를 받은 순간부터 자신의 3D 모델 파일을 인쇄할 수 있는 순간까지 총 5단계가 필요합니다. **설치 - 베드 레벨링 - 필라멘트 로드 - 테스트 gcode 파일 인쇄 - 슬라이싱 및 자신만의 3D 파일을 인쇄하세요**.
#### 설치(Z9V5-MK5와 동일)
[![](https://img.youtube.com/vi/pdr8nLl3T3w/0.jpg)](https://www.youtube.com/watch?v=pdr8nLl3T3w)
#### 기본 작업
[![](https://img.youtube.com/vi/GrCOZ4ADHeA/0.jpg)](https://www.youtube.com/watch?v=GrCOZ4ADHeA)
#### 멀티 컬러 인쇄
[![](https://img.youtube.com/vi/iddKadfrdjw/0.jpg)](https://www.youtube.com/watch?v=iddKadfrdjw)

### <a id ="a1">1단계. 설치</a>
- 1.1 **설치**. [:book: **설치 가이드**](./1.Installation/Installation.md) 및 [:clapper: **설치 비디오 튜토리얼**](https://youtu.be/pdr8nLl3T3w)을 참조하세요. 기계 설치를 완료합니다.
- 1.2 **배선**. 배선 과정은 기본적으로 해당 소켓에 플러그를 삽입하는 것입니다. 주의해야 할 것은 **커넥터가 잘 꽂혀 있는지 확인**하는 것입니다. 특히 2PIN 도킹 소켓의 경우 더욱 그렇습니다. 또한, 프린트 헤드(핫 엔드)의 배선에는 동일하지만 색상이 다른 소켓이 여러 개 있으므로 소켓 색상에 따라 연결하도록 주의하십시오.
- 1.3 **전원 켜기**. 배선이 완료되면 [:clapper: **Z9V5 켜기**][VIDEO_POWERON]할 수 있습니다. 특히 Z9V5에는 2개의 전원 스위치가 있다는 점에 유의하세요. 하나는 ***AC 스위치***(기계 뒷면의 빨간색 스위치)이고 다른 하나는 ***DC 스위치***(기계 제어 상자 전면에 있는 둥근 금속 푸시 버튼 스위치)입니다. 먼저 AC 스위치를 켠 다음 DC 스위치를 약 5초 동안 **눌러서** Z9V5를 켜야 합니다.
- 1.4 **단순한 테스트**. 전원을 켠 후 LCD 화면([:book: **LCD 메뉴 설명**](./2.Operation/LCDMENU_Description.md))에서 메뉴를 조작하여 기기가 정상적으로 작동하는지 확인할 수 있습니다. 일반적으로 여기에는 여러 단계가 포함됩니다.
   - 1.4.1 **준비>>자동 홈>>모두 홈**. 이 단계는 기계의 프린트 헤드를 원점으로 복귀시키는 단계입니다.
   - 1.4.2 **준비>>온도>>PLA 예열**. 이 단계는 핫엔드를 확인하는 단계이며 핫베드가 정상적으로 가열될 수 있습니다. 이 단계에서 노즐의 온도가 60도를 초과하면 프린트 헤드 오른쪽(핫엔드)의 팬이 회전하는 것을 볼 수 있습니다. , 이것은 핫 엔드 냉각 팬입니다.
   - 1.4.3 **준비>>온도>>팬 속도:**. 손잡이를 누르고 팬 속도(255로 설정)를 설정한 후 이제 팬(M4V6 핫엔드의 경우 왼쪽)도 위로 돌릴 수 있습니다.
   이 3단계를 거쳐 기본적으로 기기가 정상적으로 작동하는 것으로 판단되면 다음 단계를 진행할 수 있습니다. 일부 부품이 제대로 작동하지 않는 경우 배선을 다시 확인하거나 [:clapper: **기계 자동 테스트 비디오 튜토리얼**](https://youtu.be/Mf92BlmKA0A)을 참조하여 자동 기계를 수행하십시오. 테스트.

### <a id ="a2">2단계. 침대 수평 맞추기</a>
프린팅을 시작하기 전에 필라멘트가 베드에 잘 붙을 수 있도록 간단한 베드 레벨링을 하여 노즐과 베드(프린팅 플랫폼) 사이의 높이를 설정해야 합니다. [:clapper: **베드 레벨링 비디오 튜토리얼**][VIDEO_BEDLEVEL]을 참조하여 수행하세요.

### <a id ="a3">3단계. 필라멘트 장착</a>
압출기 및 핫엔드에 필라멘트 4개를 모두 로드하려면 이 [:clapper: 동영상 튜토리얼][VIDEO_LOADFILAMENT]을 참조하세요.
#### :warning: 주의하세요 :warning:
1. **단색 또는 다중 색상 3D 인쇄를 인쇄하려면 4개의 필라멘트를 모두 핫엔드에 로드해야 합니다.**
2. **필라멘트가 핫 엔드 하단에 로드되었는지 확인하세요. 그렇지 않으면 핫 엔드가 막힐 수 있습니다.**

### <a id ="a4">4단계. 테스트 gcode 파일 인쇄</a>
FDM 3D 프린터는 gcode 파일만 인식할 수 있습니다. gcode 파일을 SD 카드에 복사하고 SD 카드를 3D 프린터의 SD 카드 소켓에 삽입한 다음 인쇄를 시작해야 합니다.
Z9V5Pro는 4개의 압출기가 있는 3D 프린터이므로 단색 3D 모델과 4색 3D 모델을 인쇄하여 기계가 제대로 작동하는지 테스트하는 것이 좋습니다.
#### 단색 3D 프린트 인쇄
#####  [:clapper: 동영상 튜토리얼][VIDEO_PRINT1C]
- **gcode 파일을 준비하세요**. SD 카드에서 **xyz_cube.gcode** 파일을 찾거나 [:arrow_down: 다운로드하려면 여기를 클릭](./3.Test_gcode/xyz_cube.zip)하여 PC에 압축을 푼 다음 **xyz_cube를 복사하세요. .gcode**를 SD 카드에 연결하려면 SD 카드를 기기의 SD 소켓에 연결하세요.
- **SD 카드에서 인쇄**. LCD 화면의 **Print** 항목으로 커서를 이동한 후 손잡이를 클릭하고 **xyz_cube** 파일을 선택한 후 손잡이를 클릭하여 인쇄를 시작합니다.
- **노즐 높이를 미세 조정하세요**. 노즐과 온상 가열을 기다린 후 첫 번째 레이어 인쇄를 시작할 때 LCD 화면의 손잡이를 두 번 클릭하고 노즐에서 베드까지의 거리를 미세 조정하고(노즐은 스티커보다 약 0.4mm 높음) 인쇄가 완료될 때까지 기다립니다. 완성된.
#### 4색 3D 프린트 인쇄
#####  [:clapper: 동영상 튜토리얼][VIDEO_PRINT4C]
- **gcode 파일을 준비하세요**. SD 카드에서 **M4_4CTest.gcode** 파일을 찾거나 [:arrow_down: 다운로드하려면 여기를 클릭](./3.Test_gcode/M4_4CTest.zip)하고 PC에 압축을 푼 다음 **M4_4CTest를 복사하세요. .gcode**를 SD 카드에 연결하려면 SD 카드를 기기의 SD 소켓에 연결하세요.
- **SD 카드에서 인쇄**. LCD 화면의 **Print** 항목으로 커서를 이동한 후 손잡이를 클릭하고 **M4_4CTest** 파일을 선택한 후 손잡이를 클릭하여 인쇄를 시작합니다.
- **노즐 높이를 미세 조정하세요**. 노즐과 온상 가열을 기다린 후 첫 번째 레이어 인쇄를 시작할 때 LCD 화면의 손잡이를 두 번 클릭하고 노즐에서 베드까지의 거리를 미세 조정하고(노즐은 스티커보다 약 0.4mm 높음) 인쇄가 완료될 때까지 기다립니다. 완성된.

### <a id ="a5">5단계. 나만의 3D 모델을 잘라서 인쇄</a>
자신의 3D 모델을 인쇄하기 전에 3D 모델 파일([인터넷에서 다운로드](#a6)하거나 직접 그리는 stl/obj/AMF 형식 파일)을 gcode 파일로 변환해야 합니다. 이 프로세스를 <u>"**슬라이싱**"</u>.
- 먼저 슬라이싱 소프트웨어를 다운로드하여 컴퓨터에 설치하고 슬라이싱 소프트웨어에서 기계의 매개변수를 설정하거나 3D 프린터 제조업체에서 설정한 기계의 사전 설정 파일을 로드해야 합니다.
- 다음으로 슬라이싱 소프트웨어를 실행해야 하며, 3D 모델 파일의 특성에 따라 일부 매개변수를 설정한 후 슬라이싱을 실행해야 할 수도 있습니다.
- 슬라이싱이 완료되면 생성된 gcode 파일을 SD 카드에 복사하고 [:point_right:Stpe 4](#a4) 순서에 따라 3D 프린터로 출력합니다.
#### *PrusaSlicer*는 우리가 권장하는 슬라이싱 소프트웨어입니다. PrusaSlicer 소프트웨어를 다운로드 및 설치하고 사용자 가이드를 읽으려면 [:point_right:here][PRUSA_SLICER]를 참조하세요.
:warning: **주의하세요** :warning:
기본 Z9V5Pro-MK6에는 M4V6(4-IN-1-OUT 혼합 색상) 핫엔드가 장착되어 있습니다. 슬라이스 시 프린터 사전 설정(Z9 + M4 핫엔드)을 선택하는 데 주의하시기 바랍니다.

----
### <a id ="a6">유명한 무료 3D 모델 다운로드 웹사이트</a>
- [thingiverse](https://www.thingiverse.com/)  
- [printables](https://www.printables.com/)  
- [youmagine](https://www.youmagine.com/)   

----