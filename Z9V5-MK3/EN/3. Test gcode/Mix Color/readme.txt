//=================================================================
Modifying gcode file to realize automatic Gradient mixing
Step 1: slicing a single color stl file to gcode file, choose the the first extruder
Step 2: open the gcode file by Notepad, add M166 command to the gcode file (before start printing)

Example: GradientMix_Vase.gcode 
Open this file by Notepad, you can find we have added the below command at line 30
M166 S1 A0 Z100 I0 J1
/**
 * M166 command description
 *
 *   S[bool]  - Enable / disable gradients
 *   A[float] - Starting Z for the gradient
 *   Z[float] - Ending Z for the gradient. (Must be greater than the starting Z.)
 *   I[index] - V-Tool to use as the starting mix.
 *   J[index] - V-Tool to use as the ending mix.
 *
 */
//=================================================================

//=================================================================
Modifying gcode file to realize automatic random mixing
Step 1: slicing a single color stl file to gcode file, choose the the first extruder
Step 2: open the gcode file by Notepad, add M167 command to the gcode file (before start printing)

Example: RandomMix_Xmastree.gcode
Open this file by Notepad, you can find we have added the below command at line 30
M167 S1 A0 Z100 H5 E4

/**
 * M167 command description
 *
 *   S[bool]  - Enable / disable random mixing
 *   A[float] - Starting Z for the random mixing
 *   Z[float] - Ending Z for the random mixing. (Must be greater than the starting Z.)
 *   H[float] - Minimum height of changing mixing rate
 *   E[int] - how many extruders used on random mixing 
 */
//=================================================================