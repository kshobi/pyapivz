#!/usr/bin/python3

def main():
    while True:
        try:
            name=input("Enter the name of the file: ")
            with open(name, 'w') as myfile:
                myfile.write("This worked")

        except:
            print("Error with THST file name.....trying again.....")
            
        else:
            break

    print("Thanks for making that simple file")

if __name__=="__main__"
main()
















































