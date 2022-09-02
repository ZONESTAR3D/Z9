## Language / Translate
[![](../../languagepic/EN.png)](https://github/ZONESTAR3D/Z9/tree/main/Z9V5-MK4)
[![](../../languagepic/ES.png)](https://github-com.translate.goog/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK4?_x_tr_sl=en&_x_tr_tl=es)
[![](../../languagepic/PT.png)](https://github-com.translate.goog/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK4?_x_tr_sl=en&_x_tr_tl=pt)
[![](../../languagepic/FR.png)](https://github-com.translate.goog/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK4?_x_tr_sl=en&_x_tr_tl=fr)
[![](../../languagepic/RU.png)](https://github-com.translate.goog/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK4?_x_tr_sl=en&_x_tr_tl=ru)
[![](../../languagepic/IT.png)](https://github-com.translate.goog/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK4?_x_tr_sl=en&_x_tr_tl=it)
[![](../../languagepic/DE.png)](https://github-com.translate.goog/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK4?_x_tr_sl=en&_x_tr_tl=de)
[![](../../languagepic/PL.png)](https://github-com.translate.goog/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK4?_x_tr_sl=en&_x_tr_tl=pl)
[![](../../languagepic/KR.png)](https://github-com.translate.goog/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK4?_x_tr_sl=en&_x_tr_tl=ko)
[![](../../languagepic/JP.png)](https://github-com.translate.goog/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK4?_x_tr_sl=en&_x_tr_tl=ja)
[![](../../languagepic/SA.png)](https://github-com.translate.goog/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK4?_x_tr_sl=en&_x_tr_tl=ar)

------
## :warning:NOTICE:warning:
### Even if you are very experienced in using 3D printers, please read the following documents carefully too:  
- [**Installation and Quick User Guide**](./1.Installation_and_User_Guide/Z9V5Pro-MK4_Installation_and_User_Guide_EN.pdf).  
- [**E4 hotend user guide**](./1.Installation_and_User_Guide/E4_Hotend_User_Guide.pdf).  

## Download Z9V5-MK4 files
- :arrow_down: [**Download all documents from github**](https://downgit.github.io/#/home?url=https:%2F%2Fgithub.com%2FZONESTAR3D%2FZ9%2Ftree%2Fmain%2FZ9V5%2FZ9V5-MK4)  
- :arrow_down: [**Download document from cloud disk - google driver**](https://drive.google.com/drive/folders/1WHe4OkeOWdzoYPS0skEaJ-6lydVaQIRK)   
- :arrow_down: [**Download document from cloud disk - Jianguoyun**](https://www.jianguoyun.com/p/DUr952YQyoP1BxiRhcgEIAA)   

------
## Step by Step Guide
If you're a beginner with 3D printers, with so much documentation to read, you might not know where to start. Don't worry, we'll go into the details of these documents next step by step. In a word, you need to do 4 steps **Install the machine - Printing test file - Slicing your own 3d file - Printing your 3d file**.      
First at all, please download the documents and save to your PC from [:point_up: above link](#download-z9v5-mk4-files).
### Step 1. Install the machine
- 1.1 **Installation**. Refer to the [:blue_book: **installation guide**](./1.Installation_and_User_Guide/Z9V5Pro-MK4_Installation_and_User_Guide_EN.pdf) and [ :movie_camera: **installation video tutorial**](https://youtu.be/Xa3Q1m6HbDI) to complete the installation of the machine. The Z9V5 has a high pre-assembled ratio, so installation is very simple. 
- 1.2 **Wiring**. the process of wiring is basically to insert the plug into the corresponding socket. What you need to pay attention is to make sure the plug is fully inserted into the socket. Especially for those 2PIN docking sockets that sometimes make poor contact. In addition, for the wiring of the print head (hot end), please note that there are several sockets of the same type but different colors, please pay attention to plug them according to the color of the socket.
- 1.3 **Power ON**. When wiring is complete, you can [:movie_camera: **turn on Z9V5**](https://youtu.be/xTlMHtxkGoY). Please note in particular that the Z9V5 has 2 power switches. the one is ***AC switch***(the red switch on the back of the machine) and another is ***DC switch***(a round metal push button switch on the front of the machine control box), you need to turn on the AC switch first and then **press and hold** the DC switch for a few seconds to turn on Z9V5.
- 1.4 **Simply Test**. After power on, you can operate the menu on the LCD screen ([**LCD Menu description**](./1.Installation_and_User_Guide/LCD_DWIN_MENU_Description.md)) to verify whether the machine can work normally. Usually this involves several steps:
  - 1.4.1 **Prepare>>Auto Home>>Home All**. This step is to make the print head of the machine return to the origin.
  - 1.4.2 **Prepare>>Temperature>>Preheat PLA**. This step is to check the hot end and the hot bed can be heated normally.In this step, when the temperature of the nozzle exceeds 60 degrees, you should see a fan on the right side of the print head (hot end) spin up, this is the hot end cooling fan. 
  - 1.4.3 **Prepare>>Temperature>>FAN**. After pressing the knob and setting the fan speed (set to 255), you should now be able to turn the fan on the left side up as well.   
  After these 3 steps, it is basically determined that the machine are working normally, you can proceed to the following steps. If you find that any part is not working properly, please double check the wiring, or to do a auto testing (Refer to[ :movie_camera: **machine auto testing video turorial**](https://youtu.be/Mf92BlmKA0A)).
- 1.5 **Bed Level**. Before printing the test file, you need to do a simple hot bed leveling to set the height between the nozzle and the printing platform, so that the filament flowing out of the nozzle can be pasted on the hot bed well. Please refer to [:movie_camera: **Bed leveling video tutorial**](https://youtu.be/nxzB7ho1kNo) to do it.

### Step 2. Printing test file
FDM 3D printers can only recognize gcode files, we need to copy the gcode files to the SD card, insert the SD card into the SD card slot of the 3D printer, and then start to print.
- 2.1 **Prepare gcode file - one color**. Locate the **xyz_cube.gcode** file from your downloaded files or [:arrow_down: download it](./2.Test_gcode/xyz_cube.zip) directly and  unzip it on PC, and then copy the **xyz_cube.gcode** to SD card. Plug the SD card to the SD socket of machine.
- 2.2 **Load filament - one color**. Refer to this [:movie_camera: video tutorial](https://youtu.be/6aTF5QnFhi4) to load filament to the extruder and hotend.
- 2.3 **Print from SD card - one color**. Move item to **Print** item on LCD screen and click the knob and choose **xyz_cube.gcode** file, click knob to start print.
- 2.4 **Fine tune nozzle height**. Wait the nozzle and hotbed heating, and when starting to print the first layer, double to click the knob of LCD screen to fine turn the distance from the nozzle to the bed, and then wait it to finish.
- 2.5 **Prepare gcode file**. Locate the **Z9E4_4CTest.gcode** file from your downloaded files or [:arrow_down: download it](./2.Test_gcode/E4_4C/Z9E4_4C_Test.zip) directly and  unzip it on PC, and then copy the **Z9E4_4CTest.gcode** to SD card. Plug the SD card to the SD socket of machine.
- 2.6 **Load filaments - 4 colors**. Refer to this [:movie_camera: video tutorial](https://youtu.be/FyHrAMytlT8) to load 4 color filaments to the extruders and hotend.
- 2.7 **Print from SD card - 4 colors**. Move item to **Print** item on LCD screen and click the knob and choose **Z9E4_4CTest.gcode** file, click knob to start print.
- 2.8 **Check Preload**. Wait the nozzle and hotbed heating, and check if the printer can print out 4 colors lines on the side of the hotbed.
- 2.9 **Fine tune nozzle height**. When the hotend moved to the center of the hotbed, double to click the knob of LCD screen to fine turn the distance from the nozzle to the bed. Wait until the printing is finished.

### Step 3. Slicing your own 3d file
Obviously you will have the need to print your own 3D models. The process of converting a 3D model into a gcode file that can be printed on a machine is called slicing. You need to download and install the slicing software, then import the 3D model file (stl, obj, AMF, etc.) and complete the slicing, and finally copy the generated gcode file to the SD card and print it on the machine. Our recommended slicing software is PrusaSlicer. For detailed instructions, please refer to [4. Slicing](#4-slicing).   
Several of the most famous free 3D model download websites:
- [thingiverse](https://www.thingiverse.com/)  
- [printables](https://www.printables.com/)  
- [youmagine](https://www.youmagine.com/)   

### Step 4. Printing your 3d file
Once you are done slicing, copy the obtained gcode files to your SD card, then you can print them out like in the [step 2](#step-2-printing-test-file).

### Step 5. To use advanced features
After you fully understand all the basic use of the machine, you can try some advanced functions of the machine. For details, please refer to [Advance features](#advanced-features).

------
## Documents
### :book: Contents
- [**Installation and operation guide**](#1-installation-and-user-guide)  
- [**Test gcode files**](#2-test-gcode)
- [**Video tutorial for installation, operation and step-by-Step guide**](#-3video-tutorial)
- [**Slicing software user guide and slicing software download link**](#4-slicing)
- [**Control board firmware ,source code, firmware uploadling guide and download link**](#5-firmware)
- [**FAQ, Maintenance manual, etc.**](#6-faq)
- [**Print parts stl files, introduction to upgradeable functions, etc.**](#7-others)

### 1. Installation and User Guide
- :book: [**Installation and user guide**](./1.Installation_and_User_Guide/Z9V5Pro-MK4_Installation_and_User_Guide_EN.pdf)
- :book: [**LCD screen menu description**](./1.Installation_and_User_Guide/LCD_DWIN_MENU_Description.pdf)
- :movie_camera: [**Installation video tutorial**](https://youtu.be/Xa3Q1m6HbDI)
- :art: [**Wiring diagram**](./1.Installation_and_User_Guide/Z9V5Pro_Wiring_Diagram.jpg)
- :file_folder: [**Advanced features guide**](./1.Installation_and_User_Guide/Advances_Feature/)

### 2. Test Gcode
#### :pencil: What Is G-code In 3D Printing?
G-code is information, or instructions that 3d printer requires in order to print a 3 dimensional object, it is the langurage of the 3d printer can understand. G Code is generated by your slicing software, by translating a standard 3D modelling file such as an STL file into the code that your specific 3D printer will understand.    
:page_with_curl: [**Reference 1**](https://beginner3dprinting.com/what-is-g-code-in-3d-printing/)  :page_with_curl: [**Reference 2**](https://www.reprap.org/wiki/G-code)     
#### :book: File list
- [:arrow_down:](./2.Test_gcode/xyz_cube.zip) **xyz_cube.gcode**:           A simple test gcode file for verifing if the machine is working well.  
- [:arrow_down:](./2.Test_gcode/TempCal_PLA.zip)**TempCal_PLA.gcode**:        A test gcode file to check the best printing temperature of your PLA filament
- [:arrow_down:](./2.Test_gcode/1C/1C_3DBenchy.zip) **1C/3DBenchy.gcode**:        A classic printing performance test file, one color  
- [:arrow_down:](./2.Test_gcode/1C/1C_dog.zip)**1C/dog.gcode**:             A classic printing quanlity test file, one color    
- [:arrow_down:](./2.Test_gcode/E4_4C/Z9E4_4CTest.zip)**E4_4C/Z9E4_4CTest.gcode**:  A base 4 colors test file   
- :file_folder: More gcode file, please refer to :point_right:[**here**](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/PrusaSlicer/test_gcode/E4)

### 3. Video Tutorial  
**NOTE: The video tutorial may be a little different with your machine because of firmware version is different, for reference only**     
#### Installation and Operation Guide
- :movie_camera: [**Installaltion**](https://youtu.be/Xa3Q1m6HbDI) 
- :movie_camera: [**Turn On / Turn Off the printer**](https://youtu.be/xTlMHtxkGoY)
- :movie_camera: [**Bed leveling**](https://youtu.be/nxzB7ho1kNo)
- :movie_camera: [**How to load Filament - for one color printing**](https://youtu.be/6aTF5QnFhi4)
- :movie_camera: [**How to load Filament - for multi colors printing**](https://youtu.be/FyHrAMytlT8)
#### Advanced features
- **Bed auto leveling.** Bending of the 3D printer's hotbed is unavoidable. When you are printing a print with a large bottom, you need to use the hotbed auto-leveling feature to correct the curvature of the hotbed. For how to use, please refer to [:book: **User Guide**](./1.Installation_and_User_Guide/Advances_Feature/Bed_Auto_Leveling) or [:movie_camera: **Video tutorial**](https://youtu.be/Zoyl6PybsUk)
- **Power auto shutdown after print finished.** Usually 3D printing takes a long time, you can enable this feature to let the machine turn off automatically after the printing is finished to save energy. For how to use, please refer to [:movie_camera: **Video tutorial**](https://youtu.be/SJLpmJL-tG4)
- **Filament run out detect.** Sometimes there is not enough filaments left in the filament roll to complete the current printing. At this time, you can pass the filament through the Filament-Run-Out-Detector and enable the **run-out** feature on LCD screen. The machine can detect that the filament are out and pause the printing, and then resume the printing process after you replace a new filament roll. For how to use, please refer to [:movie_camera: **Video tutorial**](https://youtu.be/QCJ-6L6ze1w)     
  :warning: If you are sure that the filament of one extruder is engouh, do not pass the filament through that Filament-Run-Out-Detector.       
  :warning: Filament-Run-Out-Detect feature may introduce some imperfections on the print when printing is paused.        
       
- **Power losss recovery.** If your power supply network has frequent power outages, you can enable the automatic power losss recovery function before start printing. When the power goes out and it resumed, you can press the DC switch to turn on the power of the machine, and then the machine will automatically detect the printing breakpoint and provide you with whether you need to continue printing. For how to use, please refer to  [:movie_camera: **Video tutorial**](https://youtu.be/SK95C-6OpB4)   
  :warning: Breakpoints data and gcode files will be stored on the SD, must keep the SD card in socket when turn on the machine after power resumed.       
  :warning: Power losss recovery feature may introduce some imperfections on the prints when printing is resumed.

### 4. Slicing
#### :pencil: What is slicing In 3D Printing?
Slicing is a piece of software that everyone uses when creating objects and products on a 3D printer. The software gives the printer a path to follow. The slicing software takes your image and converts it into G codes that your 3D printer can understand. These G codes are a type of instruction on how the printer needs to print your design.:page_with_curl: [**Reference 1**](https://loveandrobots.com/what-is-slicing-in-3d-printing/)  :page_with_curl: [**Reference 2**](https://en.wikipedia.org/wiki/Slicer_(3D_printing))     
Please download the slicing software and install to your PC, and then read the guide or video tutorial to study how to slicing.
- :arrow_down: [**Download Slicing Software**](https://github.com/ZONESTAR3D/Slicing-Guide)
- :movie_camera: [**How to download and install slicing software**](https://youtu.be/SgyXD-kQIeo)  
- :book: [**PrusSlicer User Manual**](./4.Slicing/readme.md)  :blue_book:[**(pdf file)**](./4.Slicing/readme.pdf)  
- :movie_camera: [**Slicing guide - for one color printing**](https://youtu.be/SgyXD-kQIeo4)  
- :movie_camera: [**Slicing guide - for multi colors printing**](https://youtu.be/AIKrszmxvE4)    
- :movie_camera: [**Slicing guide - Convert one color 3d file to multi colors**](https://youtu.be/2LJu4G0T4Zg)    
:star2: **For the newest slicing guide and more slicing software user guide, please click here :point_right: [slicing guide](https://github.com/ZONESTAR3D/Slicing-Guide)**

### 5. Firmware
- [**Firmware bin file**](https://github.com/ZONESTAR3D/Firmware/tree/master/Z9/Z9V5/Z9V5-MK4)  
- [**Firmware source code**](https://github.com/ZONESTAR3D/source-code-for-3d-printer)
#### :pencil: What is bin file and source code?
> **Firmware bin file** is the exact memory that is written to the embedded flash.  
> **Firmware source code** is the core part of the firmware. The entire firmware can be thought of as different sub modules. It is divided into many sub files. These files are called source files. And, the entire program files are called source file or source code. Now our firmware source code is base on [**marlin**](https://www.marlinfw.org).

### 6. FAQ
- :movie_camera: [**How to replace nozzle**](https://youtu.be/N3-aCQg5XYI)
- :movie_camera: [**Machine auto test**](https://youtu.be/Mf92BlmKA0A)
<!-- - :movie_camera: [**How to adjust the pressure of extruder**]() -->
<!-- - :movie_camera: [**How to clean the extruder**]() -->
<!-- - :movie_camera: [**How to clean the E4 hotend**]() -->

### 7. Others
#### [Print parts stl files](./7.Others/Parts_stl_file/readme.md)


------
## Optional upgrade kit / parts
### Automatic Repeat Printing Module
By upgrading this module to make your 3D printer capable of continuous automatic mass production.  
:book: [**User guide**](https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/Auto_Repeat_Printing)   

### Laser engine
By upgrading this item, you can turn your 3D printer into a simple laser engraving machine. Higher power laser modules can improve engraving speed or support materials with higher melting point.  
:book: [**User guide**](https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/Laser%20Engraving)  
<!-- :movie_camera: [**Video tutorial**]() -->

### WiFi wireless control module
By upgrading this item, you can remote control your 3d printer.    
:book: [**User guide**](https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/WiFi)  
<!-- :movie_camera: [**Video tutorial**]() -->

### Direct drive extruder
By upgrading this project, you can print flexible materials (such as TPU filament). Of course, it also has other advantages and disadvantages of the "direct drive" extruders, such as having less strings issue, better flow, more supporting materials, etc., Also because of the heavier weight of the extruder, the printing speed must be lower.  
:book: [**User guide**](https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/Direct%20Drive%20Extrruder)   
:movie_camera: [**Video tutorial**](https://youtu.be/7aF-C7VgDZY)

### More types of Hotend / extruder
Each type of hot end has its advantages and disadvantages, you can choose different hotends according to different requirement.
- Fast printing
- Print flexible filament
- Support higher temperature filament (Max 260 degreeC)     
Please refer to [**here**](https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND)    
