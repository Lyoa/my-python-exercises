# Who Play's Basket Ball?

from  pickle import load, dump

def read_records():
    # We change to with to lessen the code instead of (infile = open('game.dat', 'rb')) 
    with open('game.dat','rb') as r_infile:
        with open('basket.dat', 'wb') as w_to_basket:
            #read to the end of file.

            while True:
                try:
                    #reading the object from file in binary form
                    participant = load(r_infile)

                    # Check if the key is Basket Ball
                    if participant[0] == 'Basket Ball':
                        # Transfer/Dump current participant line to basket.bat
                        dump(participant, w_to_basket)

                    else:
                        continue

                # Exception when it reaches the end of the file
                except EOFError:
                    break

# This is just a checker
def displayBinary(file):
    with open(file,'rb') as r_infile:
        while True:
                try:
                    #reading the object from file in binary form
                    current_file = load(r_infile)
                    #display the object
                    # print(current_file[0], current_file[1])
                    print(current_file)

                except EOFError:
                    break

read_records()

# Just to check if the function take effect
# displayBinary('game.dat')
displayBinary('basket.dat')