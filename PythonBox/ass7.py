# 1
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


        

