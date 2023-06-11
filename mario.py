# get pyramid height
while True:
    try:
        height = int(input("How high do you wanna go? "))
    except ValueError:
        continue
    if height > 0 and height < 9:
        break


# loop for rows of pyramid
for i in range(0, height, 1):
    for j in range(0, height, 1):
        if (i + j < height - 1):
            print(" ", end="")
        else:
            print("#", end="")
    print()

