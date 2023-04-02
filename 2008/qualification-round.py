'''
Codejam 2008; qualification round: Fly Swatter
- https://codingcompetitions.withgoogle.com/codejam/round/0000000000432b79/0000000000432f32#problem
'''

from dataclasses import dataclass
import fileinput

@dataclass
class TestCase:
  f: float # radius of fly
  R: float # radius of racquet
  t: float # thickness of ring
  r: float # radio of chord
  g: float # gap between chords

@dataclass
class Input:
  total_input: int
  test_cases: list


def main():
  print_output(get_prods())


def print_output(prods_list):
  for i, prod in enumerate(prods_list):
    print(f'Case #{i+1}: {str(prod)}')


def get_prods():
  input : Input = get_all_input()
  prods_str = []
  for i in range(input.total_input):
    test_case : TestCase = input.test_cases[i]
    prods_str.append(str(get_prod(test_case)))

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


# final answer is area of gaps divided by area of racquet
def get_prod(test_case: TestCase):
  # research so far
  # area of a segment of circle: https://www.wolframalpha.com/input?i=segment+of+a+circle
  # where 0.5 * r^2 * (θ - sinθ)
  # where θ is in radian
  # where 2 π radians == 360 degree
  return test_case.f + test_case.R + test_case.t + test_case.r + test_case.g

def circle_segment():
  pass

if __name__ == "__main__":
  sample_input = '''5
0.250000 1.000000 0.100000 0.010000 0.500000
0.250000 1.000000 0.100000 0.010000 0.900000
0.000010 10000.000000 0.000010 0.000010 1000.000000
0.400000 10000.000000 0.000010 0.000010 700.000000
1.000000 100.000000 1.000000 1.000000 10.000000
'''
  # get_prods()
  main()
