
import math

# goal is to calculate for first matrix
# right now, all I need to do is collect first 
# 100 values, take first 2 and last 2, output 
# some matrix with correct values

# sample on docs btw

# load data
with open("data", 'r') as file:
    data = file.read()
    file.close()

parsed = [tuple(map(float, x.split())) for x in data.split('\n')]
print(parsed[0])
datasize = len(parsed)

# now we have a parsed list of coordinate values
# create matrix - X
X = [[1.0, parsed[i][1], parsed[i][1]**2, parsed[i][0]**3] for i in range(datasize)]


# output :)
for i in range(2):
    print(" ".join([str(int(X[i][j]*100000) / 100000) for j in range(1,4)]))

print("...              ...")

for i in range(datasize-2, datasize):
    print(" ".join([str(int(X[i][j]*100000) / 100000) for j in range(1,4)]))

