'''
Taken from the analysis of a sample problem: https://codingcompetitions.withgoogle.com/codejam/round/0000000000000130/0000000000000523#analysis
'''

import sys

def solve(a, b):
  m = (a + b) // 2
  print(m)
  sys.stdout.flush() # the answer is provided to the judge here
  s = input()
  if s == "CORRECT":
    return
  elif s == "TOO_SMALL":
    a = m + 1
  else:
    b = m - 1
  solve(a, b)

if __name__ == "__main__":
  T = int(input()) # number of test cases
  for _ in range(T):
    a, b = map(int, input().split())
    _ = int(input()) # num of retries, not used but still necessary to 'consume' the input
    solve(a + 1, b)
