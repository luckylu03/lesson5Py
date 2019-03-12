# Finish the solution so that it returns the sum
# of all the multiples of 3 or 5 below the number passed in.

def solution(number):
  return sum(n for n in range(number) if n % 3 == 0 or n % 5 == 0)