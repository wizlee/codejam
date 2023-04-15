'''
Codejam 2023; farewell round: Illumination Optimization (4pts, 10pts)
- https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cad086
- run this program using `python {this filename} < input.txt`
  - Example: `python template.py input.txt`
'''

from dataclasses import dataclass

@dataclass
class Input:
  total_input: int
  test_cases: list # list of TestCase

@dataclass
class TestCase:
  M: int # freeway length in meters
  R: int # illumination radius in meters
  N: int # number of street lights
  light_loc: list


def main():
  print_output(compute_all())


def print_output(results):
  for i, result in enumerate(results):
    print(f'Case #{i+1}: {result}')


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
    M, R, N = (int(var) for var in input().split(' '))
    light_loc = [int(var) for var in input().split(' ')]

    test_cases.append(TestCase(M, R, N, light_loc))

  return Input(T, test_cases)


def compute(test_case: TestCase):
  who_lights_this_slot = [[] for _ in range(test_case.M)] # do not use `[[]] * test_case.M` because all the list element will reference to the SAME list

  for street_light_index, loc in enumerate(test_case.light_loc):
    these_slots_are_lit = [i for i in range(max(0, loc - test_case.R), min(test_case.M, loc + test_case.R))]
    for slot in these_slots_are_lit:
      who_lights_this_slot[slot].append(street_light_index)

  if is_any_empty_list(who_lights_this_slot):
    answer = "IMPOSSIBLE"
  else:
    all_slots_with_1_light = [slot for slot in set([tuple(x) for x in who_lights_this_slot]) if len(slot) == 1]
    answer = str(len(all_slots_with_1_light))

  return answer


def is_any_empty_list(li):
  if li == []:
    return True
  else:
    return any((isinstance(sli, list) and is_any_empty_list(sli)) for sli in li)


if __name__ == "__main__":
  main()
