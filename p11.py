def drawl(row,co):
    for i in range(0,co):
        if(i%2==0):
            print(" ___","   ",end="")
    print(end="\n")
    for j in range(row):
            print("/"+"   "+"\\"+"___",end="")
    print(end="\n")
    for z in range(row):
            print("\\"+"___"+"/"+"   ",end="")
    for i in range(row-1):
        print(end="\n")
        for j in range(row):
            print("/" + "   " + "\\" + "___", end="")
        print(end="\n")
        for z in range(row):
            print("\\" + "___" + "/" + "   ", end="")

drawl(3,5)