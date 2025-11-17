commands_num = int(input())
commands_list = []
my_list = []

for _ in range(commands_num):
    current_command = input().split()
    commands_list.append(current_command)

for command_line in commands_list:
    command = command_line[0]

    if command_line[0] == "insert":
        i = int(command_line[1])
        e = int(command_line[2])
        my_list.insert(i, e)

    elif command_line[0] == "print":
        print(my_list)

    elif command_line[0] == "remove":
        element_to_remove = int(command_line[1])
        my_list.remove(element_to_remove)

    elif command_line[0] == "append":
        element_to_append = int(command_line[1])
        my_list.append(element_to_append)

    elif command_line[0] == "sort":
        my_list.sort()

    elif command_line[0] == "pop":
        my_list.pop()

    elif command_line[0] == "reverse":
        my_list.reverse()

