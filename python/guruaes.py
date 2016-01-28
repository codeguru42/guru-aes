# general functions
def repeat(f, x):
  while True:
    yield x
    x = f(x)
