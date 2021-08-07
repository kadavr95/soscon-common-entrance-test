def palindrome(test_string):
    test_string=test_string.lower().replace(" ", "")
    first_half = test_string[:(len(test_string) // 2)]
    second_half = test_string[-(len(test_string) // 2):]
    return first_half == second_half[::-1]

assert palindrome('А РОЗА УПАЛА НА ЛАПУ АЗОРА') is True
