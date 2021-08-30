# MultiSSH
A tool that allows you to control more than one SSH server at the same time.

# What is MultiSSH?
MultiSSH is a simple python project that allows you to connect and control more than one SSH server at the same (Send the same command to more than 1 server at once)

# How to install and run?
First install dependencies

```$ pip3 install paramiko requests```

then git clone the repo.

```$ git clone https://github.com/KrisIsHere/MultiSSH```

then cd into it

```$ cd MultiSSH```

then run it by typing

```$ python3 multissh.py```

# How to add a server?
Line 1:

  ```serv = [["192.168.0.103", "22", "joe", "password"], ["192.168.0.102", "8022", "mama", "fat"]]```

# Config options
To get an up-to-date help document of MultiSSH, just run ```python3 multissh.py -h```.

- -s, --silent
  
  Does not show command output
- -l, --loud
  
  Shows command output
- -u, --update
  
  Check for updates
- -o, --outlog
  
  log output of silent mode in a file (a bit buggy)
