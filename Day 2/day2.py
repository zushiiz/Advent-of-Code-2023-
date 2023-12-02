def cube_game():
    with open("Day 2/input.txt", "r", encoding="utf-8") as file:
        games = [line.strip() for line in file.readlines()] 

        red_limit = 12
        green_limit = 13
        blue_limit = 14
        final_count = 0

        for game in games:
            result_list = [item.strip() for item in game.replace(':', ';').split(';')]
            game_id = result_list.pop(0)
            sorted_list = [item.split(', ') for item in result_list]

            game_id_number = ''.join(filter(str.isdigit, game_id))
            final_id = int(game_id_number)            
            iterations = 0
            id_iterations = 0

            while iterations < len(sorted_list):
                for sublist in sorted_list:

                    red_count = 0
                    green_count = 0
                    blue_count = 0

                    for item in sublist:
                        quantity, color = item.split()
                        quantity = int(quantity)

                        if color == 'red':
                            red_count += quantity
                        elif color == 'green':
                            green_count += quantity
                        elif color == 'blue':
                            blue_count += quantity

                    if red_limit >= red_count:
                        if green_limit >= green_count:
                            if blue_limit >= blue_count:
                                iterations += 1
                                id_iterations += 1
                            else:
                                iterations += 1
                        else:
                            iterations += 1
                    else:
                        iterations += 1

            if id_iterations == iterations:
                final_count += final_id

    print("aur aur", final_count)
cube_game()