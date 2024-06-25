# set uses {}
# set is modifiable (add, edit and delete)
# set is unordered (the items does not retain its position)
# set is not indexed (Do not have 0, 1, 2, 3, 4, .....)
# set does not allows duplicates

# in python this is the first time we are using {}
x = {10, 20, 30, 10, 40, 50, 20, 60, 70}
print(x)
# what do you observe
# 1. numbers are not in the same order as it was created
# 2. duplicate numbers are missing

# selection and indexing
# since set is not indexed you cannot retrieve the value using [] syntax
# to retrieve the items inside the set
# only way is to use fro loop
for i in x:
    print(i)

# modifiable
fruits = {"apple", "orange", "mango"}
print(fruits)
fruits.add("durian") # add a random place
print(fruits)

# to delete an item in the set
fruits.remove("orange")
print(fruits)
# pop => randomly removes an item in the set
fruits.pop()
print(fruits)

# if you want to update an item
# 1. remove the item
# 2. add the new item

fruits = ["apple", "orange", "apple", "mango", "banana", "apple"]
uniquefruits = set(fruits)
print(uniquefruits)

overseafruits = {"apple", "orange","mango", "banana", "grapes"}
localfruit = {"durian", "rambutan", "cempedak", "banana", "mangosteen"}
print(overseafruits.union(localfruit))
print(overseafruits.intersection(localfruit))
print(overseafruits.difference(localfruit))
print(localfruit.difference(overseafruits))

favouritefruits = {"durian", "rambutan", "mangosteen"}
print(favouritefruits.issubset(localfruit)) # true
print(favouritefruits.issuperset(favouritefruits)) #true
print(favouritefruits.isdisjoint(overseafruits)) #true


emailcontent = """A shocking proportion of email traffic—about according to 2022 data—is spam. 
Much of that spam is purposely crafted for fraudulent purposes, to compromise communication, and gain access to data, networks, or funds.
Many spam filtering programs identify spam messages before they reach human readers. 
Many more seem obviously fishy and are easy to delete when they reach your inbox. 
But what about those outlier messages that are hard for both software and people to detect?"""

words = emailcontent.split()
print(len(words))

uniqueword = set(words)
print(len(uniqueword))

print(uniqueword)

cleanword = []
for word in words:
    # word is instance of string class or word is a string object
    # remove is a method inside the word object
    # remove takes 2 arguments first argument is to find second argument 
    word = word.replace(",","")
    word = word.replace(".","")
    word = word.lower()
    cleanword.append(word)

uniqueword = set(cleanword)
print(len(uniqueword))
print(uniqueword)

commonword = {"is", "or", "of", "so", "by", "how", "when", "it", "on", 
              "the", "into", "a", "to", "are", "what", "be", "i", "you", "more", "and", "can", "an"}

uniqueword = uniqueword.difference(commonword)
print(len(uniqueword))
print(uniqueword)

# here we try to demonstrate the features of set data structures
# however we have another library called NLTK this have many features
# required for NLP (natural language processing)

scam = {"pishing", "trick", "security", "criminals", "spam"}

howmanyscamword = uniqueword.intersection(scam)
print(len(howmanyscamword))

