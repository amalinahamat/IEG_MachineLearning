import pickle

try:
    filehandler =  open('fruitsdictionary.txt', 'rt')
    data = pickle.load(filehandler)
    for product in data:
        print(product)
except Exception as e:
    print("Something went wrong")