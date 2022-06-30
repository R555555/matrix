def minnum() :
    numbers = [34, 65, 98, 43, 95, 94, 23]
    minmumber = 1000000
    for num in numbers :
        if num < minmumber :
            minmumber = num
        print("number", minmumber, num)
    print('min number is : ', minmumber)

minnum()
