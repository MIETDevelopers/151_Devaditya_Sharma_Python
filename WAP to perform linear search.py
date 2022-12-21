array = [2,20,56,51,39]
n = int(input("Enter the number you want to search"))
for i in range (0,len(array)):
    if (array[i] == n ):
        print ("index of the Required number is",i)
        break