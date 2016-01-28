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
  if b < 256:
    return b
  return b ^ 0x11b

def x3(a):
  return xtime(a) ^ a

# Tables
def invertTable(table):
  inverse = [0] * len(table)
  for x, y in enumerate(table):
    inverse[y] = x
  return inverse

eTable = take(256, repeat(x3, 1))
logTable = invertTable(eTable)
