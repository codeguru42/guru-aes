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
