bill = int(input("how much is the bill: "))

sum = 0

i = 0

while True:

    coin = int(input("give the coin: "))

    if coin != 1 and coin !=2 and coin !=5 and coin !=10:
        print("only give coins that are 1 2 5 10: ")

        continue

    sum = sum + coin

    if sum > bill:
        print("the chnage is: ", sum - bill)

        break

    elif sum - bill ==0:
        print("we have got the amount thank you")

        break

    else:
         print("recived",i+1 ,"coin")

         i = i + 1

         print("the current amount is", sum )

if sum - bill <0:       
        print("there is not enough money please add more")