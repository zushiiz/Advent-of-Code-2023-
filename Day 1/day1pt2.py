with open ("Day 1\calibrations.txt", "r", encoding = "utf-8") as file_lines:
  l_rows = file_lines.readlines()

  finished_numbers = []

  word_numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    }

  for l_row in l_rows:
    stripped_row = l_row.strip()

    temporary_list = []

    i = 0

    while i < len(stripped_row):

      if stripped_row[i].isdigit(): 
        temporary_list.append(stripped_row[i])
        i += 1

      else:
        for letter, number in word_numbers.items():
          if stripped_row.startswith(letter, i):
            temporary_list.append(number)
            i += len(letter)
            break
        else:
          i += 1

    str_digits_list = [str(str_digit) for str_digit in temporary_list]
    amount = len(str_digits_list)
    new_digit = str_digits_list[0]
    new_digit2 = str_digits_list[amount-1]
    final_digit = new_digit + str(new_digit2)
    finished_numbers.append(int(final_digit))

  answer = sum(finished_numbers)

  print(answer)