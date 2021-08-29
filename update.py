import os
from sys import platform
path = os.getcwd()
parent = os.path.abspath(os.path.join(path, os.pardir))
os.chdir(parent)
print(os.getcwd())
print("MultiSSH update tool made by KrisIsHere | ver. 1.0")
xd = input("Would you like to update? (Y/N): ")
if xd in ["Y", "y"]:
    os.system("rm -rf MultiSSH ; git clone https://github.com/krisishere/MultiSSH")
    os.chdir(parent + "/MultiSSH")
    os.system("python3 multissh.py")
    exit()
else:
    print("ok")
    exit()
