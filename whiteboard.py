['5', '0', 9, 3, 2, 1, '9', 6, 7] 



def lst(list1):
    int_list = []
    str_list = []

    for number in list1:

        if type(number) == int:
            int_list.append(number)
        else:
            str_list.append(int(number))

    return sum(int_list) - sum(str_list)


lst(['5', '0', 9, 3, 2, 1, '9', 6, 7])