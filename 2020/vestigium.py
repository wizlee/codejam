'''
Codejam 2020; qualification round: Vestigium (7pts)
- https://link-to-problem.com
- run this program using `python {this filename} < input.txt`
  - Example: `python template.py input.txt`
'''

from dataclasses import dataclass
import numpy as np

@dataclass
class TestCase:
  N: int # matrix size
  matrix: np.ndarray

@dataclass
class Input:
  total_input: int
  test_cases: list # list of TestCase


def main():
  print_output(compute_all())


def print_output(results):
  for i, (k, r, c) in enumerate(results):
    print(f'Case #{i+1}: {str(k)} {str(r)} {str(c)}')


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

  for _ in range(1, T + 1):
    N = int(input())
    matrix_list = []
    for _ in range(N):
      matrix_list.append([int(var) for var in input().split(' ')])

    matrix = np.vstack(matrix_list)
    test_cases.append(TestCase(N, matrix))

  return Input(T, test_cases)


def compute(test_case: TestCase):
  k = r = c = 0

  k = np.sum(np.diag(test_case.matrix))
  r = row_dup_count(test_case.matrix)
  c = column_dup_count(test_case.matrix)
  return (k, r, c)


def column_dup_count(A):
  count = 0
  diff = np.diff(np.sort(A, axis=0), axis=0)
  for col in diff.T:
    count += np.any(col == 0)
  return count


def row_dup_count(A):
  count = 0
  diff = np.diff(np.sort(A, axis=1), axis=1)
  for row in diff:
    count += np.any(row == 0)
  return count


if __name__ == "__main__":
  main()
