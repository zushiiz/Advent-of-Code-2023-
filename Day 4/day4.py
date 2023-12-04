def scratch_cards():
  with open("Day 4/input.txt", "r", encoding="utf-8") as file:
      cards = [line.strip() for line in file.readlines()] 
      final_point = 0

      for card in cards:

        new_cards = [item.strip() for item in card.replace(":", "|").split("|")]
        new_cards.pop(0)
        temp_list1 = []
        temp_list2 = []
        temp_list1.append(new_cards.pop(0))
        temp_list2.append(new_cards.pop(0))

        win_list = temp_list1[0].split()
        digits_list = temp_list2[0].split()
        
        x = 0
        amount = 0

        for win_digit in win_list:
        
          for digit in digits_list:

            if win_digit == digit:
              amount += 1
              if amount != 1:
                x *= 2
              else:
                x = 1
        final_point += x

  print("points", final_point)

scratch_cards()