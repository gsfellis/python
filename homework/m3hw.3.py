X = 0
Y = 1

N = int(input('N = '))
print('')

while X < N:        
    print('Loop', X + 1, ':')
    print('X =', X, '+ 1')      
    X = X + 1    
    
    print('Y -', Y, '+ 2(', X, ')')
    Y = Y + 2 * X

print('')    
print('Y =', Y)
print('Y =', Y, '/', N)   
Y = Y / N

print(Y)

        

