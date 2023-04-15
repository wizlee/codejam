'''
Codejam 2023; farewell round: Colliding Encoding (4pts, 10pts)
- https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cad7cf
- run this program using `python {this filename} < input.txt`
  - Example: `python template.py input.txt`
'''

from dataclasses import dataclass
import string

@dataclass
class Input:
  total_input: int
  test_cases: list # list of TestCase


@dataclass
class TestCase:
  mapping: dict
  N: int
  words: list


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
    mapping = {string.ascii_uppercase[i]: d for i, d in enumerate(input().split(' '))}
    N = int(input())
    words = []
    for _ in range(N):
      words.append(input())

    test_cases.append(TestCase(mapping, N, words))

  return Input(T, test_cases)


def compute(test_case: TestCase):
  encoded = []
  for word in test_case.words:
    digits = [test_case.mapping[w] for w in word]
    encoded.append(''.join(digits))

  return "YES" if has_duplicate(encoded) else "NO"


def has_duplicate(list):
  return len(list) != len(set(list))


if __name__ == "__main__":
  main()
