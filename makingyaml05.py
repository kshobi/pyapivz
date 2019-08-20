#!/usr/bin/python3


import yaml

def main():
    hitchhikers =  [{"name": "Zaphod Beebler","species":"betelgeusin"},
                    {"name": "author dent","species":"human"},
                    {"name": "Ford","species":None}
                   ]


    with open("zfile.yml", "w") as zfile:
        yaml.dump(hitchhikers,zfile)

    

main()
