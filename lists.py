print('Lists')

list01 = []
count = 0

while count < 5:
    count += 1
    list01.append('FFFF' + str(count))
    print(list01)


# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)