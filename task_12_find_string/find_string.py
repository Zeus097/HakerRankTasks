def count_substring(string, sub_string):
    counter = 0

    for l in range(len(string)):
        if string[l:l+len(sub_string)] == sub_string:
            counter += 1

    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
