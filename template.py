'''
Codejam 20XX; round X: Problem name
- https://link-to-problem.com
- run this program using `python {this filename} < input.txt`
  - Example: `python template.py input.txt`
'''

from dataclasses import dataclass


@dataclass
class TestCase:
  '''each of the member here is a value from a single line input separated by space'''
  f: float
  R: float
  t: float
  r: float
  g: float

@dataclass
class Input:
  total_input: int
  test_cases: list # list of TestCase


def main():
  print_output(compute_all())


def print_output(results):
  for i, result in enumerate(results):
    print(f'Case #{i+1}: {str(result)}')


def compute_all():
  input : Input = get_all_input()
  results = []
  for i in range(input.total_input):
    test_case : TestCase = input.test_cases[i]
    results.append(compute(test_case))

  return results


def get_all_input():
  test_cases = []

  N = int(input()) # read a line with a single integer, this is expected to be the number of test cases
  for _ in range(1, N + 1):
    f ,R ,t ,r ,g = (float(var) for var in input().split(' ')) # read a list of floats, 5 in this case
    test_cases.append(TestCase(f, R, t, r, g))

  return Input(N, test_cases)


def compute(test_case: TestCase):
  return test_case.f + test_case.R + test_case.t + test_case.r + test_case.g

if __name__ == "__main__":
  main()
