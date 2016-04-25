

#define global commands
#ioin = 'sup test bro man'

def io(ioin):
    fullio = ioin.split()
    print ('Received:',fullio)

    if fullio[0] == 'walk':
        print('test')
    else:
        print('failed')
