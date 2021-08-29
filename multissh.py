import paramiko
import requests
import sys
import os
version = "0.95"
serv = [["192.168.0.103", "22", "joe", "bigchungus"], ["192.168.0.102", "8022", "mama", "password"]]

#TODO: SSH Keys

#Update
def update():
        path = os.getcwd()
        parent = os.path.abspath(os.path.join(path, os.pardir))
        os.system("cp -r update.py " + parent)
        os.system("python3 " + parent + "/update.py")
        sys.exit()

#Code for initiating the SSH connection
def simpleLogin(hostname, port, username, password):
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
    print("\n\033[0;92mBasic Multi-SSH control tool " + version + " \n\033[0;91mMade by KrisIsHere\033[0;00m\n\n")
    for x in serv:
        simpleLogin(x[0], x[1], x[2], x[3])
    while True:
        global verbose
        print("\n")
        command = input("$ ")
        for x in serv:
            sshCommand(x[0], x[1], x[2], x[3], command, verbose)

#Check for updates
def up_check():
    print('Checking for Updates.....', end='')
    ver_url = 'https://raw.githubusercontent.com/KrisIsHere/MultiSSH/main/version.txt'
    try:
        ver_rqst = requests.get(ver_url)
        ver_sc = ver_rqst.status_code
        if ver_sc == 200:
            github_ver = ver_rqst.text
            github_ver = github_ver.strip()

            if version == github_ver:
                print('\nUp-To-Date' + '\n')
                exit()
            else:
                print('\nAvailable: {}'.format(github_ver) + '' + '\n')
                up = input("Would you like to update? (Y/N): ")
                if up in ["y", "Y"]:
                    update()
                else:
                    exit()
        else:
            print('Status: {} '.format(ver_sc) + '' + '\n')
    except Exception as e:
        print('\nException: ' + str(e))
    exit()

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
    elif len(args) == 1 and args[0] in ["-u", "--update"]:
        up_check()
    else:
        print("""Error: Usage: python3 multissh.py [-h] [-s] [-l] [-u]

Arguments:
    -h, --help   | shows this help

    -s, --silent | does not show ssh output
    -l, --loud   | shows ssh output
    -u, --update | check for updates""")

main()
