# Read puzzle_input_day1.txt file into data object
with open("puzzle_input_day2.txt", "r") as file:
    data = file.read().split("\n")

elf_moves = [gesture[0] for gesture in data]
my_moves = [gesture[2] for gesture in data]

def calculate_total_points_part1(opp1_moves: list, opp2_moves: list):
    """
    TODO: Add description.
    """
    number_of_moves = len(opp1_moves)
    opp1_points = 0
    opp2_points = 0
    win_points = 6
    draw_points = 3
    loss_points = 0
    rock_points = 1
    paper_points = 2
    scissors_points = 3

    for index in range(number_of_moves):
        if opp1_moves[index] == "A" and opp2_moves[index] == "X":
            opp1_points += draw_points + rock_points
            opp2_points += draw_points + rock_points
        if opp1_moves[index] == "A" and opp2_moves[index] == "Y":
            opp1_points += loss_points + rock_points
            opp2_points += win_points + paper_points
        if opp1_moves[index] == "A" and opp2_moves[index] == "Z":
            opp1_points += win_points + rock_points
            opp2_points += loss_points + scissors_points

        if opp1_moves[index] == "B" and opp2_moves[index] == "X":
            opp1_points += win_points + paper_points
            opp2_points += loss_points + rock_points
        if opp1_moves[index] == "B" and opp2_moves[index] == "Y":
            opp1_points += draw_points + paper_points
            opp2_points += draw_points + paper_points
        if opp1_moves[index] == "B" and opp2_moves[index] == "Z":
            opp1_points += loss_points + paper_points
            opp2_points += win_points + scissors_points

        if opp1_moves[index] == "C" and opp2_moves[index] == "X":
            opp1_points += loss_points + scissors_points
            opp2_points += win_points + rock_points
        if opp1_moves[index] == "C" and opp2_moves[index] == "Y":
            opp1_points += win_points + scissors_points
            opp2_points += loss_points + paper_points
        if opp1_moves[index] == "C" and opp2_moves[index] == "Z":
            opp1_points += draw_points + scissors_points
            opp2_points += draw_points + scissors_points

    return opp2_points

my_points_part1 = calculate_total_points_part1(elf_moves, my_moves)

def calculate_total_points_part2(opp1_moves, opp2_moves):
    """
    TODO: Add description.
    """
    number_of_moves = len(opp1_moves)
    opp1_points = 0
    opp2_points = 0
    win_points = 6
    draw_points = 3
    loss_points = 0
    rock_points = 1
    paper_points = 2
    scissors_points = 3
    
    for index in range(number_of_moves):
        if opp1_moves[index] == "A" and opp2_moves[index] == "X":
            opp1_points += win_points + rock_points
            opp2_points += loss_points + scissors_points
        if opp1_moves[index] == "A" and opp2_moves[index] == "Y":
            opp1_points += draw_points + rock_points
            opp2_points += draw_points + rock_points
        if opp1_moves[index] == "A" and opp2_moves[index] == "Z":
            opp1_points += loss_points + rock_points
            opp2_points += win_points + paper_points

        if opp1_moves[index] == "B" and opp2_moves[index] == "X":
            opp1_points += win_points + paper_points
            opp2_points += loss_points + rock_points
        if opp1_moves[index] == "B" and opp2_moves[index] == "Y":
            opp1_points += draw_points + paper_points
            opp2_points += draw_points + paper_points
        if opp1_moves[index] == "B" and opp2_moves[index] == "Z":
            opp1_points += loss_points + paper_points
            opp2_points += win_points + scissors_points

        if opp1_moves[index] == "C" and opp2_moves[index] == "X":
            opp1_points += win_points + scissors_points
            opp2_points += loss_points + paper_points
        if opp1_moves[index] == "C" and opp2_moves[index] == "Y":
            opp1_points += draw_points + scissors_points
            opp2_points += draw_points + scissors_points
        if opp1_moves[index] == "C" and opp2_moves[index] == "Z":
            opp1_points += loss_points + scissors_points
            opp2_points += win_points + rock_points

    return opp2_points



my_points_part1 = calculate_total_points_part1(elf_moves, my_moves)
my_points_part2 = calculate_total_points_part2(elf_moves, my_moves)

print(f"My total points in part 1 are: {my_points_part1}")
print(f"My total points in part 2 are: {my_points_part2}")
