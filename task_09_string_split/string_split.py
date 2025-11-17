def split_and_join(line):
    modified_string = line.split(" ")

    return "-".join(modified_string)



if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

