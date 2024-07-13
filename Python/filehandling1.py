import json

try:
    with open('fruitsdictionary.json') as filehandler:
        data = json.load(filehandler) # data is the list of dictinary
    for product in data:
        print(product["product"])
        print(product["quantity"])
        print(product["price"])
except Exception as e:
    print("Something went wrong")