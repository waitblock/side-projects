'''
Supported Phones:

iPhone 2G
iPhone 3G
iPhone 4
iPhone 5
iPhone 6
iPhone 7
iPhone 8
iPhone X
iPhone 11
'''

answer = input("How many cameras does your phone have? ")
if answer == "two":
    answer = input("Does your phone have a slow-motion front facing camera? ")
    if answer == "yes":
        print("iPhone 11")
    elif answer == "no":
        print("iPhone X")
elif answer == "one":
    answer = input("Does your phone have Touch ID? ")
    if answer == "yes":
        answer = input("Does your phone have a headphone jack? ")
        if answer == "yes":
            answer = input("Does your phone have 3D Touch? ")
            if answer == "yes":
                print("iPhone 6")
            elif answer == "no":
                print("iPhone SE")
        if answer == "no":
            answer = input("Does your phone support wireless charging? ")
            if answer == "yes":
                print("iPhone 8")
            elif answer == "no":
                print("iPhone 7")
    if answer == "no":
        answer = input("Does your phone have LTE support? ")
        if answer == "yes":
            print("iPhone 5")
        elif answer == "no":
            answer = input("Does your phone support video recording? ")
            if answer == "yes":
                print("iPhone 4")
            elif answer == "no":
                answer = int(input("What year was your phone released? "))
                if answer == 2007:
                    print("iPhone 2G")
                elif answer == 2008:
                    print("iPhone 3G")
