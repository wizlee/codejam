'''
Codejam 20XX; round X: Problem name
- https://link-to-problem.com
- run this program using `python {this filename} < {input.txt file}`
  - Example: `python template.py sample-input.txt`
'''

from dataclasses import dataclass
import fileinput

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


def print_output(ans_list):
  for i, prod in enumerate(ans_list):
    print(f'Case #{i+1}: {str(prod)}')


def compute_all():
  input : Input = get_all_input()
  prods_str = []
  for i in range(input.total_input):
    test_case : TestCase = input.test_cases[i]
    prods_str.append(str(compute(test_case)))

  return prods_str


def get_all_input():
  test_cases = []

  with fileinput.input() as f_input:
    for line in f_input:
      if f_input.isfirstline():
        N = int(line)
        continue

      if f_input.filelineno() > N + 1:
        fileinput.close() # protect against invalid inputs
        break

      variables = line.split(' ')
      f = float(variables[0])
      R = float(variables[1])
      t = float(variables[2])
      r = float(variables[3])
      g = float(variables[4])

      test_cases.append(TestCase(f, R, t, r, g))

  return Input(N, test_cases)


def compute(test_case: TestCase):
  return test_case.f + test_case.R + test_case.t + test_case.r + test_case.g

if __name__ == "__main__":
  main()
