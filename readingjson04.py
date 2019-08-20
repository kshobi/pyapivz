#!/usr/bin/python3

import json

def main():
    with open("datacenter.json","r") as datacenter:
        datacenterst= datacenter.read()
        
    print(type(datacenterstr))
    datacenterdict= json.loads(datacenterstr)

    print(datacenterdict["row1"])



main()
