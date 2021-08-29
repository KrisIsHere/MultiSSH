import paramiko
import sys
serv = [["192.168.0.103", "22", "joe", "bigchungus"], ["192.168.0.102", "8022", "mama", "password"]]

#TODO: SSH Keys

#Code for initiating the SSH connection
#Variable "compteur" (Maybe a mispelling of computer?) is only refrenced once here and never used
def simpleLogin(hostname, port, username, password, compteur):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname, port, username, password)
        print(hostname, "was \033[0;92mconnected \033[0;00msuccesfully")
    except:
        print(hostname, "\033[0;91mcannot connect\033[0;00m")

#Code for sending SSH Commands
def sshCommand(hostname, port, username, password, command, verbose):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname, port, username, password)
        stdin, stdout, stderr = client.exec_command(command)
        if verbose:
            print(stdout.read().decode())
    except:
        print("Error")

#A continuation of main()
def main1(serv):
    print("\n\033[0;92mBasic Multi-SSH control tool 0.90 \n\033[0;91mMade by KrisIsHere\033[0;00m\n\n")
    for x in range(len(serv)):
        simpleLogin(serv[x][0], serv[x][1], serv[x][2], serv[x][3], x+1)
    while True:
        global verbose
        print("\n")
        if choice == "y":
            command = input("$ ")
            for x in range(len(serv)):
                sshCommand(serv[x][0], serv[x][1], serv[x][2], serv[x][3], command, "y")
        else:
            command = input("$ ")
            for x in range(len(serv)):
                sshCommand(serv[x][0], serv[x][1], serv[x][2], serv[x][3], command, "n")

#Parsing command arguments
def main():
    global verbose
    args = sys.argv[1:]
    if len(args) == 1 and args[0] in ["-s", "--silent"]:
        verbose = False
        main1(serv)
    elif len(args) == 1 and args[0] in ["-l", "--loud"]:
        verbose = True
        main1(serv)
    else:
        print("""Error: Usage: python3 multissh.py [-h] [-s] [-l]

Arguments:
    -h, --help   | shows this help

    -s, --silent | does not show ssh output
    -l, --loud   | shows ssh output""")

main()
