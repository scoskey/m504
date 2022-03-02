# input: integers a, b
# prints: steps of Euclidean algorithm to calculate gcd(a,b)
# output: gcd(a,b)
def euclid(a,b):
    if a==0 or b==0:
        print ( f'so the gcd is {max(a,b)}' )
        return max(a,b)
    q, r = a//b, a%b
    print ( f'{a} = ({q}){b} + {r}' )
    return euclid(b, r)

# input: integers a, b
# prints: steps of the Euclidean algorithm to calculate gcd(a,b)
# prints: steps to back-solve and express gcd(a,b) as ax+by
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
def powertable(n):
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
# output: list of values of pi(0),...,pi(n-1) (pi(i) is the number of primes < i)
def countprimes(n):
    from sympy import isprime
    pivals = [0]
    for i in range(1,n):
        if isprime(i):
            pivals.append( pivals[i-1]+1 )
        else:
            pivals.append( pivals[i-1] )
    return pivals

# input: integer n
# output: sum of d such that d|n
def divisorsum(n):
    sum = 0;
    for i in range(1,int(n/2)+1):
        if n%i==0:
            sum += i
    return sum+n

# input: integer n
# output: list of perfect numbers < n
def perfectfind(n):
    output = []
    for i in range(1,n):
        if divisorsum(i)==2*i:
            output.append(i)
    return output

# input: integers a,k,n
# prints: values of a^(2^p) mod (n) for all p such that 2^p<k
def powermod(a,k,n):
    power, exponent = a, 1
    while exponent<k:
        print( f'{a}^{exponent} = {power} (mod {n})' )
        power, exponent = (power*power) % n, 2*exponent

# input: integer m
# output: string expressing m as a sum of distinct powers of 2
def binaryexpand(m):
    output, power, q = [], 1, m
    while q > 0:
        q, r = q//2, q%2
        if r == 1: output.append(str(power))
        power = 2 * power
    return f'{m} = ' + ' + '.join(output)

## input: integers a,n
## ouptut: multiplicative inverse of a in Z_n, if it exists
def inverse(a,n):
    def euclid3(a,b):
        if a==0 or b==0: return max(a,b), 1, 0
        d, x, y = euclid3(b, a%b)
        return d, y, x-y*(a//b)
    d, x, y = euclid3(a,n)
    if d > 1: return False
    return x % n

## input: string s, integer b
## output: string encoded as array of integers with b letters per integer
def text2ints(s,b=1):
    from math import ceil
    output = []
    if b==1:
        s = s.lower()
        for i in range(len(s)):
            n = ord(s[i])-86
            if 11 <= n and n <= 36:
                output.append(n)
    else:
        a = text2ints(s)
        for i in range(ceil(len(a)/b)):
            j, block = 0, 0
            while j < b and i*b+j<len(a):
                block = 100*block + a[i*b+j]
                j = j+1
            output.append(block)
    return output

## input: integer OR integer array
## output: string of letters coded by a or the elements of a
def ints2text(a):
    output = ''
    if isinstance(a,int):
        s = str(a)
        for i in range(int(len(s)/2)):
            n = int(s[2*i:2*i+2])
            if 11 <= n and n <= 36:
                output = output + chr(n+86)
    else:
        for i in range(len(a)):
            t = ints2text(a[i])
            output = output + t
    return output
