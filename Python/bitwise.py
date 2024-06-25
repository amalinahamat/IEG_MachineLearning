# how to represent binary numbers in python
# you can use 0b followed by the binary number
# however it is still an integer
# syahmi
# by adding 0b python start reading it as one one one
# instead of one hundred and eleven
owner_permission = 0b111
#print(owner_permission)

filepermission = 0b111101001
# now owner can read , write and execute
# group can read and execute
# others can execute only

# in data science/ machine learning , when you were given
# categorical data,you must convert them to numbers
# which machine can understand
# this itself called "feature engineering"
# gender representation 01 for female 10 for male
# race representation 1000 fro malay, 0100 for chinese

# this bit extraction can be using bitwise and operator

mask = 0b000111000
#print((filepermission & mask) >> 3) # we manage to get group permission over the file
#print("{0:b}".format((filepermission & mask) >> 3))
#print("{0:b}".format(filepermission & mask))
#print(bin(filepermission & mask))


# in order to perform bit extraction we use bitwise & operator
# we are interested in 4,5,6 bits only
# original data             0b111101001     and
# our mask                  0b000111000
# 4,5,6, bits extracted     0b000101000 (above + below)
# shift it to right 3 times  0b000000101 >> 3
# >> 3 => shift to the right 3 times
# << 3 => shift to the left 3 times

# original data             0b111101001     or
# our mask                  0b000111000
# 4,5,6, bits extracted     0b111111001 (above + below)
# The or operator is used to set a specific bit to 1
# please remember there is no way to set a specific bit to 0 using or operator
# Or operator is also used in extracting region of interest in a image
print(bin(filepermission | mask))
print((filepermission or mask) >> 3)
print(filepermission)

# original data             0b111101001     xor
# our mask                  0b000111000
# 4,5,6, bits extracted     0b111010001 (above + below)
# xor is used for encryption and decryptions

message = 0b01001010 # my content "J"
key = 0b00101100 # encryption key ","
encrypted_message = message ^ key
print(bin(encrypted_message))

decrypt_message = encrypted_message ^ key
print(bin(decrypt_message))

#public and private key


# 1st complement
given_number = 5
# 5          => 0101
# 1st compliment is nothing but reverse the 1 and 0. 1 becomes 0 and 0 becomes 1
print(~given_number) # ~ => 1st complement

# 2nd compliment => 1st compliment + 1
print(~given_number + 1) # we can convert any positive number to negative number by using second comliment

# we can also just used - symbol
print(~given_number)     # ~ => 1st complement
print(~given_number + 1) # ~ + 1 => 2nd compliment
print(-given_number)     # - => unary negative
print(+given_number)     # + => unary positive

# hexadecimal number 
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
hexadecimalnumber = 0xF
print(hexadecimalnumber)
print(hex(hexadecimalnumber))

# octal
# 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20
# 0, 1, 2, 3, 4, 5, 6, 7,  8,  9, 10, 11, 12, 13, 14, 15, 16
octalnumber = 0O10
print(octalnumber)
print(oct(octalnumber))

