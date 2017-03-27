# Euclidean algorithm
# Find GCD of (a, b)
# could use recursion!

a = int(input('A = '))
b = int(input('B = '))

aOrig = a;
bOrig = b;

x = int(a / b)
y = a % b

while y != 0:
    print('divide', a, 'by', b, ':\t', a, '=', b, '·', x, '+', y)
    a = b
    b = y
    x = int(a / b)
    y = a % b

print('divide', a, 'by', b, ':\t', a, '=', b, '·', x, '+', y)
print('GCD({0}, {1}) = {2}'.format(aOrig, bOrig, b))
    



    
    
    
