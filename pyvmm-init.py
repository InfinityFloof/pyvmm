import os
print("In order for Pyvmm to work, you need a vm. Please add a vm.")
command = "echo '"
command_end = "' > data.txt"
name = input("VM Nickname $ ")
script = "./" + input("VM Script Name $ ") + ".sh"
os.system("touch data.bak.txt")
os.system(f'{command}[["{name}", "{script}"]]{command_end}')