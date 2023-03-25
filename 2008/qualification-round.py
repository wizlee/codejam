'''
Attempting year 2008 code jam qualification round question
- https://codingcompetitions.withgoogle.com/codejam/round/0000000000432b79/0000000000432f32#problem
'''


import argparse
from pathlib import Path
from dataclasses import dataclass

sample_input = '''5
0.250000 1.000000 0.100000 0.010000 0.500000
0.250000 1.000000 0.100000 0.010000 0.900000
0.000010 10000.000000 0.000010 0.000010 1000.000000
0.400000 10000.000000 0.000010 0.000010 700.000000
1.000000 100.000000 1.000000 1.000000 10.000000
'''

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
  parser = argparse.ArgumentParser()
  parser.add_argument("-f", "--inputfile", type=int, help="Filepath to input file")

  args = parser.parse_args()
  input = args.inputfile
  input_txt = Path(input).read_text()
  prods_list = get_probs(input_txt)


def get_probs(input_txt):
  input : Input = parse_input_txt(input_txt)
  prods_str = []
  for i in range(input.total_input):
    test_case : TestCase = input.test_cases[i]
    prods_str.append(str(get_prod(test_case)))

  return prods_str


# final answer is area of gaps divided by area of racquet
def get_prod(test_case: TestCase):
  # research so far
  # area of a segment of circle: https://www.wolframalpha.com/input?i=segment+of+a+circle
  # where 0.5 * r^2 * (θ - sinθ)
  # where θ is in radian
  # where 2 π radians == 360 degree
  pass


def parse_input_txt(input_txt):
  input_lines = str.splitlines(input_txt)

  N = 0
  test_cases = []

  for i, line in enumerate(input_lines):
    if i == 0:
      N = int(line)
      continue

    variables = str.split(line, ' ')
    f = float(variables[0])
    R = float(variables[1])
    t = float(variables[2])
    r = float(variables[3])
    g = float(variables[4])

    test_cases.append(TestCase(f, R, t, r, g))

  return Input(N, test_cases)


if __name__ == "__main__":
    get_probs(sample_input)
