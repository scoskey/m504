# inputs: integers a,b
# prints steps of Euclidean algorithm to calculate gcd(a,b)
# outputs: d=gcd(a,b)
def gcd(a,b):
  if a==0 or b==0:
    print ( f'so the gcd is {max(a,b)}' )
    return max(a,b)
  q, r = a//b, a%b
  print ( f'{a} = ({q}){b} + {r}' )
  return gcd(b, r)

# inputs: integers a,b
# prints steps of the Euclidean algorithm to calculate gcd(a,b)
# prints back-solving to write gcd(a,b) as a combination ax+by
# outputs: gcd(a,b), x, y
def gcd2(a,b):
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
# prints table of values a^i (mod n).
# 1^1     ... 1^n
# ...
# (n-1)^1 ... (n-1)^n
def powerTable(n):
  for a in range(1,n):
    powerRow = ''
    power = 1
    for i in range(n):
      power = (power * a) % n
      powerRow += f'{power:4}'
    print(powerRow)

