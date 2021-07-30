def chess(x, y, back):
    cnt = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if (arr[i][j] == back):
                cnt += 1
                if (arr[i][j] == 'W'):
                    back = 'B'
                else:
                    back = 'W'
            elif (arr[i][j] != back):
                back = arr[i][j]
        if(back == 'B'):
            back = 'W'
        else:
            back = 'B'
    return cnt

x, y = map(int, input().split())
arr = [list(map(str,input())) for _ in range(x)]
result = 64
for i in range(0, x-8+1):
    for j in range(0, y-8+1):
        sum1 = chess(i,j, 'W')
        sum2 = chess(i,j, 'B')
        sum = min(sum1, sum2)
        if(result > sum):
            result = sum

print(result)