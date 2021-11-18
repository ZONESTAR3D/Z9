# Z9M3 
Installation guide, user guide, slicing guide and testing gcode file for Z9M3 3d printer  
***Note***
---
1. Z9M3 use a ZRIBV6 control board, 3 extruders and a M3 hotend, it used a 128x64 dots LCD screen
2. from the 4nd version Z9M3(Z9F), it upgrade the extduer to a Titan extruders


# Z9M4 
Installation guide, user guide, slicing guide and testing gcode file for Z9M4 3d printer  
***Note***
---
Default Z9M4 use a 32bits ZM3E4V1 control board, 4 extruders and a M4 hotend, it used a 128x64 dots LCD screen

# Z9V5(-MK1) 
Installation guide, user guide, slicing guide and testing gcode file for Z9V5/Z9V5Pro 3d printer  
***Note***
---
1. Default Z9V5 used a 32bits ZM3E4V2 control board, 4 extruders and a M4 hotend, it used a 128x64 dots LCD screen
2. Default Z9V5Pro used a 32bits ZM3E4V2 control board, 4 extruders and a M4 hotend, it used a 4.3" TFT-LCD screen

# Z9V5-MK2 
Installation guide, user guide, slicing guide and testing gcode file for Z9V5Pro-MK2 3d printer   
*Note*
---
1. Z9V5-MK2 mainly improves the hot end interface. When shipping, the print head (hotend) is separated from the backplane. There are 5 connecotor behind the backplane, which can connect the wiring of the hot end without opening the control box.
2. Due to the shortage of chips, a small number of Z9V5-MK2 used ZM3E4V1 control board. Please check the product serial number (pasted on the power supply of the backplane). If the product with serial number V1-XXXXXX is displayed, the machine uses ZM3E4V1 control board.

# Z9V5-MK3 
Installation guide, user guide, slicing guide and testing gcode file for Z9V5Pro-MK3 3d printer  
***Note***
---
1. Z9V5-MK3 improved bed leveling sensor to ZLSensor, to replace the PL-08N bed leveling sensor. ZLSensor can probing the glass directly.
2. Z9V5-MK3 used TMC2225 to replace A4988 on the extruders motor driver, so it need to use a different firmware with Z9V5 and Z9V5MK2.(Firmware version is above V2.0)