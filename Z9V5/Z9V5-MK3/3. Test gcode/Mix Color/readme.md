## How to realize gradient color by modifying gcode file? 
- Step 1: slicing a single color stl file to gcode file, choose the the first extruder.  
- Step 2: open the gcode file by Notepad, add M166 command to the gcode file (before start printing)  
#### Example: GradientMix_Vase.gcode 
Open this file by notepad, you can find we added the below command at line 30:  
**M166 S1 A0 Z100 I0 J1**     
>
    M166 command description  
    S[0/1]  - Enable / disable gradients  
    A[number] - Starting Z height  
    Z[number] - Ending Z height. (Must be greater than the starting Z.)  
    I[number] - V-Tool to use as the starting mix.  
    J[number] - V-Tool to use as the ending mix.  

## How to realize multiple stages gradient color by using Cura plug-in?
Please refer to [here](https://github.com/ZONESTAR3D/Slicing-Guide/tree/master/cura/plugins).

----
## How to realize random mixing by modifying gcode file? 
- Step 1: slicing a single color stl file to gcode file, choose the the first extruder.  
- Step 2: open the gcode file by Notepad, add M167 command to the gcode file (before start printing)  
#### Example: RandomMix_Xmastree.gcode
Open this file by Notepad, you can find the below command has been add at line 30  
**M167 S1 A0 Z100 H5 E4**   
>
    M167 command description   
    S[0/1]  - Enable / disable random mixing    
    A[number] - Starting Z height    
    Z[number] - Ending Z height. (Must be greater than the starting Z.)    
    H[number] - Minimum height of changing mixing rate   
    E[number] - how many extruders used on random mixing   

