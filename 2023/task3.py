'''
Codejam 2023; farewell round: Rainbow Sort
- https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cada38
- run this program using `python {this filename} < filename.txt`
  - Example: `python template.py template.txt`
'''

from dataclasses import dataclass


@dataclass
class Input:
  total_input: int
  test_cases: list # list of TestCase

@dataclass
class TestCase:
  N: int
  colours: list


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

  T = int(input())
  for _ in range(T):
    N = int(input())
    colours = (var for var in input().split(' '))
    test_cases.append(TestCase(N, colours))

  return Input(T, test_cases)


def compute(test_case: TestCase):
  colour_dict = {}
  for c in test_case.colours:
    keys = colour_dict.keys()
    if c in keys:
      if c != keys[-1]:
        return "IMPOSSIBLE"

  return ""

if __name__ == "__main__":
  main()
