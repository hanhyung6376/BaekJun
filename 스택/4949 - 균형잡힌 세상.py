def check(msg):
    stack = []
    for i in msg:
        if i in '([':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return 0
        elif i ==']':
            if len(stack) == 0 or stack.pop() != '[':
                return 0
    if len(stack) == 0:
        return 1
    else:
        return 0

msg = []
content = ''
user = ''
while 1:
   user += input()
   if user == '.':
       break
   if user[-1] == '.':
       msg.append(user)
       user = ''

a = check(msg)
for i in msg:
    a = check(i)
    if a == 1:
        print('yes')
    else:
        print('no')