name = "David"
batch = 101
fee = 12345.5551515651
# traditionally how we do this
inputstring = "hello" + name + ",welcome to python class" + str(batch)
print(inputstring)

# special string called f string
inputstring = f"hello {name}, welcome to python class {batch}"
print(inputstring)

# how much of space required
inputstring = f"Heloo {name:40s}, wwelcome to python class {batch}"

# align David to center
inputstring = f"Hello {name:^40s}, welcome to python class {batch}"
print(inputstring)

# align David to right
inputstring = f"hello {name:>40s}, welcome to python class {batch}"
print(inputstring)

# You can also provide padding characters
inputstring = f"Hello {name:*>40s}, welocome to python class {batch}"
print(inputstring)

# You can also provide padding characters
inputstring = f"Hello {name:^15}, welocome to python class {batch}"
print(inputstring)

# Truncate to 3 characters
inputstring = f"hello {name:.3}, welcome to python class {batch}"
print(inputstring)

# Let us focus on decimal let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:10d} in KL"
print(inputstring)

# Let us focus on decimal let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:<10d} in KL"
print(inputstring)

# Let us focus on decimal let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:10d} in KL for RM{fee:10.2f}"
print(inputstring)

# Let us focus on decimal let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:10d} in KL for RM{fee:.2f}"
print(inputstring)

# Let us focus on decimal let us take 10 space
inputstring = f"Hello {name:.3}, welcome to python class {batch:10d} in KL for RM{fee:,.2f}"
print(inputstring)

# binary for batch
inputstring = f"Hello {name}, welcome to python class {batch:b} in KL"
print(inputstring)

# octagon for batch
inputstring = f"Hello {name}, welcome to python class {batch:o} in KL"
print(inputstring)

# hexagon for batch
inputstring = f"Hello {name}, welcome to python class {batch:x} in KL"
print(inputstring)


