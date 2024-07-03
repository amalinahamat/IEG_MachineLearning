
# videos

# video 1 filter() function
def starts_with_r(friends):
    return friends.startswith("R")

friends = ["Rolf","Jose","Randy","Anna","Mary","maRy"]
start_with_r = filter(starts_with_r,friends) # arg 1 : function that returns True/False
print(next(start_with_r))
print(next(start_with_r))
print(next(start_with_r))


'''
# video 2 map() function
 
# video 3 any() and all() function

# video 4 queues 

# video 5 some interesting python collections

# video 6 timezones

# video 7 dates and time in python

# video 8 timing your code with python

# video 9 regular expression

# video 10 regex examples

# video 11 regex in python
'''

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