
# videos
'''
# video 1 filter() function
def starts_with_r(friends):
    return friends.startswith("R")

friends = ["Rolf","Jose","Randy","Anna","Mary","maRy"]
start_with_r = filter(starts_with_r,friends) # arg 1 : function that returns True/False
# start_with_r = filter(lambda friend : friend.startswith("R"), friends)
starts_with_r = (f for f in friends if f.startswith("R"))
print(list(start_with_r))
#print(next(start_with_r))
#print(next(start_with_r))
#print(next(start_with_r))

def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i

'''
'''
# video 2 map() function
friends = ["Rolf","Jose","Randy","Anna","Mary","maRy"]
#friends_lower = map(lambda x : x.lower(), friends)
#friends_lower = [friend.lower() for friend in friends]
friends_lower = (friend.lower() for friend in friends)
print(list(friends_lower))


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data["username"], data["password"])
    
users = [{"username" : "rolf", "password" : "123"},
         {"username" : "teclaskd", "password" : "amals"}]

users = [User.from_dict(user) for user in users]
users = map(User.from_dict, users)
'''

# video 3 any() and all() function
# any  // or
# all // and
friends = [
    {
        "name" : "Rolf",
        "location" : "Washington, D.C."
    },
    {
        "name" : "Anna",
        "location" : "San Francisco"
    },
    {
        "name" : "Charlie",
        "location" : "San Francisco"
    },
    {
        "name" : "Jose",
        "location" : "San Francisco"
    }
]

your_location = input("Where are you right now? ")
friends_nearby = [friend for friend in friends if friend ["location"] == your_location ]

if any(friends_nearby):
    print("You are not alone!")

'''
# 0, 0.0
# None
# [] , (), {}
# False
'''
print(bool(0))
print(all([1,2,3,4,5]))
print(all([0,1,2,3,4,5]))

# video 4 queues 

'''
queue = add elements at the end and remove elements from the start
deque
double-ended queue
.append() => will remvoe at end
.popleft() => will add at start

stack = add and remove from the same end

.appendleft()
.pop()

'''
from collections import Counter

device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 16.0]

temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.5])

print(Counter({"hello" : 5, "hi" : 3})["hi"])

my_dict = {"hello" : 5}

from collections import defaultdict

coworkers = [("Rolf","MIT"),("Jen","Oxford"),("Rolf", "Cambridge"),("Charlie","Manchester")]

#alma_maters = {}

#for coworker,place in coworkers:
#    if coworker not in alma_maters:
#        alma_maters[coworker] = []
#    alma_maters[coworker].append(place)
alma_maters = defaultdict(list)

for coworker, place in coworkers:
    alma_maters[coworker].append(place)

alma_maters.default_factory = int

print(alma_maters["Rolf"])
print(alma_maters["Anne"])
    

# video 5 some interesting python collections

my_company = "Teclado"

coworkers = ["Jen", "Li", "Charlie", "Rhys"]
other_coworkers = [("Rolf","Apple Inc."),("Anne", "Google")]

coworker_companies = defaultdict(lambda: my_company)

for person, company in other_coworkers:
    coworker_companies[person] = company

print(coworker_companies[coworker[0]])
print(coworker_companies["Rolf"])

from collections import OrderedDict

o  = OrderedDict()
o["Rolf"] = 6
o["Jose"] = 12
o["Jen"] = 3

print(o)

o.move_to_end("Rolf")
print(o)
o.move_to_end("Jen", last=False)
print(o)

o.popitem()
print(o)

from collections import namedtuple

account = ("checking", 1850.90)

print(account[0]) # name
print(account[1]) # balance

Account = namedtuple("Account", ["name", "balance"])

account = Account("checking", balance = 1850.90)

accountNamedTuple = Account(*account)
print(accountNamedTuple._asdict()["balance"])
print(account.name)
print(account)

from collections import deque

friends = deque(("Rolf", "Charlie", "Jen", "Anna"))
friends.append("Jose")
friends.appendleft("Anthony")

print(friends)

friends.pop()
friends.popleft()

print(friends)

# video 6 timezones

'''
there are a lot of timezones
some countries have many
some very large countries only have one
normally the difference between timezones is 1hr
sometimes it's 15 min, 30 min, or 45 min

2018-02-11 10:;34 in UK/London (GMT)
2018-02-11 11:34 in Spain/Madrid (CET)
2018-02-11 02:34 in US/San Francisco (PST)
2018-02-11 18:34 in China/Shanghai (CST)

utc => coordinated universal time

a date & time object in python does not know about timezones is called "naive"

one that does is called "aware"

'''
from datetime import datetime
print(datetime.now())

from datetime import datetime, timezone
print(datetime.now(timezone.utc))


# video 7 dates and time in python

from datetime import datetime, timezone, timedelta

print(datetime.now()) # naive 
print(datetime.now(timezone.utc))

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)

print(today)
print(tomorrow)

print(today.strftime("%d-%m-%Y %H:%M:%S")) # string format ime

#user_date = input("Enter the date in YYYY-MM-DD format: ")
#user_date = datetime.strptime(user_date, "%Y-%m-%d") # striing parse time
#print(user_date)

# video 8 timing your code with python
import time

def powers(limit):
    return [(x ** 2) for x in range(limit)]

#print(powers(5))

start = time.time()
powers(50000000)
end = time.time()

print(end - start)

def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)

measure_runtime(lambda: powers(5000000))

import timeit

print(timeit.timeit("[x ** 2 for x in range(10)]"))
print(timeit.timeit("list(map(lambda x: x**2, range(10)))"))


# video 9 regular expression

'''
regular expressions are a language
not a programming language
it has syntax and keywords
we use it to express what we want

a1 a3 a9 a5 a4
a followed by a number, followed by a space
a1 a3 a9 a4 a4(the entire string)

Jose, Rolf, Charlie, Adam
characters, followed by a comma, followed by a space

http://google.com
https://www.facebook.com
https://www.twitter.com
https://udemy.com
https://tecladocode.com
characters, followed by a newline
http,sometimes followed by s, followed by ://, 
sometimes followed by www, followed by characters, followed by .com

jose@tecladocode.com
rolf@google.com
char.lie@twitter.com
anna@gmail.com
jen45@icloud.com
someone_is_awesome@example.net
a combination of letters, numbers, periods, underscores followed by @, 
followed by character(seems only letters), followed by ., followed by character com,net,me

"Getting" regex is a matter of seeing the patterns
and being able to express them using the language

four most important components
1. .    anything - letter,numbers,symbols... but not newlines // .*
2. +    one or more of
3. *    zero or more of
4. ?    zero or one of

[abc]+
[a-z]
[A-z]+ => ASCII character code 
[A-z\.]+@[A-z\.]+

[A-z\.]+@[A-z]+\.(com|me)
'''

# video 10 regex examples


# video 11 regex in python

import re

email = "jose@tecladocode.com"
# expression = "[a-z]+"
expression = "[a-z\.]+"

matches = re.findall(expression, email)
print(matches)

name = matches[0]
# domain = f"{matches[1]}.{matches[2]}"
domain = matches[1]

print(name)
print(domain)

email = "jose@tecladocode.com"
parts = email.split("@")

name = parts[0]
domain = parts[1]
print(name)
print(domain)


import re

price = "Price: $189.50"
# expression = ""
# expression = "Price: \$189.50"
expression = "Price: \$(189.50)"

matches = re.search(expression, price)
print(matches.group(0)) # entire match
print(matches.group(1)) # first thing in brackets

price_number = float(matches.group(1))
print(price_number)


import re

price = "Price: $18,649.50"
# expression = ""
# expression = "Price: \$189.50"
expression = "Price: \$([0-9,]*\.[0-9]*)"

matches = re.search(expression, price)
print(matches.group(0)) # entire match
print(matches.group(1)) # first thing in brackets

price_without_comma = matches.group(1).replace(",", "")

price_number = float(price_without_comma)
print(price_number)

'''
import re
print(re.split('\W+', 'Hello, hello, hello.'))

n = re.ASCII

import re
sentence = 'we are humans'
matched = re.match(r'(.*) (.*?) (.*)', sentence)
print(matched.groups())

import re
sentence = 'horses are fast'
regex = re.compile('(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
matched = re.search(regex, sentence)
print(matched.groupdict())
'''

# 1

import re

def find_max_number(input_user):
    numbers = re.findall(r"\d+", input_user)

    if not numbers:
        return "No Password"
    
    numbers = list(map(int,numbers))

    return max(numbers)
    
input_user = input()

print(find_max_number(input_user))

# 2

import re

def check_pattern(input_user):

    vowels = set("aeiou")

    words = re.findall(r"\b\w+\b", input_user)

    for word in words:
        word_set = set(word)

        if vowels.issubset(word_set):
            return "Accepted"
        
    else:
        return "Not Accepted"
    
input_user = input().strip().lower().replace(" ","")

print(check_pattern(input_user))

# 3

import re

def check_spam_call(input_user):

    pattern = r"^\+91-\d{10}$"

    if re.match(pattern, input_user):
            return "Not a Spam Call"   
    else:
        return "Spam Call"
    
input_user = input().strip()

print(check_spam_call(input_user))

# 4
import re

def encrypt_string(first_word, second_word):
    first_word = re.sub(r'[^a-zA-Z]', '', first_word)
    second_word = re.sub(r'[^a-zA-Z]', '', second_word)

    len1 = len(first_word)
    len2 = len(second_word)
    encrypted_str = []

    for i in range(max(len1,len2)):
        if i < len1:
            encrypted_str.append(first_word[i])
        if i < len2:
            encrypted_str.append(second_word[len2-1-i])

    return "".join(encrypted_str)


first_word = input().strip()
second_word = input().strip()

print(encrypt_string(first_word, second_word))

# 5
# PAN contains ten-digits in which first five characters are letters, next four numerals, 
# last character is a letter and all characters in PAN number is always uppercase.

import re

def check_PAN(input_user):
    pattern = r"^[A-Z]{5}\d{4}[A-Z]$"

    if re.match(pattern, input_user):
                     
        return "Valid PAN Number"  
     
    else:

        return "Invalid PAN Number"


input_user = input().strip()

print(check_PAN(input_user))

# i Assess

# 1













