def swap_case(s):

    modifyed_string = ""


    for letter_indx in range(len(s)):

        if s[letter_indx].isalpha() and s[letter_indx].islower():
            modifyed_string += s[letter_indx].upper()

        elif s[letter_indx].isalpha() and s[letter_indx].isupper():
            modifyed_string += s[letter_indx].lower()
        else:
            modifyed_string += s[letter_indx]


    return modifyed_string


string_to_modify = input()
print(swap_case(string_to_modify))
