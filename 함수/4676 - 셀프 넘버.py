def selfNumber(a):
    cnt = 0
    SN = [0]*a
    for i in range(a):
        SN[i] = 0
    for i in range (0 ,a):
        num=0
        array = []
        array = str(i)
        num += i
        for j in range (0, len(array)):
            num += int(array[j])
        if(num < a):
            SN[num] = 1
    for i in range (0, a):
        if(SN[i] != 1):
            print(i)
