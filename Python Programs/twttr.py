def main():
    text = input("Input: ")
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        text = text.replace(vowel, "")
    print("Output:", text)

main()