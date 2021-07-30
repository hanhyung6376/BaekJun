num = int(input())
group=0
for i in range (num):
    word = input()
    cnt = 0
    for j in range(0, len(word)):
        a=word[word.index(word[j]):word.rindex(word[j])+1]
        if(len(set(a))==1):
            cnt+=1
    if(cnt==len(word)):
        group+=1
print(group)
