import os, sys
path = "/home/alex06/Documents/Python/pyvmm/"
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
    print("4 = Load backup")
    print("")
    data_file = open(f"{path}data.txt")
    vm_matrix = eval(data_file.read())
    data_file.close()
    data_file = open(f"{path}data.txt", "w+")
    thechosenone =  int(input("Choose your fate anakin $ "))
    if thechosenone == 0:
        print("Closing...")
        data_file.write(str(vm_matrix))
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
        os.system(vm_matrix[vm_open][1])
        data_file.write(str(vm_matrix))
    if thechosenone == 2:
        print("")
        name_import = input("Name of VM $ ")
        script_import = "./" + input("Script name $ ") + ".sh"
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
        vm_matrix.pop(vm_del)
        write_str = vm_matrix
        data_file.write(str(write_str))
        print("VM deleted from Catalogue")
    if thechosenone == 4:
        os.system(f"cp {path}data.bak.txt {path}data.txt")
        print("Backup loaded")
        break