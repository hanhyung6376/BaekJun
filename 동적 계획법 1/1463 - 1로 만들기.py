num = int(input())
num_cnt = [0] * (num+1)


for i in range(2, len(num_cnt)):
  num_cnt[i] = 1 + num_cnt[i-1]
  if i % 3 == 0 and num_cnt[i] >  num_cnt[i//3] + 1:
    num_cnt[i] = 1 + num_cnt[i//3]
  elif i % 2 == 0 and num_cnt[i] > num_cnt[i//2] + 1:
    num_cnt[i] = 1 + num_cnt[i//2]


print(num_cnt[num])