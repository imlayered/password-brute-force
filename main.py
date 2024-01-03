import subprocess
import sys

def open_terminal_and_run_script(script_name, value):
    try:
        command = f'python3 {script_name}; read -p "Press enter to close | Software by Layered (bagel.land)"'

        # For GNOME terminal
        subprocess.Popen(['gnome-terminal', '--', '/bin/bash', '-c', command])
    except FileNotFoundError:
        try:
            # For other terminal (like xterm)
            subprocess.Popen(['xterm', '-e', command])
        except FileNotFoundError:
            print("Terminal not found", file=sys.stderr)

def write_value_to_file(value, file_name):
    with open(file_name, 'w') as file:
        file.write(value)

input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNOTE: If main.py does not work on your OS (I've tested on Ubuntu), run common.py and random.py seperately.\n\n\n\nDeveloped by Layered (bagel.land) \n Disclaimer: This program is intended for educational purposes. Use legally.\n\n Click enter to start...")

value = input("Enter your password: ")

write_value_to_file(value, "result.txt")

open_terminal_and_run_script('common.py', value)
open_terminal_and_run_script('random.py', value)



#
#  _                               _ 
# | |                             | |
# | | __ _ _   _  ___ _ __ ___  __| |
# | |/ _` | | | |/ _ \ '__/ _ \/ _` |
# | | (_| | |_| |  __/ | |  __/ (_| |
# |_|\__,_|\__, |\___|_|  \___|\__,_|
#           __/ |                    
#          |___/                     Developed on January 2nd, 2023. See github.com/imlayered for updates. Please leave this credit in <3 | 
