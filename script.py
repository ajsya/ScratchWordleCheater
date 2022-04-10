print("Welcome to Shark's Wordle on Scratch word finder script.")
word_length = input("How long is the word you're looking for?")

if word_length == '5':

    my_file = open("5.txt", "r")
    data = my_file.read()

    words = data.split("\n")
    #print(words)
    my_file.close()

else:
    print(f"Currently, words with {word_length} characters aren't supported.")
    exit()

char = input("What's a character in your word? (You may enter more then one if they coincide)").upper()
str_match = [s for s in words if char in s]
print("Here are some possible matches...")
print(str_match)
while True:
    print("Let's narrow the search...")
    char = input("What's a character in your word? (You may enter more then one if they coincide)").upper()
    str_match = [s for s in str_match if char in s]
    print("Here are some possible matches...")
    print(str_match)
