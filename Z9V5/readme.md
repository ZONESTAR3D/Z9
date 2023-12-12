# User Guide for ZONESTAR Z9V5 3D Printer 

-----
### :globe_with_meridians: Translate
We provide online documentation for files precisely because it is easy to translate into languages you are familiar with. Below, we list some common browser translation add-ons for your reference.
- [**Windows Edge Translate Add-on**](https://microsoftedge.microsoft.com/addons/detail/edge-translate/bfdogplmndidlpjfhoijckpakkdjkkil?hl=en-US)    
- [**Firefox Translations Add-on**](https://support.mozilla.org/en-US/kb/firefox-translations-add-on?redirectslug=firefox-translations&redirectlocale=en-US)
- [**Google Translate Chrome Extension**](https://chrome.google.com/webstore/detail/google-translate/aapbdbdomjkkjkaonfhkkikfgjllcleb)

-----
### User Guide for Z9V5Pro 3D Printer 
- :file_folder: Z9V5Pro-MK6 User Guide: https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6
- :file_folder: Z9V5Pro-MK5 User Guide: https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK5
- :file_folder: Z9V5Pro-MK4 User Guide: https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK4
- :file_folder: Z9V5Pro-MK3 User Guide: https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK3
- :file_folder: Z9V5Pro-MK2 User Guide: https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK2
- :file_folder: Z9V5Pro-MK1 User Guide: https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK1

-----
### How to distinguish Z9V5-MK1/MK2/MK3/MK4/MK5/MK6
You can distinguish MK1/MK2/MK3/MK4 by product serial number. There is a white sticker on the power supply, which indicates the product serial number.  
![](Z9V5_SN.jpg)
- **Z9V5-MK1:** Serial Number is **xxxxxxxxxx**   
- **Z9V5-MK2:** Serial Number is **V1-xxxxxxxxxx** and **V2-xxxxxxxxxx**    
- **Z9V5-MK3:** Serial Number is **MK3-xxxxxxxxxx**  
- **Z9V5-MK4:** Serial Number is **MK4-xxxxxxxxxx**  
- **Z9V5-MK5:** Serial Number is **MK5-xxxxxxxxxx**  
- **Z9V5-MK6:** Serial Number is **MK6-xxxxxxxxxx**  

-----
### What's different on Z9V5-MK1/MK2/MK3/MK4/MK5/MK6
#### Z9V5-MK6 mainly improves than Z9V5-MK5:    
:green_book: [**Z9V5-MK6 User Guide**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK6)    
1. Upgrade to Dual Gear Extruders (2x BMG left hand and 2x BMG right hand).
2. Upgrade control board to ZM3E4 V3.0.1.     

#### Z9V5-MK5 mainly improves than Z9V5-MK4:  
:green_book: [**Z9V5-MK5 User Guide**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK5)    
Used M4V6 (the 6th version 4-IN-1-OUT mix color) hotend as default hotend to replace of the E4 hotend.   
**[What's different between M4V6 hotend and E4 hotend](https://github.com/ZONESTAR3D/Upgrade-kit-guide/blob/main/HOTEND/FAQ_M4E4.md#whats-different-between-e4-and-m4-hotend).**     

#### Z9V5-MK4 mainly improves than Z9V5-MK3:  
:green_book: [**Z9V5-MK4 User Guide**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK4)    
1. Use E4 (4-IN-1-OUT non mix color) hotend as default hotend to replace of the M4V4 (the 4th version 4-IN-1-OUT mix color) hotend.
2. Use magnetic hot bed sticker to replace hot bed glass.
3. Bed leveling sensor used PL-08N.
4. Optimized structure on top assembly, filament run out sensor case, etc..    

#### Z9V5-MK3 mainly improves than Z9V5-MK2:
:green_book: [**Z9V5-MK3 User Guide**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK3)
1. Upgraded bed leveling sensor to [**ZLSensor**](https://aliexpress.com/item/1005002865311470.html) from [**PL-08N**](https://www.aliexpress.com/item/2255800409994958.html) bed leveling sensor. ZLSensor can probing the glass directly.  
2. Upgraded the extruder motor drivers to [**TMC2225**](https://aliexpress.com/item/1005003270721219.html) from [**A4988**](https://www.aliexpress.com/item/2255800771058461.html).     

#### Z9V5-MK2 mainly improves than Z9V5-MK1:    
:green_book: [**Z9V5-MK2 User Guide**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK2)  
1. **Hot end interface** When shipping, the print head (hotend assembly) is separated from the backplane. There are 5 connectors behind the backplane, which can connect the wiring of the hot end without opening the control box. It will help switch between [**different types of hotends**](https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND) quickly.    
2. Improved the M4 hotend from the 2nd version (***M4-V2***) to the 3rd version(***M4-V3***). More details of the M4 hotend, please refer to [Here](https://github.com/ZONESTAR3D/Upgrade-kit-guide/tree/main/HOTEND/M4%20%204-IN-1-OUT%20Mixing%20Color%20Hotend).  
3. Improved the backlight of ZONESTAR LOGO.  
4. Improved the cover case of control box to make it easier to open.  
5. improved the belt transmission device to prevent the belt from scratching the idler pulley.  
6. improved the filament run out installation to make it solve the problem that may lead to the winding of filament.    
:warning: **NOTE** :warning:   
Due to the shortage of chips, a small numbers of **Z9V5-MK2** used **ZM3E4V1** control board. Please check the product serial number (a white lable pasted on the power supply). If the product with serial number **V1xxxxxxxx** , it means your machine used a **ZM3E4V1** control board. Basically ZM3E4V1 has the same features with ZM3E4V2.        

#### Z9V5-MK1 is the first version Z9V5    
:green_book: [**Z9V5-MK1 User Guide**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5-MK1) 

-----
### Troubleshooting
If you have any problem when installing and using Z9V5, please read the [**:book:Document of Z9V5 Troubleshooting**](https://github.com/ZONESTAR3D/Z9/tree/main/Z9V5/Z9V5_FAQ/readme.md) to find a solution a solution first.


