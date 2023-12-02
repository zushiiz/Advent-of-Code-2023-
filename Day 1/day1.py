with open ("Advent-of-Code-2023\Day 1\calibrations.txt", "r", encoding = "utf-8") as file_lines:
  l_rows = file_lines.readlines()

  finished_numbers = []

  for l_row in l_rows:
    stripped_row = l_row.strip()

    numbers = ''.join(filter(str.isdigit, stripped_row))

    str_digits_list = [str(str_digit) for str_digit in numbers]

    amount = len(str_digits_list)

    new_digit = str_digits_list[0]

    new_digit2 = str_digits_list[amount-1]

    final_digit = new_digit + str(new_digit2)

    finished_numbers.append(int(final_digit))

  answer = sum(finished_numbers)

  print(answer)