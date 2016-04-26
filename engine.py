

#define global commands
#ioin = 'sup test bro man'

def io(ioin):#function to retrieve input from flask, which flask gets from game.html
    fullio = ioin.split()#output stuff for debug
    print ('Received:',fullio)

    if fullio[0] == 'walk' or fullio[0] == 'go':#create possible 'first verb' commands
        print('test')
    else:
        print('failed')
