import sys

word = []
for i in range(int(sys.stdin.readline())):
    word.append(sys.stdin.readline().strip())

word = list(set(word))
word_list = []

for i in word:
    word_list.append((len(i), i))

word_list.sort()

for len_word, i in word_list:
    sys.stdout.write('%s\n' % i)