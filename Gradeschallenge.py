g = input("What's your grade? ")

x = int(g)

# make sure it's for 40 or greater
if (x < 40):
    print("Fail")

#for (x > 40):
  #if (x % 3) or (x % 4) or (x % 8) or (x % 9):
    #x = round((x + 2.5)/ 5.0) * 5.0

elif (40 < x < 80):
  print("Pass")

elif (x > 80):
  print("Distinction")


