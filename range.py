def range_check(num,range1,range2):
    if num in range(range1,range2+1):
        print(num,"is in the given range")
    else:
        print(num,"is not in the given range")
range1 = int(input("Enter the first range: "))
range2 = int(input("Enter the last range: "))
num = int(input("Enter a number to check: "))
range_check(num,range1,range2)




