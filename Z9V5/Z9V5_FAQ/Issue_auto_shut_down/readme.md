## The printer shut down when printing from SD card
1. Upload the newest firmware ([Download the newsst firmware](https://github.com/ZONESTAR3D/Firmware/tree/master/Z9/Z9V5/bin)) to the control board and try again.
2. Turn off the **PowerLoss Recovery** feature and try again (***Control>>Configre>>PowerLoss Recovery***).
3. Print another gcode file and try again.
4. Format the SD card and copy only one gcode file to SD card and print it again.
:warning: Sometimes the automatic shutdown is due to the quality of the SD card, not the gcode file itself. This causes a card reading error and shutdown.
5. Replace a new SD card (1~8G, format to FAT32) and try again.
6. [:link: Open the control box](../How_to_open_the_control_box.jpg) and check the wires which connected the AC connector to the power supply. Please check the yellow and black wires carefully, Check whether the connector is damaged or not tightly connected with the AC socket.
### :loudspeaker: :warning: Disconnect AC Power Before Checking.:warning:     
![](./AC_connector_wires.jpg)
### If you have tried all above steps and the question can't be fixed, please contact our technical support team : support@zonestar3d.com.