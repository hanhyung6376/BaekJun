word = input().upper()
word_list = list(set(word))
word_cnt = []
for i in word_list:
    cnt = word.count(i)
    word_cnt.append(cnt)

if (word_cnt.count(max(word_cnt)) >= 2):
    print("?")
else:
    print(word_list[word_cnt.index(max(word_cnt))])

