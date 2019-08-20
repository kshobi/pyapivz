#!/usr/bin/python3

def showInstructions():
    print('''
        RPG Game
        --------

        Commands:
        go [direction]
        get [item]

''')

def showStatus():
    print('--------------------')
    print(f"You are in the {currentRoom}")
    print("Inventory: " + str(inventory))
    if "item" in rooms[currentRoom]:
        print(f"you see a {rooms[currentRoom]['item']}")
    print("------------------")

inventory = []

rooms = {
               'Hall': {
                   'south': 'Kitchen',
                   'east': 'Dining Room'
               },
               'Kitchen': {
                   'north': 'Hall'
               },
               'Dining Room': {
                   'west':'Hall',
                   'south':'Garden',
                   'item':'cookies'
                   },
               'Garden':{
                   'north':'Dining room'
        }

currentRoom = 'Hall'

showInstructions()

while True:
    showStatus()
    move = ''
    while move=='':
        move= input("> ")
    move=move.lower().split()

    if move[0]=='go':
        if move[1] in rooms[currentRoom]:
            currentRoom=rooms[currentRoom][move[1]]
        else:
            print("You cannot go that way!")

    if move[0]=='get':
        if "items" in rooms[currentRoom] and move[1] in rooms[currentRoom]:
            inventory +=[move[1]]
            print(f"You just picked up {move[1]}!")
            del rooms[currentRoom]['item']
        else:
            print("You cannot pick that up!")
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        if 'cookies' in inventory:
        inventory.remove('cookies')
        del rooms[currentRoom]['item']
        print("A monster has you! game Over")
        break
    
    if currentRoom== 'Garden' and 'skeletonkey' in inventory:
        print(" You open the old rusty gate in the garden with the skeleton key escaped the house! You Win!")
        break























