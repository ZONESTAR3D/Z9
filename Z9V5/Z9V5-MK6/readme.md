# User Guide for ZONESTAR Z9V5Pro-MK6 3D Printer 
### [:arrow_down: Download All Document](https://downgit.github.io/#/home?url=https:%2F%2Fgithub.com%2FZONESTAR3D%2FZ9%2Ftree%2Fmain%2FZ9V5%2FZ9V5-MK6)  

----
### :globe_with_meridians: Translate this page
We provide online documentation for files precisely because it is easy to translate into languages you are familiar with. Below, we list some common browser translation add-ons for your reference.
- [**Windows Edge Translate Add-on**](https://microsoftedge.microsoft.com/addons/detail/edge-translate/bfdogplmndidlpjfhoijckpakkdjkkil?hl=en-US)    
- [**Firefox Translations Add-on**](https://support.mozilla.org/en-US/kb/firefox-translations-add-on?redirectslug=firefox-translations&redirectlocale=en-US)
- [**Google Translate Chrome Extension**](https://chrome.google.com/webstore/detail/google-translate/aapbdbdomjkkjkaonfhkkikfgjllcleb)

----
## :warning: ATTENTION PLEASE
#### :loudspeaker: Before using the machine, please read [:book:"Precautions for using M4V6"](https://github.com/ZONESTAR3D/Upgrade-kit-guide/blob/main/HOTEND/M4/M4_V6/M4V6_Precaution.md) carefully.
#### :loudspeaker: Must load 4 filaments onto the M4V6 hotend simultaneously, incorrect operationa may block the mix color hotend. If the hot end blockage caused by incorrect operation, it is not covered by the warranty. For how to load filaments, please refer to [:book: this guide](https://github.com/ZONESTAR3D/Z9/blob/main/Z9V5/Z9V5-MK6/2.Operation/Operation.md#load-filaments).
#### :loudspeaker: If you are a beginner of 3d printer, please carefully read the [Step-by-Step Guide](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/step_by_step.md), and following the steps to do.   
- [:book: **Precautions for using M4V6**](https://github.com/ZONESTAR3D/Upgrade-kit-guide/blob/main/HOTEND/M4/M4_V6/M4V6_Precaution.md)
- [:book: **How to load filaments correctly**](https://github.com/ZONESTAR3D/Upgrade-kit-guide/blob/main/HOTEND/M4/M4_V6/M4V6_Precaution.md)
- [:book: **Step-by-Step Guide**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/step_by_step.md) 
<!-- - [:blue_book: Step-by-Step Guide PDF file](./step_by_step.pdf)  -->

----
## :book: Contents
- [**Installation guide**](#1-installation-guide)  
- [**Operation guide**](#2-operation-guide)  
- [**Test gcode files**](#3-test-g-code-file)
- [**Slicing software**](#4-slicing)
- [**Firmware**](#5-firmware)
- [**Troubleshootings**](#6-troubleshooting)
- [**Print parts stl files**](#7-print-parts)
- [**Optional upgrade features**](#optional-features)

----
## 1. Installation guide
First, please refer to the following documents and videos to complete the installation and wiring of the machine.
### Installation   
- [:book: Installation Guide Online Document](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/1.Installation/Installation.md) 
- [:blue_book: Installation Guide PDF file](./1.Installation/Installation.pdf) 
- [:clapper: Installation Guide Video tutorial](https://youtu.be/TGHUVzV1Pg4)   
### Wiring    
- [:book: Wiring Guide Online Document](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/1.Installation/Wiring.md) 
- [:blue_book: Wiring Guide PDF file](./1.Installation/Wiring.pdf) 
- [:art: Wiring diagram](./1.Installation/Z9V5Pro_Wiring_Diagram.jpg) 
- [:clapper: Wiring Video tutorial](https://youtu.be/tQQNLDOpdQU)

## 2. Operation Guide
### **Introduction to LCD Control Panel**     
After completing the installation and wiring, please take a look the below guide to know how to use the control panel (LCD Screen), and understand the functions of LCD menu generally.      
- [:book: LCD Menu Online Document](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/2.Operation/LCDMENU_Description.md)    
- [:blue_book: LCD Menu PDF file](./2.Operation/LCDMENU_Description.pdf)    
#### **Print your first works**     
Now you can try to print your "Hello word" works, before starting printing, you first need to make a simple correction to the height of the hot bed (it is called "bed leveling"), and then load the filaments into the extruder (please note that regardless of the color of your print, you need to load all 4 filaments into the extruders and hot end). Next, you can insert the SD card into the machine and choose a testing 3D model gcode file in the SD card. For details, please refer to the documents below.     
- [:book: Operation Guide Online Document](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/2.Operation/Operation.md) 
- [:blue_book: Operation Guide PDF file](./2.Operation/Operation.pdf) 
#### :page_with_curl: More features
You can also read the following documents to gain a deeper understanding of the extruder (hot end and print head) used by your machine, as well as some advanced features of the machine.      
- [:book: Mix color feature use guide][LINK_Mix_Feature]     
- [:book: M4V6 Hotend introduction][LINK_M4V6] 
- [:book: Print From PC](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/2.Operation/PrintFromPC/readme.md)   
- [:book: Advance features use guide](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/2.Operation/Advance_Features.md)    

## 3. Test G-code file
**:pencil: What Is G-code In 3D Printing?**    
G-code is information, or instructions that 3d printer requires in order to print a 3 dimensional object, it is the langurage of the 3d printer can understand. G-Code is generated by your slicing software, by translating a standard 3D modelling file such as STL, object, AMF file etc..  :page_with_curl: [**Reference 1**](https://beginner3dprinting.com/what-is-g-code-in-3d-printing/)  :page_with_curl: [**Reference 2**](https://www.reprap.org/wiki/G-code)    
We stored some test gcode files in SD card, to help verify whether the machine was working properly or to demonstrate what printing functions this machine has. If you can't find the test gcode files in the SD card, please download from [:arrow_down: **here**](https://github.com/ZONESTAR3D/Z9/blob/main/Z9V5/Z9V5-MK6/3.TestGcode/Test_gcode.zip).
- **xyz_cube.gcode**: A simple test gcode file used to verify if the machine was working well.  
- **dog.gcode**: A classic printing quality test file. 
- **Vase.gcode**: A test vase.      
  - **GradientMix_Vase.gcode**: A vase as the same with vase.gcode but enabled "gradient mix" feature.
  - **RandomMix_Vase.gcode**: A vase as the same with vase.gcode but enabled "random mix" feature.
- **M4_4CTest.gcode**: A base 4 colors test file for 3d printer with a M4 hot end.
- **M4_4C_BODY3D.gcode**: A biger 4 color test file.   
- **16color_tower.gcode**: A base 16 color test file to show the result of mixed different color filaments. 
- **level_test_310.gcode**: A test file used to verify the Hot bed flatness (without bed auto leveling). 
- **level_test_310-G29.gcode**: A test file used to verify the Hot bed flatness (with bed auto leveling).     
**[:arrow_down: Download more test gcode files](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/test_gcode/M4/readme.md).**
 
## 4. Slicing
**[:pencil: What is slicing In 3D Printing?](https://en.wikipedia.org/wiki/Slicer_(3D_printing))**             
A slicer is toolpath generation software used in the majority of 3D printing processes for the conversion of a 3D object model to specific instructions for the printer. In particular, the conversion from a model in STL format to printer commands in g-code format in fused filament fabrication and other similar processes.   
- [:book:Slicer User Guide Online Document](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/4.Slicing/readme.md)    
- [:blue_book: Slicer User Guide PDF File](./4.Slicing/Slicing.pdf)   

## 5. Firmware
**:pencil: What is firmware bin file and source code?**    
Firmware bin file is the exact memory that is written to the embedded flash.        
Firmware source code is the core part of the firmware. Our firmware source code is base on [**marlin**](https://www.marlinfw.org).  
You can download firmware bin file or source code from the below link.  
- [:arrow_down: Firmware bin file][LINK_Firmware]   
- [:arrow_down: Firmware source code][LINK_SourceCode]     

## 6. Troubleshooting
If you have any problems installing and using the printer, please try to find a solution from the [:book: Troubleshooting Online Document][LINK_Troubleshooting] first. If you cannot solve this problem, please contact us by email (:email: support@zonestar3d.com).      

## 7. Print Parts
There are several components on the machine that are printed, and we have also prepared some upgrades for you. If you like, you can download and print them and then install them on your machine.

----
## Optional features
We have introduced some optional features for this machine, you can upgrade these features at any time according to your preferences. If you are interesting in this, please read Optional upgrade features guide to get more detailed information.
- [:book:Optional upgrade features guide online document](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/OptionalFeatures.md)
- [:blue_book:Optional upgrade features guide pdf file](./OptionalFeatures.pdf)

----
[LINK_M4V6]: https://github.com/ZONESTAR3D/Upgrade-kit-guide/blob/main/HOTEND/M4%20%204-IN-1-OUT%20Mixing%20Color%20Hotend/M4_V6
[LINK_Mix_Feature]: https://github.com/ZONESTAR3D/Document-and-User-Guide/tree/master/Mixing_Color
[LINK_Firmware]: https://github.com/ZONESTAR3D/Firmware/tree/master/Z9/Z9V5/bin/Z9V5Pro-MK6
[LINK_SourceCode]: https://github.com/ZONESTAR3D/source-code-for-3d-printer
[LINK_Troubleshooting]: https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5_FAQ