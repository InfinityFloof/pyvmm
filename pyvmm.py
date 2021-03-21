import os, sys
path = "/home/alex06/Documents/Python/pyvmm/"

if os.path.exists(f"{path}data.txt") == False:
    os.system(f"python {path}pyvmm-init.py")
    quit()
if os.path.getsize(f"{path}data.txt") == 0:
    os.system(f"cp {path}data.bak.txt {path}data.txt")
    print("Backup loaded")

# Actually the start of the program
os.system(f"cp {path}data.txt {path}data.bak.txt")
print("  /$$$$$$  /$$   /$$ /$$    /$$ /$$$$$$/$$$$  /$$$$$$/$$$$ ")
print(" /$$__  $$| $$  | $$|  $$  /$$/| $$_  $$_  $$| $$_  $$_  $$")
print("| $$  \ $$| $$  | $$ \  $$/$$/ | $$ \ $$ \ $$| $$ \ $$ \ $$")
print("| $$  | $$| $$  | $$  \  $$$/  | $$ | $$ | $$| $$ | $$ | $$")
print("| $$$$$$$/|  $$$$$$$   \  $/   | $$ | $$ | $$| $$ | $$ | $$")
print("| $$____/  \____  $$    \_/    |__/ |__/ |__/|__/ |__/ |__/")
print("| $$       /$$  | $$                                       ")
print("| $$      |  $$$$$$/                                       ")
print("|__/       \______/                                        ")
while True:
    print("")
    print("")
    print("0 = Save and Exit")
    print("1 = Open VM")
    print("2 = Import VM")
    print("3 = Remove VM")
    print("")
    data_file = open(f"{path}data.txt")
    vm_matrix = eval(data_file.read())
    data_file.close()
    data_file = open(f"{path}data.txt", "w+")
    thechosenone =  int(input("Choose operation $ "))
    if thechosenone == 0:
        print("Closing...")
        data_file.write(str(vm_matrix))
        os.system(f"cp {path}data.bak.txt {path}data.txt")
        break
    if thechosenone == 1:
        print("")
        print("Available VMs:")
        for gen in range(len(vm_matrix)):
            print(f"ID {gen}: {vm_matrix[gen][0]}")
        print("")
        vm_open = int(input("Choose (ID) $ "))
        print("")
        print(f"Opening {vm_matrix[vm_open][0]}...")
        os.system(f"cd {path}VMsh && chmod +x {vm_matrix[vm_open][1]}.sh && ./{vm_matrix[vm_open][1]}.sh")
        data_file.write(str(vm_matrix))
    if thechosenone == 2:
        print("")
        name_import = input("VM Nickname $ ")
        script_import = input("Script name (Do not include .sh) $ ")
        write_str = vm_matrix + [[name_import, script_import]]
        print(write_str)
        data_file.write(str(write_str))
    if thechosenone == 3:
        print("")
        print("Available VMs to remove:")
        for gen in range(len(vm_matrix)):
            print(f"ID {gen}: {vm_matrix[gen][0]}")
        print("")
        vm_del = int(input("Choose (ID) $ "))
        if input("Do you want to delete the sh file? [y/n] $ ").lower() == "y":
            os.system(f"rm {path}VMsh/{vm_matrix[vm_del][1]}.sh")
            print(".sh file removed")
        vm_matrix.pop(vm_del)
        write_str = vm_matrix
        data_file.write(str(write_str))
        print("VM deleted from Catalogue")