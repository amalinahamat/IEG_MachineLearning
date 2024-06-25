# python dictionary is also called JSON in other programming language
# (JSON) javascript object notation
# XML Data
# Dictionary is also using {}
# The data is ordered
# The data is indexed by key (not by number)
# Every single data is associated with a key
# For example firstname is a key and Peter is the data  
# Key cannot be duplicated . Data can be duplicated
# It is modifiable

foreigner = {
    "firstname" : "Peter",
    "lastname" : "Parker",
    "passportnumber" : "E4837589",
    "incometaxnumber" : "SG834934",
    "pcbamount" : 892,
    "lastmonth" : 5,
    "lastyear" : 2024,                
    "previousmonth" : [(4, 2024, 891), (3, 2024, 895), (2, 2024, 893), (1, 2024, 892)],
    "Addresses" : {
        "office" : {
            "street" : "2484, Kampung Teluk Pelong Padang Midin",
            "passcodedistrict" : "24100, Kuala Terengganu",
            "state" : "Terengganu"
        },
        "home" : {
            "street" : "International Islamic University Malaysia",
            "passcodedistrict" : "53100, Wilayah Persekutuan",
            "state" : "Kuala Lumpur"
        }
    }

}

print("First name: ",foreigner["firstname"])
print("Last Name: ", foreigner["lastname"])
print("Passport Number: ", foreigner["passportnumber"])
print("PCB Amount: ", foreigner["pcbamount"])
print("Income Tax Number: ", foreigner["incometaxnumber"])
print("Last Month: ", foreigner["lastmonth"])
print("Last Year: ", foreigner["lastyear"])

print()

# for item in foreigner["previousmonth"]:
# item will hold a tuple (4,2023, 892)
# however we know tuple is auto explode
# as long as we have 3 variables we can explode and hold the 3 values

for month,year,amount in foreigner["previousmonth"]:
    print(f"Transaction: {month}-{year} RM{amount}")

print()

officeAddress = foreigner["Addresses"]["office"]
homeAddress = foreigner["Addresses"]["home"]
print(f"Street : {officeAddress["street"]} \nPasscode and District : {officeAddress["passcodedistrict"]} \nState: {officeAddress["state"]}" )
print()
print(f"Street : {homeAddress["street"]} \nPasscode and District : {homeAddress["passcodedistrict"]} \nState: {homeAddress["state"]}" )

print()
# you can access the street directly as follows
print(foreigner["Addresses"]["office"]["street"])

# sometimes we may not know the keys
print(foreigner.keys())
for key in foreigner.keys():
    print(foreigner[key])

print(foreigner.keys())
for ke in foreigner.keys():
    # isinstance is a built in function to determine the type of variable
    if(isinstance(foreigner[ke],list)):
       for item in foreigner[ke]:
           print(item)
    
    else:
        print(foreigner[ke])


# when you use the method items you will get the key, value
for key, value in foreigner.items():
    print(key,value)

# how can i modify the dictionary
# since the key car does not exists in the dictionary it gets added automatically
foreigner["car"] = {
    "brand" : "MCLAUREN",
    "model" : "GT",
    "carplate" : "AMA317"
}


foreigner["salary"] = 4890
print(foreigner)

# if i want to modify the salary
# since the salary is already there, it modifies/updates the existing salary
foreigner["salary"] = 5550

print(foreigner)

print()
# delete
foreigner.pop("Addresses")
print(foreigner)

    

