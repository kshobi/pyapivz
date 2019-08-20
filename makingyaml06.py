#!/usr/bin/python3


import yaml

def main():
    hitchhikers =  [{"name": "Zaphod Beebler","species":"betelgeusin"},
                    {"name": "author dent","species":"human"},
                    {"name": "Ford","species":None}
                   ]


    mystr= yaml.dump(hitchhikers)
    print(mystr)
    

main()
