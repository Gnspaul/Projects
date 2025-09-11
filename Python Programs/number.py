def getInt(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            pass
        

def main():
    x = getInt("What's x? ")
    print(f"x is {x}")

main()