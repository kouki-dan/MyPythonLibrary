
import string

def base_str(n, radix=None):
  digits = string.digits + string.ascii_letters

  if not 1 < radix < len(digits)+1:
    raise ValueError("invalid radix {}".format(radix))
  if radix is None:
    radix = len(digits)
  
  negative = n < 0
  n = abs(n)

  num = []
  while n:
    num.insert(0, n % radix)
    n //= radix
    if n == 0:
      break
  num = "".join([digits[i] for i in num])
  if negative:
    num = "-" + num
  return num

