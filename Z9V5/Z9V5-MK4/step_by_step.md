## Step by Step Guide
If you're a beginner with 3D printers, with so much documentation to read, you might not know where to start. Don't worry, we'll go into the details of these documents next step by step. In a word, you need to do 4 steps **Install the machine - Printing test file - Slicing your own 3d file - Printing your 3d file**.      
First at all, please download the documents and save to your PC from [:arrow_down: this link](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK4#download-z9v5-mk4-files).
### Step 1. Install the machine
- 1.1 **Installation**. Refer to the [:blue_book: **installation guide**](./1.Installation_and_User_Guide/Z9V5Pro-MK4_Installation_and_User_Guide_EN.pdf) and [ :movie_camera: **installation video tutorial**](https://youtu.be/Xa3Q1m6HbDI) to complete the installation of the machine. The Z9V5 has a high pre-assembled ratio, so installation is very simple. 
- 1.2 **Wiring**. the process of wiring is basically to insert the plug into the corresponding socket. What you need to pay attention is to make sure the plug is fully inserted into the socket. Especially for those 2PIN docking sockets that sometimes make poor contact. In addition, for the wiring of the print head (hot end), please note that there are several sockets of the same type but different colors, please pay attention to plug them according to the color of the socket.
- 1.3 **Power ON**. When wiring is complete, you can [:movie_camera: **turn on Z9V5**](https://youtu.be/xTlMHtxkGoY). Please note in particular that the Z9V5 has 2 power switches. the one is ***AC switch***(the red switch on the back of the machine) and another is ***DC switch***(a round metal push button switch on the front of the machine control box), you need to turn on the AC switch first and then **press and hold** the DC switch for a few seconds to turn on Z9V5.
- 1.4 **Simply Test**. After power on, you can operate the menu on the LCD screen ([**LCD Menu description**](./1.Installation_and_User_Guide/LCD_DWIN_MENU_Description.md)) to verify whether the machine can work normally. Usually this involves several steps:
  - 1.4.1 **Prepare>>Auto Home>>Home All**. This step is to make the print head of the machine return to the origin.
  - 1.4.2 **Prepare>>Temperature>>Preheat PLA**. This step is to check the hot end and the hot bed can be heated normally.In this step, when the temperature of the nozzle exceeds 60 degrees, you should see a fan on the right side of the print head (hot end) spin up, this is the hot end cooling fan. 
  - 1.4.3 **Prepare>>Temperature>>FAN**. After pressing the knob and setting the fan speed (set to 255), you should now be able to turn the fan on the left side up as well.   
  After these 3 steps, it is basically determined that the machine are working normally, you can proceed to the following steps. If you find that any part is not working properly, please double check the wiring, or to do a auto testing (Refer to[ :movie_camera: **machine auto testing video turorial**](https://youtu.be/Mf92BlmKA0A)).
- 1.5 **Bed Level - leveling 4 corners of the bed**. Before printing the test file, you need to do a simple bed leveling to set the height between the nozzle and the bed (printing platform), so that the filament can be sticked on the hot bed well. Please refer to [:movie_camera: **Bed leveling video tutorial**](https://youtu.be/nxzB7ho1kNo) to do it.

### Step 2. Print test 3d model
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

### Step 3. Slicing your own 3d model
Obviously you will have the need to print your own 3D models. The process of converting a 3D model into a gcode file that can be printed on a machine is called slicing. You need to download and install the slicing software, then import the 3D model file (stl, obj, AMF, etc.) and complete the slicing, and finally copy the generated gcode file to the SD card and print it on the machine. Our recommended slicing software is PrusaSlicer. For detailed instructions, please refer to [4. Slicing](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK4#download-z9v5-mk4-files).   
Several of the most famous free 3D model download websites:
- [thingiverse](https://www.thingiverse.com/)  
- [printables](https://www.printables.com/)  
- [youmagine](https://www.youmagine.com/)   

### Step 4. Printing your own 3d model
Once you are done slicing, copy the obtained gcode files to your SD card, then you can print them out like in the [step 2](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK4#2-test-gcode).

### Step 5. To use advanced features
After you fully understand all the basic use of the machine, you can try some advanced functions of the machine. For details, please refer to [Advance features](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK4#2-test-gcode).

