# video 1

import matplotlib.pyplot as plt # type: ignore
plt.style.use("classic")
fig = plt.figure()
ax = plt.axes()

plt.style.available

file_path = open("Medals.csv","rt")
content = file_path.readlines()
print(content)