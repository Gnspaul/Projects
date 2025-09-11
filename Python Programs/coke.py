def main():
    cokePrice = 50
    while cokePrice > 0:
        print("Amount Due:", cokePrice)
        userInput = int(input("Insert Coin: "))
        if userInput == 25 or userInput == 10 or userInput == 5:
            cokePrice -= userInput
        else:
            print("This machine only accepts quarters, dimes, and nickels.")
        if cokePrice == 0:
            print("Enjoy!")
            break
        elif cokePrice < 0:
            print("Change Due:", abs(cokePrice))

main()