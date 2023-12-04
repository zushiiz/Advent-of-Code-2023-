def scratch_cards():
  with open("Day 4/test.txt", "r", encoding="utf-8") as file:
      cards = [line.strip() for line in file.readlines()] 

      cardinstance = [1] * 6

      for card in cards:

        new_cards = [item.strip() for item in card.replace(":", "|").split("|")]
        new_cards.pop(0)
        temp_list1 = []
        temp_list2 = []
        temp_list1.append(new_cards.pop(0))
        temp_list2.append(new_cards.pop(0))

        win_list = temp_list1[0].split()
        digits_list = temp_list2[0].split()

        amount = 0

        for win_digit in win_list:
        
          for digit in digits_list:

            if win_digit == digit:
              amount += 1

        for i in range(amount):
           cardinstance[int(digit) + i] += cardinstance[int(digit) - 1]
           print(digit)

  print(cardinstance)

scratch_cards()