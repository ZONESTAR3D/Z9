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
# ZONESTAR Z9V5Pro-MK6 3D 프린터 사용 설명서

----
## :warning: 주의하세요
#### :loudspeaker: 기기를 사용하기 전에 [:book:"M4V6 사용 시 주의사항"][M4V6_PRECAUTION]을 주의 깊게 읽어보세요.
#### :loudspeaker: M4V6 핫엔드에 4개의 필라멘트를 동시에 로드해야 합니다. 잘못된 작동으로 인해 혼합 색상 핫엔드가 차단될 수 있습니다. 잘못된 작동으로 인해 핫엔드가 막힌 경우에는 보증이 적용되지 않습니다. 필라멘트 로딩 방법은 [:book: 이 가이드][Z9V5MK6_LOADFILAMENT]를 참조하세요.
#### :loudspeaker: 3D 프린터 초보자라면 [:book: 단계별 가이드][Z9V5MK6_STEPBYSTEP]를 주의 깊게 읽고 단계를 따르세요.
- [:book: **M4V6 사용 시 주의사항**][M4V6_PRECAUTION]
- [:book: **필라멘트를 올바르게 로드하는 방법**][Z9V5MK6_LOADFILAMENT]
- [:book: **단계별 가이드**][Z9V5MK6_STEPBYSTEP]

------
## :book: 목차
- [**설치 가이드**](#A1)
- [**조작안내**](#A2)
- [**gcode 파일 테스트**](#A3)
- [**슬라이싱 소프트웨어**](#A4)
- [**펌웨어**](#A5)
- [**문제 해결**](#A6)
- [**부품 stl 파일 인쇄**](#A7)
- [**선택적 업그레이드 기능**](#A8)

-----
## <a id="A1"> 1. 설치 가이드 </a>
먼저, 기계의 설치 및 배선을 완료하기 위해 다음 문서와 비디오를 참조하십시오.
### 설치
- [:book: 설치 가이드 온라인 문서](./1.Installation/Installation.md)
- [:blue_book: 설치 가이드 PDF 파일](./1.Installation/Installation.pdf)
- [:clapper: 설치 가이드 동영상 튜토리얼](https://youtu.be/TGHUVzV1Pg4)
### 배선
- [:book: 배선 가이드 온라인 문서](./1.Installation/Wiring.md)
- [:blue_book: 배선 가이드 PDF 파일](./1.Installation/Wiring.pdf)
- [:art: 배선도](./1.Installation/Z9V5Pro_Wiring_Diagram.jpg)
- [:clapper: 배선 동영상 튜토리얼](https://youtu.be/tQQNLDOpdQU)

## <a id="A2"> 2. 운영 안내 </a>
### **LCD 제어판 소개**
설치 및 결선 작업이 완료되면 아래의 가이드를 통해 제어판(LCD 화면)의 사용법을 숙지하시고, LCD 메뉴의 전반적인 기능을 이해하시기 바랍니다.
- [:book: LCD 메뉴 온라인 문서](./2.Operation/LCDMENU_Description.md)
- [:blue_book: LCD 메뉴 PDF 파일](./2.Operation/LCDMENU_Description.pdf)
#### **첫 번째 작품을 인쇄하세요**
이제 "Hello word" 작품을 인쇄해 볼 수 있습니다. 인쇄를 시작하기 전에 먼저 핫 베드의 높이를 간단히 수정한 다음("베드 레벨링"이라고 함) 필라멘트를 압출기에 로드해야 합니다. (인쇄물의 색상에 관계없이 4개의 필라멘트를 모두 압출기와 핫엔드에 로드해야 합니다.) 다음으로 SD 카드를 기기에 삽입하고 SD 카드에서 테스트용 3D 모델 gcode 파일을 선택할 수 있습니다. 자세한 사항은 아래 문서를 참고하시기 바랍니다.
- [:book: 운영 가이드 온라인 문서](./2.Operation/Operation.md)
- [:blue_book: 조작 가이드 PDF 파일](./2.Operation/Operation.pdf)
#### :page_with_curl: 추가 기능
또한 다음 문서를 읽고 기계에서 사용되는 압출기(핫 엔드 및 프린트 헤드)와 기계의 일부 고급 기능에 대해 더 깊이 이해할 수 있습니다.
- [:book: 믹스 컬러 기능 이용 안내][LINK_MIX_FEATURE]
- [:book: M4V6 핫엔드 소개][LINK_M4V6]
- [:book: PC에서 인쇄](./2.Operation/PrintFromPC/readme.md)
- [:book: 고급 기능 사용 가이드](./2.Operation/Advance_Features.md)

## <a id="A3"> 3. G 코드 파일 테스트 </a>
**:연필: 3D 프린팅에서 G 코드란 무엇입니까?**
G-code는 3D 프린터가 3차원 물체를 출력하기 위해 필요한 정보 또는 명령어로, 3D 프린터가 이해할 수 있는 언어입니다. G-코드는 STL, 객체, AMF 파일 등과 같은 표준 3D 모델링 파일을 변환하여 슬라이싱 소프트웨어에 의해 생성됩니다. :page_with_curl: [**참조 1**][GCODE_REF1] :page_with_curl: [**참조 2**][GCODE_REF2]
기계가 제대로 작동하는지 확인하거나 이 기계에 어떤 인쇄 기능이 있는지 보여주기 위해 일부 테스트 gcode 파일을 SD 카드에 저장했습니다. SD 카드에서 테스트 gcode 파일을 찾을 수 없는 경우 [:arrow_down: **여기**](./3.TestGcode/Test_gcode.zip)에서 다운로드하세요.
- **xyz_cube.gcode**: 머신이 제대로 작동하는지 확인하는 데 사용되는 간단한 테스트 gcode 파일입니다.
- **dog.gcode**: 클래식 인쇄 품질 테스트 파일입니다.
- **Vase.gcode**: 테스트 꽃병입니다.
   - **GradientMix_Vase.gcode**: vase.gcode와 동일하지만 "그라디언트 믹스" 기능이 활성화된 꽃병입니다.
   - **RandomMix_Vase.gcode**: vase.gcode와 동일하지만 "랜덤 믹스" 기능이 활성화된 꽃병입니다.
- **M4_4CTest.gcode**: M4 핫엔드를 갖춘 3D 프린터용 기본 4색 테스트 파일입니다.
- **M4_4C_BODY3D.gcode**: 더 큰 4색 테스트 파일입니다.
- **16color_tower.gcode**: 서로 다른 색상의 필라멘트를 혼합한 결과를 보여주는 기본 16색 테스트 파일입니다.
- **level_test_310.gcode**: 핫베드 평탄도를 확인하는 데 사용되는 테스트 파일입니다(베드 자동 레벨링 없음).
- **level_test_310-G29.gcode**: 핫베드 평탄도(베드 자동 레벨링 포함)를 확인하는 데 사용되는 테스트 파일입니다.
**[:arrow_down: 추가 테스트 gcode 파일 다운로드][M4_TEST_GCODE].**
 
## <a id="A4"> 4. 자르기 </a>
**[:pencil: 3D 프린팅에서 슬라이싱이란 무엇입니까?](https://en.wikipedia.org/wiki/Slicer_(3D_printing))**
슬라이서는 3D 객체 모델을 프린터의 특정 지침으로 변환하기 위해 대부분의 3D 프린팅 프로세스에 사용되는 도구 경로 생성 소프트웨어입니다. 특히 융합 필라멘트 제조 및 기타 유사한 프로세스에서 STL 형식의 모델을 g-코드 형식의 프린터 명령으로 변환합니다.
- [:book:Slicer 사용자 가이드 온라인 문서](./4.Slicing/readme.md)
- [:blue_book: 슬라이서 사용 설명서 PDF 파일](./4.Slicing/Slicing.pdf)

## <a id="A5"> 5. 펌웨어 </a>
**:연필: 펌웨어 bin 파일과 소스 코드는 무엇입니까?**
펌웨어 bin 파일은 내장 플래시에 기록되는 정확한 메모리입니다.   
펌웨어 소스 코드는 펌웨어의 핵심 부분입니다. 당사의 펌웨어 소스 코드는 [**marlin**](https://www.marlinfw.org)을 기반으로 합니다.   
아래 링크에서 펌웨어 bin 파일이나 소스코드를 다운로드 받으실 수 있습니다.   
- [:arrow_down: 펌웨어 bin 파일][LINK_FIRMWARE]
- [:arrow_down: 펌웨어 소스 코드][LINK_SOURCECODE]

## <a id="A6"> 6. 문제 해결 </a>
프린터 설치 및 사용에 문제가 있는 경우 먼저 [:book: 문제 해결 온라인 문서][LINK_TROUBLESHOOTING]에서 해결 방법을 찾아보세요. 이 문제를 해결할 수 없는 경우 이메일(:email: support@zonestar3d.com)로 문의해 주세요.

## <a id="A7"> 7. 부품 인쇄 </a>
기계에는 인쇄된 여러 구성 요소가 있으며, 우리는 또한 귀하를 위해 몇 가지 업그레이드를 준비했습니다. 원하는 경우 다운로드하여 인쇄한 다음 컴퓨터에 설치할 수 있습니다.

-----
## <a id="A8"> 선택 기능 </a>
우리는 이 기기에 몇 가지 옵션 기능을 도입했습니다. 귀하는 귀하의 선호에 따라 언제든지 이러한 기능을 업그레이드할 수 있습니다. 이에 관심이 있으시면 선택적 업그레이드 기능 가이드를 읽어 자세한 정보를 얻으십시오.
- [:book: 선택적 업그레이드 기능 가이드 온라인 문서][Z9V5MK6_OPTION]
- [:blue_book: 선택적 업그레이드 기능 가이드 pdf 파일](./OptionalFeatures.pdf)
