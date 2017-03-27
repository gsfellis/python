# Bacon's Code

import math

def removeSpaces(msg):
    return msg.upper().replace(' ', '')

def dummyHasChars(dummyMsg, chars):
    return len(dummyMsg.strip().replace(' ', '')) == chars

def base2(t):
    x = t
    binaryString = ''
    
    while x > 0:
        i = x % 2
        #print(x, '/ 2 = ', math.floor(x / 2), 'with remainder', i)
        x = math.floor(x / 2)    
        binaryString = binaryString + str(i)

    if len(binaryString) < 5:
        binaryString = binaryString + '0' * (5 - len(binaryString))
            
    return binaryString[::-1]

def letterToNumber(ltr):    
    return ord(ltr.upper()) - 65

def updateDummyMsg(bs, msg):  
    codedMsg = ''
    i = 0   

    while i < len(bs):
        if bs[i] == '1':
            codedMsg = codedMsg + msg[i].upper()
        else:
            codedMsg = codedMsg + msg[i].lower()
        i = i + 1

    return codedMsg    

def makeBinaryString(msg): 
    binaryString = ''
    
    for c in msg:
        binaryString = binaryString + base2(letterToNumber(c))
        
    return binaryString

def printTable(msg, bs, dMsg):
    print(msg.replace('', '    ').strip())
    print(' '.join(bs[i:i+5] for i in range(0, len(bs), 5)))
    print(' '.join(dMsg[i:i+5] for i in range(0, len(dMsg), 5)))         

def main():
    dummyMsg = ''

    msg = input('Enter message to encode: ')

    msgNoSpaces = removeSpaces(msg)
    chars = len(msgNoSpaces)
    charsNeeded = len(msgNoSpaces) * 5
    
    print('')
    print('Your dummy message should contain', charsNeeded, 'characters.')

    print((" " * 21) + ('-' *+ charsNeeded)) 
    while not dummyHasChars(dummyMsg, charsNeeded):
        dummyMsg = input('Enter dummy message: ')

    dummyMsgNoSpaces = removeSpaces(dummyMsg)
    print(dummyMsgNoSpaces)

    binaryString = makeBinaryString(msgNoSpaces)
    print(binaryString)

    codedDummyMsg = updateDummyMsg(binaryString, dummyMsgNoSpaces)

    print('')
    print(msgNoSpaces)
    print(binaryString)
    print(codedDummyMsg)

    printTable(msgNoSpaces, binaryString, codedDummyMsg)
        
main()

    
    

    

    

          
    
