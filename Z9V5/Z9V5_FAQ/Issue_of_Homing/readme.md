## Homing Issues
First please follow the [:movie_camera:**electronics parts auto testing video tutorial**](https://youtu.be/Mf92BlmKA0A) to check the ENDSTOPs and motors, if you find a problem during testing, follow the steps below to identify where the problem came from.  
:warning: Please note that because the Z9 uses the CoreXY structure, when testing the XY motors, the print head (hotend) will only move left and right in the X direction.

### Homing X issue
If X ENDSTOP and XY motors works well, but when homing X, the print head (hotend housing) can't touch the X ENDSTOP, please refer to the picture below to slightly correct the tongue of the X now switch.    
![](correct_x_switch.jpg)

### :one: X ENDSTOP or motor don't work?
- **X ENDSTOP doesn't work?**  
1. Check X ENDSTOP wiring.    
2. Check X wiring on the control boad.   
3. Check that the X limit switch is well soldered to the wire and that the wire is connected to the NO and COM pins of the limit switch.   
![](x_endstop_wring.jpg) ![](xy_wiring_board.jpg) ![](X_limitswitch.jpg)
- **X Motor doesn't work?**  
1. Check X motor wiring.    
2. Check X wiring on the control boad.   
![](x_motor_wring.jpg) ![](xy_wiring_board.jpg)

### :two: Y ENDSTOP or motor don't work?
- **Y ENDSTOP doesn't work?**  
1. Check Y ENDSTOP wiring.    
2. Check Y wiring on the control boad.   
3. Check that the Y limit switch is well soldered to the wire and that the wire is connected to the NO and COM pins of the limit switch.
![](y_endstop_wring.jpg)  ![](xy_wiring_board.jpg) ![](y_limitswitch.jpg)
- **Y Motor doesn't work?**  
1. Check Y motor wiring.    
2. Check Y wiring on the control boad.   
![](y_motor_wring.jpg) ![](xy_wiring_board.jpg)

### :three: Z ENDSTOPs or motors don't work?
:loudspeaker:Because the Z axis has 2 sets of drive system (the left and the right), so if you find a problem with the Z, you can swap the wiring on the left and right to confirm whether the problem is from the control board side or the motor/ENDSTOP side.   
:warning: For Z axis, the two sets (left and right) of ENDSTOPS + Motor must be matched. If you exchange one of them (for example, the left and right ENDSTOP wiring is exchanged but the motor wiring is not ), it will also cause the Z axis to fail to home.  
- **ZL/ZR ENDSTOPs don't work?**  
1. Check Z ENDSTOPs wiring (Both the left and right).    
2. Check the Z ENDSTOPs PCBA  (Both the left and right). :warning: Please pay attention to check the Z limit switch circuit board for damage or accidental poor soldering.   
![](Z_endstop_wring.jpg) ![](Z_endstop.jpg)
- **ZL/ZR Motor don't work?**  
1. Check Z(L/R) motor wiring.    
2. Check Z(L/R) Motor wiring on the control boad.   
![](Z_motor_wring.jpg) ![](Z_wiring_board.jpg)
