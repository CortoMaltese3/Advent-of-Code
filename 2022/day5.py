with open('puzzle_input\\day5.txt', 'r') as file:
    data = file.read().split('\n')

crates = data[:8]
moves = data[10:]
crate_rows = []
for row in crates:
    crate_row = ""
    for i in range(1, 34, 4):
        crate_row += f'{row[i:i+1].replace(" ", "-")}'
    crate_rows.append(crate_row)

# Part1
crate_stacks = []
for i in range(9):
    stack = ""
    for j in range(8):
        stack+=crate_rows[j][i]
    crate_stacks.append(stack.replace("-", ""))

for i in range(len(moves)):
    if len(moves[i]) > 18:
        number_of_boxes = int(moves[i][5:7])
        start_stack_column = int(moves[i][13])-1
        end_stack_column = int(moves[i][18])-1
    else:
        number_of_boxes = int(moves[i][5])
        start_stack_column = int(moves[i][12])-1
        end_stack_column = int(moves[i][17])-1

    start_stack = crate_stacks[start_stack_column].replace("-", "")
    end_stack = crate_stacks[end_stack_column].replace("-", "")
    end_stack = start_stack[:number_of_boxes][::-1] + end_stack # This row changes the result with part2
    start_stack = start_stack[number_of_boxes:].rjust(8, "-")
    end_stack = end_stack.rjust(8, "-")
    crate_stacks[start_stack_column] = start_stack
    crate_stacks[end_stack_column] = end_stack

answer = ""
for i in range(9):
    answer+=crate_stacks[i].replace("-", "")[0]

print(f'Crates that end up at the top of each stack form: {answer}') #SHQWSRBDL


# Part2
crate_stacks = []
for i in range(9):
    stack = ""
    for j in range(8):
        stack+=crate_rows[j][i]
    crate_stacks.append(stack.replace("-", ""))

for i in range(len(moves)):
    if len(moves[i]) > 18:
        number_of_boxes = int(moves[i][5:7])
        start_stack_column = int(moves[i][13])-1
        end_stack_column = int(moves[i][18])-1
    else:
        number_of_boxes = int(moves[i][5])
        start_stack_column = int(moves[i][12])-1
        end_stack_column = int(moves[i][17])-1

    start_stack = crate_stacks[start_stack_column].replace("-", "")
    end_stack = crate_stacks[end_stack_column].replace("-", "")
    end_stack = start_stack[:number_of_boxes] + end_stack # This row changes the result with part1
    start_stack = start_stack[number_of_boxes:].rjust(8, "-")
    end_stack = end_stack.rjust(8, "-")
    crate_stacks[start_stack_column] = start_stack
    crate_stacks[end_stack_column] = end_stack

answer = ""
for i in range(9):
    answer+=crate_stacks[i].replace("-", "")[0]

print(f'Crates that end up at the top of each stack form: {answer}') #SHQWSRBDL
