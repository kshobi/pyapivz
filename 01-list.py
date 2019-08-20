#!/usr/bin/python3

def main():
    mylist=["bert",55,"juniper","cisco",["bigip","meraki","dell"]]
    print("My primary network providers are " + mylist[2] + " "+ mylist[3] + ".")
    print(f"My primary network providers are {mylist[2]} {mylist[3]}.")
    print(mylist[4][1])


if __name__=="__main__":
    main()

