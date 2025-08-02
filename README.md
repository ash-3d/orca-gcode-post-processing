# orca-gcode-post-processing
Find and replace orca gcode post processing using python script

This is a simple python script for finding 'X-Find-X' and replace it with 'X-Replace-X'. In the place of X-Find-X and X-Replace-X, you can insert the specific command. For eg. Find M201 and replace it with ;M201.
Follow the below steps to configure it with Orca Slicer or PrusaSlicer.

Step 1:
Install python on your computer from https://www.python.org/

Step 2:
Download the python script(find_replace.py) and copy it to your local machine. For eg. C:\python_scripts

Step 3:
In the slicer, go to the post-processing field. Type the address of the python.exe and after a space address of the py script. The example below is an example. You have to make necessary changes based on your user name in your computer and the version of pythonn installed.
Eg. C:\Users\YOUR_USER_NAME\AppData\Local\Programs\Python\Python3XX\python.exe C:\python_scripts\find_replace.py;

Step 4:
Slice any part and when you export G-code file the script wil be called and the saved file will have necessary commands replaced.
