from typing import List
# Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]:
  return [x for x in int_list if x % 2 == 0]
  pass
# Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
  return sum(x ** 2 for x in even_int_list)
  pass
# Main function
def main():
  # Example list
  int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  even_int_list = even_list(int_list)
  output = sum_of_squares_of_even(even_int_list)
  print(output)
# Boilerplate code
if __name__ == "__main__":
  main()
