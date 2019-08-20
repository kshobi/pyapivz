#!/usr/bin/python3


import json

def main():
    hitchhikers =  [{"name": "Zaphod Beebler","species":"betelgeusin"},
                    {"name": "author dent","species":"human"},
                    {"name": "Ford","species":None}
                   ]


    with open("galaxyguide.json", "w") as zfile:
        json.dump(hitchhikers, zfile)

    myhitchhikers = json.dumps(hitchhikers)

    print(myhitchhikers)

main()
