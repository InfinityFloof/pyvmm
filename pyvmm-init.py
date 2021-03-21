import os
path = f"{os.path.dirname(__file__)}/"
os.system(f"mkdir {path}VMsh")
print("                                                                    /$$           /$$   /$$    ")
print("                                                                   |__/          |__/  | $$    ")
print("  /$$$$$$  /$$   /$$ /$$    /$$ /$$$$$$/$$$$  /$$$$$$/$$$$          /$$ /$$$$$$$  /$$ /$$$$$$  ")
print(" /$$__  $$| $$  | $$|  $$  /$$/| $$_  $$_  $$| $$_  $$_  $$ /$$$$$$| $$| $$__  $$| $$|_  $$_/  ")
print("| $$  \ $$| $$  | $$ \  $$/$$/ | $$ \ $$ \ $$| $$ \ $$ \ $$|______/| $$| $$  \ $$| $$  | $$    ")
print("| $$  | $$| $$  | $$  \  $$$/  | $$ | $$ | $$| $$ | $$ | $$        | $$| $$  | $$| $$  | $$ /$$")
print("| $$$$$$$/|  $$$$$$$   \  $/   | $$ | $$ | $$| $$ | $$ | $$        | $$| $$  | $$| $$  |  $$$$/")
print("| $$____/  \____  $$    \_/    |__/ |__/ |__/|__/ |__/ |__/        |__/|__/  |__/|__/   \___/  ")
print("| $$       /$$  | $$                                                                           ")
print("| $$      |  $$$$$$/                                                                           ")
print("|__/       \______/                                                                            ")
print("")
print("In order for Pyvmm to work, you need a sh file that starts your VM, please put these in the newly generated VMsh directory and register it down here.")
command = "echo '"
command_end = f"' > {path}data.txt"
name = input("VM Nickname $ ")
script = input("Script Name (Do not include .sh) $ ")
os.system(f"touch {path}data.bak.txt")
os.system(f'{command}[["{name}", "{script}"]]{command_end}')
print("Run this program again to run pyvmm")