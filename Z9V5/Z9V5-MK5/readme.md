# Z9V5Pro-MK5 User Guide
### [:arrow_down: Download All Document](https://downgit.github.io/#/home?url=https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/FZ9V5-MK5)  

-----
### :globe_with_meridians: Translate
We provide online documentation for files precisely because it is easy to translate into languages you are familiar with. Below, we list some common browser translation add-ons for your reference.
- [**Windows Edge Translate Add-on**](https://microsoftedge.microsoft.com/addons/detail/edge-translate/bfdogplmndidlpjfhoijckpakkdjkkil?hl=en-US)    
- [**Firefox Translations Add-on**](https://support.mozilla.org/en-US/kb/firefox-translations-add-on?redirectslug=firefox-translations&redirectlocale=en-US)
- [**Google Translate Chrome Extension**](https://chrome.google.com/webstore/detail/google-translate/aapbdbdomjkkjkaonfhkkikfgjllcleb)

------
## :warning:NOTICE:warning:
### :loudspeaker:If you are a beginner of 3d printer, please carefully read the [:book: Step-by-Step Guide](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK5/step_by_step.md), and following the steps to do step by step.  
### :loudspeaker: If you are experienced on 3d printer, please also briefly read the [:book: Step-by-Step Guide](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK5/step_by_step.md) at least, and ensure that you have known how to load filaments to the hot end correctlly.
### :loudspeaker: You need to load all the 4 filaments to the hotend whether printing one or multi color 3d prints, incorrect operationa may block the mix color hotend. If the hot end blockage caused by incorrect operation, it is not covered by the warranty. For how to load filaments, please refer to [this guide](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK5/1.Installation_and_User_Guide/readme.md#load-filaments).
### :loudspeaker: DONOT pull out the "inner PTFE tubes" (the 4 white tubes with black fittings) from the M4V6 hot end.

------
# [Documents](http://bit.ly/3KLDI2J)
## :book: Contents
- [**Installation guide**](#1-installation-guide)  
- [**Operation guide**](#2-operation-guide)  
- [**Test gcode files**](#3-test-g-code-file)
- [**Slicing software**](#4-slicing)
- [**Firmware**](#5-firmware)
- [**Troubleshootings**](#6-troubleshooting)
- [**Print parts stl files**](#7-print-parts)
- [**Optional upgrade features**](#optional-upgrade-features)

-----
## 1. Installation Guide
#### First, please refer to the following documents and videos to complete the installation and wiring of the machine.
#### Installation guide    
  - [:book: Online Document][Installation]
  - [:blue_book: PDF file](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK5/1.Installation_and_User_Guide/Installation.pdf) 
  - [:clapper: Video tutorial](https://youtu.be/TGHUVzV1Pg4)
#### Wiring guide    
  - [:book: Online Document][Wiring]
  - [:blue_book: PDF file](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK5/1.Installation_and_User_Guide/Wiring.pdf)
  - [:clapper: Video tutorial](https://youtu.be/tQQNLDOpdQU) 
  - [:art: Wiring diagram](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK5/1.Installation_and_User_Guide/Wiring/Z9V5Pro_Wiring_Diagram.jpg)

## 2. Operation Guide
#### Introduction to LCD Control Panel
After completing the installation and wiring, please take a look the below guide to know how to use the control panel, and understand the functions of LCD menu generally.
- [:book: Online Document][LCD_MENU].
- [:blue_book: PDF file](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK5/1.Installation_and_User_Guide/LCDMENU_Description.pdf).
#### Print first works
Read the below guide and follow the steps to level the bed, load filaments and print your first work from SD card.
- [:book: Online Document][Operation]
- [:blue_book: PDF file](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK5/1.Installation_and_User_Guide/Operation.pdf)
#### :page_with_curl: More features
You can also read the following documents to gain a deeper understanding of the extruder (hot end and print head) used by your machine, as well as some advanced features of the machine.
- [:book: M4V6 Hotend introduction][M4V6]
- [:book: Mix color feature use guide][Mix_Feature]
- [:book: Print From PC][PrintFromPC]
- [:book: Advance features use guide][Advance_Features]

## 3. Test G-code file
**:pencil: What Is G-code In 3D Printing?**    
G-code is information, or instructions that 3d printer requires in order to print a 3 dimensional object, it is the langurage of the 3d printer can understand. G-Code is generated by your slicing software, by translating a standard 3D modelling file such as STL, object, AMF file etc..  :page_with_curl: [**Reference 1**](https://beginner3dprinting.com/what-is-g-code-in-3d-printing/)  :page_with_curl: [**Reference 2**](https://www.reprap.org/wiki/G-code)    
#### We build some gcode file for testing, you can print these gcode files from the SD card. These gcode files are used to verify whether your machine is working properly or to demonstrate what printing functions this machine has.     
**[:arrow_down: Download all test gcode files](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK5/2.Test_gcode/Test_gcode.zip).**
- **xyz_cube.gcode**: A simple test gcode file used to verify if the machine was working well.  
<!-- - **TempCal_PLA.gcode**: A test gcode file to check the best printing temperature of your PLA filament. -->
- **dog.gcode**: A classic printing quality test file. 
- **Vase.gcode**: A test vase.      
  - **GradientMix_Vase.gcode**: A vase as the same with vase.gcode but enabled "gradient mix" feature.
  - **RandomMix_Vase.gcode**: A vase as the same with vase.gcode but enabled "random mix" feature.
- **M4_4CTest.gcode**: A base 4 colors test file for 3d printer with a 4-IN-1-OUT mix color hot end.
- **M4_4C_BODY3D.gcode**: A biger 4 color test file.   
- **16color_tower.gcode**: A base 16 color test file for 3d printer with a 4-IN-1-OUT mix color hot end. 
- **level_test_310.gcode**: A test file used to verify the effect after enabling "bed automatic leveling" feature.  
#### [:arrow_right: Download more test gcode files](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/test_gcode/M4/readme.md).
 
## 4. Slicing
**[:pencil: What is slicing In 3D Printing?](https://en.wikipedia.org/wiki/Slicer_(3D_printing))**             
A slicer is toolpath generation software used in the majority of 3D printing processes for the conversion of a 3D object model to specific instructions for the printer. In particular, the conversion from a model in STL format to printer commands in g-code format in fused filament fabrication and other similar processes.   
#### Slicing software use guide  
- **[:book: Online document][slicing]**
- **[:blue_book: PDF file](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK5/4.Slicing/Slicing.pdf)**

## 5. Firmware
**:pencil: What is firmware bin file and source code?**    
Firmware bin file is the exact memory that is written to the embedded flash.        
Firmware source code is the core part of the firmware. Our firmware source code is base on [**marlin**](https://www.marlinfw.org).  
You can download firmware bin file or source code from the below link
- **[:arrow_right: Download firmware bin file](https://github.com/ZONESTAR3D/Firmware/tree/master/Z9/Z9V5/bin/Z9V5Pro-MK5)**    
- **[:arrow_right: Download firmware source code](https://github.com/ZONESTAR3D/source-code-for-3d-printer)**

## 6. Troubleshooting
If you have any problems installing and using the printer, please try to find a solution from the online troubleshooting document first. If you cannot solve this problem, please contact us.      
**[:book: Z9V5 Troubleshooting](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5_FAQ)**

## 7. Print Parts
There are several components on the machine that are printed, and we have also prepared some upgrades for you. If you like, you can download and print them and then install them on your machine.
- [:arrow_down:**Filament holder**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Parts_Stl/FilamentSpoolBracket.zip). The filament holder of Z9V5Pro can support the vast majority of filament spool in the market, but there are also some filament spools that may be longer. You can download stl files and print them to replace the original ones.     
- [:arrow_down:**Power supply fan cover**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Parts_Stl/PSUfancover.zip). The fan of the power supply may have some dust after long-term use. You can print a cover and install it on the power fan, which can be easier to clean. And this cover can also reduce the noise of the fan.    
- [:arrow_down:**Hotend fan duct**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Parts_Stl/fanduct_m4v6.zip). The dock of the extruder fan is may be damaged after using a while, yiou can download and print one to replace it.     
- [:arrow_down:**Filament recycling box**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Parts_Stl/Recyclebin.zip). When printing, there are always some fine threads that need to be removed. It is a good idea to print a small garbage box and install it on the Z-axis profile of the machine to collect this garbage.     
- [:arrow_down:**Tool station**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Parts_Stl/Z9_tool_supports.zip). Diagonal pliers, tweezers, shovels, and small screwdrivers are commonly used tools with 3D printers. You can print a collection station for tools to place them.     
- [:arrow_down:**Filament run out detector case**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Parts_Stl/FRODV6.zip). The case of the Filament run our sensor equipped with the machine is a print part. If it is damaged, you can print one by yourself.     
**:arrow_right:More print stl files, please refer to https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Parts_Stl**.

-----
## Optional upgrade features
We have developed some scalable features for the machine. If you are interested in these features, please click the below link to know more detailed.    
**[:arrow_right:Optional upgrade features][OptionalFeatures]**.

-----
[Installation]: https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK5/1.Installation_and_User_Guide/Installation.md
[Wiring]: https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK5/1.Installation_and_User_Guide/Wiring.md
[LCD_MENU]: https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK5/1.Installation_and_User_Guide/LCDMENU_Description.md
[Operation]: https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK5/1.Installation_and_User_Guide/Operation.md
[M4V6]: https://github.com/ZONESTAR3D/Upgrade-kit-guide/blob/main/HOTEND/M4%20%204-IN-1-OUT%20Mixing%20Color%20Hotend/M4_V6
[Mix_Feature]: https://github.com/ZONESTAR3D/Document-and-User-Guide/tree/master/Mixing_Color
[PrintFromPC]: https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK5/1.Installation_and_User_Guide/PrintFromPC
[Advance_Features]: https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK5/1.Installation_and_User_Guide/Advance_Features.md
[slicing]: https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK5/4.Slicing
[OptionalFeatures]: https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK5/OptionalFeatures.md