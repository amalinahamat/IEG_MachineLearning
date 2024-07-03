# 1 
# A pangram is a sentence using every letter of the alphabet at least once. It is case insensitive, 
# so it doesn't matter if a letter is lower-case (e.g. k) or upper-case (e.g. K).
# For this exercise, a sentence is a pangram if it contains each of the 26 letters in the English alphabet.
# Example: The quick brown fox jumps over the lazy dog.
# Your task is to figure out if a sentence is a pangram.

sentences = input("Write a sentences\n").strip()
sentences = sentences.lower()
sentences = sentences.replace(" ", "")
sentences = sentences.replace(".", "")
sentences = sentences.replace(",", "")
# or
# sentences = sentences.lower().replace(" ", "").replace(".", "").replace(",", "")
#print(sentences)

alphabets = {"a","b", "c", "d", "e", "f", "g",
             "h","i", "j", "k", "l", "m", "n",
             "o","p", "q", "r", "s", "t", "u",
             "v","w", "x", "y", "z" }

list_char = set()

for char in sentences:
    #print(char)
    list_char.add(char)

print()
print(f"list alphabet from alphabet list:\n{sorted(alphabets)}")
print(f"list alphabet from input_user:\n{sorted(list_char)}")
print()

if alphabets <= list_char:
    print("The sentences is a PANGRAM")
else:
    print("The sentences is NOT PANGRAM")

# 2
# n isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, 
# however spaces and hyphens are allowed to appear multiple times.
# Examples of isograms:
# lumberjacks background downstream six-year-old
# The word isograms, however, is not an isogram, because the s repeats.
# Your task is to figure out if the user input is isogram

word = input("Enter a word or phrase: ").strip()
word = word.replace("-","")
word = word.replace(".","")
word = word.replace(",","")
word = word.replace(" ","")

char_set = set()
char_repeated = []
for char in word:
    if char in char_set:
        if char not in char_repeated:
            char_repeated.append(char)      
    else: 
        char_set.add(char)

if char_repeated:
    print(f"'{word}' is not an isogram as {char_repeated} repeated")

else:
    print(f"'{word}' is an isogram")


        

