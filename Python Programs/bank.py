greeting = input("Greeting: ")
greeting.strip()

if ("Hello" in greeting):
    print("$0")
elif greeting.startswith("h") or greeting.startswith("H"):
    print("$20")
else:
    print("$100")
