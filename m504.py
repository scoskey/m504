# input: integers a, b
# print: steps of Euclidean algorithm to calculate gcd(a,b)
# output: gcd(a,b)
def euclid(a,b):
    if a==0 or b==0:
        print ( f'so the gcd is {max(a,b)}' )
        return max(a,b)
    q, r = a//b, a%b
    print ( f'{a} = ({q}){b} + {r}' )
    return euclid(b, r)

# input: integers a, b
# print: steps of the Euclidean algorithm to calculate gcd(a,b)
# print: steps to back-solve and express gcd(a,b) as ax+by
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
# print: table with entries a^i (mod n) in row a, column i
def powertable(n):
    for a in range(1,n):
        row = [a]
        for i in range(n):
            row.append( (row[-1]*a)%n )
        print( ''.join([ f'{e:4}' for e in row ]) )

# input: integer n
# print: list of integers i<n such that gcd(i,n)=1
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
# output: list of values of pi(0),...,pi(n-1) (pi(i) = number of primes < i)
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
# print: values of a^(2^p) mod (n) for all p such that 2^p<k
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

# input: integers a,n
# ouptut: multiplicative inverse of a in Z_n, if it exists
def inverse(a,n):
    def euclid3(a,b):
        if a==0 or b==0: return max(a,b), 1, 0
        d, x, y = euclid3(b, a%b)
        return d, y, x-y*(a//b)
    d, x, y = euclid3(a,n)
    if d > 1: return False
    return x % n

# input: string s, integer b
# output: string encoded as array of integers with b letters per integer
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

# input: integer OR integer array
# output: string of letters coded by a OR by the elements of a
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

# input: an integer n
# print: table of powers a^((2^i)q) (mod n), where n-1=(2^k)q, q odd
def rabinmillertable(n):
    q, k = n-1, 0
    while q%2 == 0 :
        q = int(q/2)
        k = k+1
    header = f'{q:4}'
    for i in range(k):
        header = header + f'{q*(2**(i+1)):4}'
    print (header, "\n", '--')
    for a in range(1,n):
        row = [(a**q)%n]
        for i in range(k):
            row.append( (row[-1]**2)%n )
        print( ''.join([ f'{e:4}' for e in row ]) )

# input: an odd prime p
# outpt: an array of all nonzero quadratic residues (squares) modulo p
def squares(p):
    output = set()
    for b in range(1,p):
        output.add( pow(b,2,p) )
    output = list(output)
    output.sort()
    return( output )

# input: integers a,p, with p typically a prime number
# output: the value of the legendre symbol (a/p)
def legendre(a,p):
    ans = pow(a,(p-1)//2,p)
    if ans == 1:
        return 1
    elif ans == p-1:
        return -1
    elif ans == 0:
        return 0
    else:
        return False

# input: integer n
# output: sum of phi(d) such that d|n
def totientsum(n):
    from sympy import totient
    sum = 0;
    for i in range(1,int(n/2)+1):
        if n%i==0:
            sum += totient(i)
    return sum+totient(n)

# input: integer g, prime modulus p
# output: table with column of 1,...,p-1 and column of g^1,...,g^(p-1)
def indextable(g,p):
    for i in range (1,p):
      print(i,pow(g,i,p))

# input: irrational alpha, bound B
# output: table of values (x,y) making |x-y*alpha|≤.5 for all y<B, the value of x-y*alpha, and whether or not |x-y*alpha|<1/y
def dirichlet(alpha,B):
    print('  x   y  error close?')
    for y in range(1,B):
        w,f = int(y*alpha), y*alpha-int(y*alpha)
        x=w if f<0.5 else w+1
        print(f'{x:3} {y:3} {x-y*alpha: .3f} {abs(x-y*alpha)<1/y}')

# input: non-square natural number D, bound B
# output: table of values (x,y) making |x-y*sqrt(D)|<1/y, value of 
def pell(D,B):
    from math import sqrt
    alpha = sqrt(D)
    print('  x   y  error x^2-Dy^2')
    for y in range(1,B):
        w,f = int(y*alpha), y*alpha-int(y*alpha)
        x=w if f<0.5 else w+1
        if abs(x-y*alpha)<1/y:
            print(f'{x:3} {y:3} {x-y*alpha: .3f} {round(x**2-D*y**2): 3}')
