def cube_game():
    with open("Day 2/input.txt", "r", encoding="utf-8") as file:
        games = [line.strip() for line in file.readlines()]
        multiplied_values_list = [] 
        final = 0
        for game in games:
            result_list = [item.strip() for item in game.replace(':', ',').replace(';', ',').split(',')]
            result_list.pop(0)

            blue_list = []
            red_list = []
            green_list = []

            blue = 1
            red = 1
            green = 1

            for item in result_list:
                if item.endswith("blue"):
                    blue_list.append(item.replace(" blue", ""))
                    blue_int_list = [int(item) for item in blue_list ]
                    blue = max(blue_int_list)

                elif item.endswith("red"):
                    red_list.append(item.replace(" red", ""))
                    red_int_list = [int(item) for item in red_list ]
                    red = max(red_int_list)                    

                elif item.endswith("green"):
                    green_list.append(item.replace(" green", ""))
                    green_int_list = [int(item) for item in green_list ]
                    green = max(green_int_list)

                multiplied_value = red * green * blue
        
            multiplied_values_list.append(multiplied_value)
        print(multiplied_values_list)
        print(sum(multiplied_values_list))
        
cube_game()