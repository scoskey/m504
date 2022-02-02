# inputs: integers a,b
# prints steps of Euclidean algorithm to calculate gcd(a,b)
# outputs: gcd(a,b)
def euclid(a,b):
  if a==0 or b==0:
    print ( f'so the gcd is {max(a,b)}' )
    return max(a,b)
  q, r = a//b, a%b
  print ( f'{a} = ({q}){b} + {r}' )
  return gcd(b, r)

# inputs: integers a,b
# prints steps of the Euclidean algorithm to calculate gcd(a,b)
# prints back-solving steps to express gcd(a,b) as ax+by
# outputs: gcd(a,b), x, y
def euclid2(a,b):
  if a==0 or b==0:
    print ( f'so gcd is {max(a,b)} and...' )
    return max(a,b), 1, 0
  q, r = a//b, a%b
  print ( f'{a} = ({q}){b} + {r}' )
  d, x, y = gcd2(b, r)
  x, y = y, x-y*q
  print ( f'{d} = ({x}){a} + ({y}){b}' )
  return d, x, y

# inputs: integer n
# prints table with entries a^i (mod n) in row a, column i
def powerTable(n):
  for a in range(1,n):
    powerRow = ''
    power = 1
    for i in range(n):
      power = (power * a) % n
      powerRow += f'{power:4}'
    print(powerRow)

