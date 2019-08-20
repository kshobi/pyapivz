#!/usr/bin/python3

import paramiko
import getpass


# shortcut to issing commands
def commandissue(sshsession, command_to_issue):
    ssh_stdin,ssh_stdout,ssh_stderr = sshsession.exec_command(command_to_issue)
    return ssh_stdout.read().decode('UTF-8')


# shortcut to gathering targets
def gettargets():
    targetlist= []
    targetip=input("What is the IP address you would like to connect to? ")
    targetlist.append(targetip)
    targetuser=input("What UN would you like to use to connect? ")
    targetlist.append(targetuser)
    return targetlist


def main():
    connectionlist=[]
    while True:
        connectionlist.append(gettargets())
        zvarquit=input("Do you want to continue y/N: ")
        if zvarquit.lower()== 'n' or zvarquit == "":
            break



    reqfile= input("What is the full path of the requirements file? PRESS ENTEr for default")
    if reqfile == "":
        reqfile= "requirement.txt"

    sshsession=paramiko.SSHClient()
    mykey=paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for x in range(len(connectionlist)):
        sshsession.connect(hostname=connectionlist[x][0],username=connectionlist[x][1],pkey=mykey)
        print(commandissue(sshsession,"ls"))
        ftp_client=sshsession.open_sftp()
        ftp_client.put(reqfile,reqfile)
        ftp_client.close()
        print(commandissue(sshsession,"ls"))

        commandissue(sshsession,"sudo apt-get update -y ")
        print(commandissue(sshsession,"sudo apt install python3-pip -y"))
        print(commandissue(sshsession,"python3 -m pip install -r " + reqfile))


#if__name__== "__main__":
main()












