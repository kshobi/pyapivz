#!/usr/bin/python3

import requests
import pprint

def main():
    r=requests.get('https://www.anapioficeandfire.com/api')
    pprint.pprint(r.json())
    print(r.yaml())
main()




