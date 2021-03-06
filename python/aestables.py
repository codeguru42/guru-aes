# general functions
def repeat(f, x):
  while True:
    yield x
    x = f(x)

def take(n, seq):
  l = []
  for i, x in enumerate(seq):
    if i == n:
      return l
    l.append(x)
  return l

# GF(2**8)
def xtime(a):
  b = a << 1
  if b <= 0xff:
    return b
  return b ^ 0x11b

def x3(a):
  return xtime(a) ^ a

def gf(a, b):
  if a == 0x00 or b == 0x00:
    return 0x00
  return eTable[(logTable[a] + logTable[b]) % 0xff]

def initGFTable():
  gfTable = {}
  for x in [0x01, 0x02, 0x03, 0x09, 0x0b, 0x0d, 0x0e]:
    gfTable[x] = map(lambda y : gf(x, y), range(0x100))
  return gfTable

# Tables
def invertTable(table):
  inverse = [0] * len(table)
  for x, y in enumerate(table):
    inverse[y] = x
  return inverse

def rotater(x, n = 1):
  return (x >> n) | ((x << (8 - n)) & 0xff)

def affine(x):
  bytes = map(rotater, [x] * 4, range(4, 8))
  return x ^ reduce(int.__xor__, bytes) ^ 0x63

eTable = take(256, repeat(x3, 1))
logTable = invertTable(eTable)
logTable[1] = 0x00
invTable = [0] + map(lambda x : eTable[0xff - logTable[x]], range(0x01, 0x100))
sbox = map(lambda x : affine(invTable[x]), range(0x100))
invSbox = invertTable(sbox)
gfTable = initGFTable()
