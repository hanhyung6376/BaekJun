a = int(input())
b = int(input())

print(a*(b%10))
print(a*(int((b%100)/10)))
print(a*(int(b/100)))
print(a*b)