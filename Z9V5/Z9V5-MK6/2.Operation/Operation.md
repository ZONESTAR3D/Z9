# Operation guide
Before start printing, you need to level the hot bed (fine tune the distance between the nozzle and the printing platform) and load the filaments into the extruders and hot end.
## Leveling the hot bed
#### [:clapper:Video Tutorial](https://youtu.be/nxzB7ho1kNo)
#### :warning: **For FDM3D printers, the distance between the nozzle and the hot bed is very important when printing the first layer.** If the distance is too close, the filaments cannot flow out of the nozzle, and even damage the nozzle and the hot bed. If the distance is too far, the filaments cannot pasted on the hot bed, the next layers cannot be stacked correctly and cause printing fail.
- Step 1. Power on the 3d printer and then do “Prepare>>Auto Home>>Home All” on LCD MENU, wait the hotend go to the HOME position. 
- Step 2. Tighten the hand nuts under the bed to move down the bed to the lowest position (Fig 1).
- Step 3. Do “Prepare>> Bed leveling>> Point 1” on control panel(Fig 2), the nozzle will go to the corners of the bed, loosen the hand nuts under the hotbed (Fig 3) and let the nozzle almost touch the hotbed (Fig 4). Continue to do “Point 2/3/4” until all of the 4 corners has been leveled.
- Step 4. Repeat Step 3 and do 2 ~ 3 rounds, until all of the four corners at the same height.   
![](./Operation/levelbed.png)

-----
## Load filaments
#### [:clapper:Video Tutorial](https://youtu.be/KZQdL7Rgy1s)
This printer is equipped with four extruders and one 4-IN-1-OUT color mixing hot end. The extruders and the hot end are connected by a filament guide (PTFE tube). ***Before printing, you need to load all 4 filaments to the extruders and feed them into the bottom of the hot end.*** 
- Step 1. Do “Prepare>>Auto Home>>Home All” on control panel, and then do “Prepare>>Temperature>> Preheat PLA”, waiting nozzle temperature reached to 190 ℃ (Fig 1).
- Step 2. Use a diagonal pliers to cut off the head of filament (Fig 2), and then press the handle of the extruder#1 and insert filament, push the filament until you can see the filament in the PTFE guide (Fig 3). Rotate the gear of extruder #1 (Fig 4), watch the filament until it entered bottom of the hot end. 
- Step 3. Using the same method as in step 2 to load the filaments to extruder#2 ~ extruder#4, watch the filaments until them entered the bottom of hot end.
- Step 4. Slowly rotate the gear of extruder#1 ~ extruder#4 one by one and watch the nozzle, until you can see the filament flowed out from the nozzle(Fig 5).
![](./Operation/loadfilament.png)

-----
## Print your "Hellow World"" works
<!-- [:clapper:Video Tutorial]()          -->
- Step 1. Insert the SD card to the SD card socket on the printer (Fig 1).
- Step 2. Click “Print” on the control panel and choose “Test gcode\xyz_cube.gcode” (Fig 2), click the knob to start printing.
- Step 3. Wait until the hotend and hotbed is reached to the setting temperature (Fig 3), the nozzle will home to the origin position and then move to above of the printing platform and extrude the filament, use a tweezers to remove the outflow filament (Fig 4).
- Step 4. When the nozzle moved to the hot bed and start to print, double click the knob on the control panel to open a “Baby steps Z” menu (Fig 5), rotate knob slowly to fine tune the height of printing platform, watch the distance from nozzle to bed, until the distance goes well (Fig 6). Wait the printing finished, you will get your first works (Fig 7).
 Step 5. Wait the hotbed cool (<=25 degree) (Fig 8), and then remove the printed object from the hotbed (Fig 9).
![](./Operation/firstprint.png)

-----
## :fireworks: Congratulate! 
After printed the first works, you have a basic understanding of how the 3d printer works. Next, you can print other test files or slice your own 3D model and use the machine to print it out.    
It is recommended that you download and install the slicing software, and read the user guide of the slicing software to know how to use it,for details, please refer to the "Slicing Guide".
- [**:book: Slicing Guide Online Document**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6/4.Slicing).
- [**:blue_book: Slicing Guide pdf file**](../4.Slicing/readme.pdf).
