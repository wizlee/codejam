'''
Codejam 2020; qualification round: Nesting Depth (5pts, 11pts)
- https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f
- run this program using `python {this filename} < input.txt`
  - Example: `python template.py input.txt`
'''

from dataclasses import dataclass


@dataclass
class TestCase:
  S: str

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

  T = int(input())
  for _ in range(T):
    S = input()
    test_cases.append(TestCase(S))

  return Input(T, test_cases)


def compute(test_case: TestCase):
  digits = [int(i) for i in test_case.S]
  optimal_grp = optimal_groups(digits)

  final_str = ""
  for group in optimal_grp:
    final_str.join(insert_brackets(group))

  return final_str


def optimal_groups(digits):
  groups = []
  curr_group = []
  curr_group_remaining = 0

  for d in digits:
    if d == 0:
      groups.append([d])
      continue

    if not curr_group:
      curr_group.append(d)
      continue

    if abs(curr_group[-1] - d) > 1:
      groups.append(curr_group.copy())
      curr_group.clear()
    else:
      curr_group.append(d)

  return groups


def insert_brackets(group):
  substr = ""

  for d in group:
    if d == 0:
      substr = str(d)
      break



  return substr


if __name__ == "__main__":
  main()
