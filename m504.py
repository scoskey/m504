# input: integers a,b
# prints: steps of Euclidean algorithm to calculate gcd(a,b)
# output: gcd(a,b)
def euclid(a,b):
    if a==0 or b==0:
        print ( f'so the gcd is {max(a,b)}' )
        return max(a,b)
    q, r = a//b, a%b
    print ( f'{a} = ({q}){b} + {r}' )
    return euclid(b, r)

# input: integers a,b
# prints: steps of the Euclidean algorithm to calculate gcd(a,b)
# prints: back-solving steps to express gcd(a,b) as ax+by
# output: gcd(a,b), x, y
def euclid2(a,b):
    if a==0 or b==0:
        print ( f'so gcd is {max(a,b)} and...' )
        return max(a,b), 1, 0
    q, r = a//b, a%b
    print ( f'{a} = ({q}){b} + {r}' )
    d, x, y = euclid2(b, r)
    x, y = y, x-y*q
    print ( f'{d} = ({x}){a} + ({y}){b}' )
    return d, x, y

# input: integer n
# prints: table with entries a^i (mod n) in row a, column i
def powerTable(n):
    for a in range(1,n):
        powerRow = ''
        power = 1
        for i in range(n):
            power = (power * a) % n
            powerRow += f'{power:4}'
        print(powerRow)

# input: integer n
# prints: list of integers i<n such that gcd(i,n)=1
# output: number of integers i<n such that gcd(i,n)=1
def euler(n):
    from math import gcd
    list = ''
    count = 0
    for i in range(n):
        d = gcd(i,n);
        if d==1:
            list += f'{i:3}'
            count += 1
    print (list)
    return count
    
# input: integer n
# output: list of values of pi(i) for i=0,...,n-1 (the number of primes < i)
def countprimes(n):
    from sympy import isprime
    pivals = [0]
    for i in range(1,n):
        if isprime(i):
            vals.append( pivals[i-1]+1 )
        else:
            vals.append( pivals[i-1] )
    return pivals
