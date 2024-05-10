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
## Step by Step Guide
In a word, from the moment you received the machine to the moment you can print your own 3D model file, there are a total of 5 steps required: **Installation - Leveling the bed - Load filaments - Printing test gcode file - Slicing and print your own 3d file**.      

### <a id ="a1">Step 1. Installation</a>
- 1.1 **Installation**. Refer to the [:book: **installation guide**](./1.Installation/Installation.md) and [:clapper: **installation video tutorial**](https://youtu.be/pdr8nLl3T3w) to complete the installation of the machine.
- 1.2 **Wiring**. the process of wiring is basically to insert the plug into the corresponding socket. What you need to pay attention is **to make sure the connectors are plug well**, especially for the 2PIN docking sockets. In addition, for the wiring of the print head (hot end), please note that there are several sockets of the same but different colors, please pay attention to plug them according to the color of the socket.
- 1.3 **Power ON**. When wiring is complete, you can [:clapper: **turn on Z9V5**](https://youtu.be/xTlMHtxkGoY). Please note in particular that the Z9V5 has 2 power switches. the one is ***AC switch***(the red switch on the back of the machine) and another is ***DC switch***(a round metal push button switch on the front of the machine control box), you need to turn on the AC switch first and then **press and hold** the DC switch for about 5 seconds to turn on Z9V5.
- 1.4 **Simply Test**. After power on, you can operate the menu on the LCD screen ([:book: **LCD Menu description**](./2.Operation/LCDMENU_Description.md)) to verify whether the machine can work normally. Usually this involves several steps:
  - 1.4.1 **Prepare>>Auto Home>>Home All**. This step is to make the print head of the machine return to the origin.
  - 1.4.2 **Prepare>>Temperature>>Preheat PLA**. This step is to check the hot end and the hot bed can be heated normally.In this step, when the temperature of the nozzle exceeds 60 degrees, you should see a fan on the right side of the print head (hot end) spin up, this is the hot end cooling fan. 
  - 1.4.3 **Prepare>>Temperature>>FAN Speed:**. After pressing the knob and setting the fan speed (set to 255), you should now be able to turn the fan (on left side for M4V6 hotend) up as well.     
  After these 3 steps, it is basically determined that the machine are working normally, you can proceed to the following steps. If you find that any part is not working properly, please double check the wiring, or refer to[:clapper: **machine auto testing video tutorial**](https://youtu.be/Mf92BlmKA0A) to do a auto machine testing.

### <a id ="a2">Step 2. Leveling the bed</a>
Before start printing, you need to do a simple bed leveling to set the height between the nozzle and the bed (printing platform), so that the filament can be pasted on the bed well. Please refer to [:clapper: **Bed leveling video tutorial**](https://youtu.be/nxzB7ho1kNo) to do it.

### <a id ="a3">Step 3. Load filaments</a>
Refer to this [:clapper: video tutorial](https://youtu.be/KZQdL7Rgy1s) to load all 4 filaments to the extruders and hot end.     
#### :warning: ATTENTION PLEASE :warning: 
1. **You need load all 4 filaments to the hot end whatever you print one color or multi color 3d prints.**
2. **Ensure the filaments has been loaded to the bottom of the hot end, otherwise it may cause blockage the hot end.**

### <a id ="a4">Step 4. Print test gcode file</a>
FDM 3D printers can only recognize gcode files, you need to copy the gcode files to the SD card, insert the SD card into the SD card socket of the 3D printer, and then start to print.    
Since Z9V5Pro is a 3D printer with 4 extruders, we suggest that you print a one color 3d model and a 4 colors 3d model to test whether the machine is working properly.
#### Print one color 3d prints
- **Prepare gcode file**. Locate the **xyz_cube.gcode** file from your SD card or [:arrow_down: click here to download it](./3.TestGcode/Test_gcode.zip) and unzip it on your PC, and then copy the **xyz_cube.gcode** to SD card, plug the SD card to the machine's SD socket.
- **Print from SD card**. Move cursor to **Print** item on LCD screen and click the knob and choose **xyz_cube** file, click knob to start printing.
- **Fine tune nozzle height**. Wait the nozzle and hotbed heating, and when starting to print the first layer, double click the knob of LCD screen and fine tune the distance from the nozzle to the bed (nozzle is higher than sticker about 0.4mm), wait until the printing is finished.
#### Print 4 color 3d prints
- **Prepare gcode file**. Locate the **M4_4CTest.gcode** file from your SD card or [:arrow_down: click here to download it](./3.TestGcode/M4_4C_test.zip) and unzip it on your PC, and then copy the **M4_4CTest.gcode** to SD card, plug the SD card to the machine's SD socket.
- **Print from SD card**. Move cursor to **Print** item on LCD screen and click the knob and choose **M4_4CTest** file, click knob to start printing.
- **Fine tune nozzle height**. Wait the nozzle and hotbed heating, and when starting to print the first layer, double click the knob of LCD screen and fine tune the distance from the nozzle to the bed (nozzle is higher than sticker about 0.4mm), wait until the printing is finished.

### <a id ="a5">Step 5. Slicing your own 3d model and print it</a>
Before printing your own 3D models, you need to convert the 3d model file (a stl/obj/AMF format file which [downloaded from the internet](#a6) or drawing by yourself) to a gcode file, this process is called <u>"**slicing**"</u>. 
- Firstly you need to download the slicing software and install it on your computer, and set the parameters of your machine in the slicing software or load the preset file of your machine which set by the 3d printer manufacture.   
- Next, you need to run the slicing software, and may also need to set some parameters according to the characteristics of your 3D model file and then execute slicing. 
- After slicing finished, copy the generated gcode file to the SD card and following the [:point_right:Stpe 4](#a4) to print it out by your 3d printer.   
#### *PrusaSlicer* is the slicing software we recommended, please refer to [:point_right:here][PRUSA_SLICER] to download and install PrusaSlicer software and read the user guide. 
:warning: **ATTENTION PLEASE** :warning:     
Default Z9V5Pro-MK6 equipied with a M4V6 (4-IN-1-OUT mix Color) hot end, please pay attention to choose the printer preset (Z9 + M4 Hotend) when slicing.     

----
### <a id ="a6">Famous free 3D model download websites</a>
- [thingiverse](https://www.thingiverse.com/)  
- [printables](https://www.printables.com/)  
- [youmagine](https://www.youmagine.com/)   

----
