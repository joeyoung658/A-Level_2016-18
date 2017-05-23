""" Joe Young
Happy Number finder V.1

22/05/2017
"""


def happy_number(number):
    
    
    total = 0
    
    #Spilt up the number into a list then squares each one by 2 adding it onto the total each tome
    for i in [int(i) for i in str(number)]:
        total += i**2

    #Happy number if total equals 1
    if (total == 1):
        return True

    #If total adds upto one of the numbers within this list, isn't a happy number    
    elif total in [4, 16, 37, 58, 89, 145, 42, 20]:
        return False
    else:
        return(happy_number(total))

    

def main():

    test_case = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91,94, 97, 100, 103, 109, 129, 130, 133, 139, 167, 176, 188, 190,
    192, 193, 203, 208, 219, 226, 230, 236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313, 319, 320, 326, 329, 331, 338, 356, 362, 365, 367,
    368, 376, 379, 383, 386, 391, 392, 397, 404, 409, 440, 446, 464, 469, 478, 487, 490, 496, 536, 556, 563, 565, 566, 608, 617, 622, 623, 632,
        635, 637, 638, 644, 649, 653, 655, 656, 665, 671, 673, 680, 683, 694, 700, 709, 716, 736, 739, 748, 761, 763, 784, 790, 793, 802, 806, 818,
        820, 833, 836, 847, 860, 863, 874, 881, 888, 899, 901, 904, 907, 910, 912, 913, 921, 923, 931, 932, 937, 940, 946, 964, 970, 973, 989, 998,
        1000]

    test_case2 = [2, 3, 4, 5, 6, 8, 9, 11, 12, 14, 15, 16, 17, 18, 20, 21, 22, 24, 25, 26, 27, 29, 30, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
     45, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 71, 72, 73, 74, 75, 76, 77, 78, 80, 81, 83]


    test_case3 = [i * 100 for i in test_case2]

    for i in test_case3:
        print(happy_number(i), i )

    

if __name__ == "__main__":
    main()