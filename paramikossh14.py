#!/usr/bin/python3

import paramiko
import getpass


def cmdtoissue(sshsession, command_to_issue):
    ssh_stdin,ssh_stdout,ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read().decode('UTF-8')



def main():
    sshsession=paramiko.SSHClient()
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    mypass=getpass.getpass("Password: ")
    sshsession.connect(hostname="10.10.2.3",username="bender",password=mypass)

    mycommands = ["touch sshworked.txt","uptime","whoami","date","hostname"]

    for x in mycommands:
        print(cmdtoissue(sshsession,x))

    sshsession.close()

main()












