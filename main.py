def main(n:int):
  the_sum = 0
  for i in range(1, n + 1):
    the_sum += i

  return the_sum

assert main(5) == 1 + 2 + 3 + 4  + 5
assert main(10) == 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10