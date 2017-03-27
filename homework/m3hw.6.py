# Binary Expansion (base 2)

import math

def base2(t):
    x = t
    binaryString = ''
    
    while x > 0:
        i = x % 2
        print(x, '/ 2 = ', math.floor(x / 2), 'with remainder', i)
        x = math.floor(x / 2)    
        binaryString = binaryString + str(i)
        
    print(binaryString[::-1])

def base16(t):
    x = t
    binaryString = ''
    intToLetter = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
        }
    
    while x > 0:
        i = x % 16
        print(x, '/ 16 = ', math.floor(x / 16), 'with remainder', i)
        x = math.floor(x / 16)

        if (i in intToLetter):
            print(i, '=', intToLetter[i])
            i = intToLetter[i]
        
        binaryString = binaryString + str(i)        
        
    print(binaryString[::-1])

def main():
    t = int(input('T = '))

    base2(t)

    base16(t)

main()


