import random
x=0
i = int(raw_input("\nWhich one do you need? (1 = coin, 2 = dice):"))
while x==0:
        if i==1:
                y = random.randint(1, 2)
                if y == 1:
                        print "heads"
                if y == 2:
                        print "tails"
                        x=1
        if i==2:
                z = random.randint(1, 6)
                print (z)
                x=1
