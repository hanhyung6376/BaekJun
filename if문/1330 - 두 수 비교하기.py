while(1):
    a, b = map(int, input().split())
    if (a>=-10000 and a<=10000) and (b>=-10000 and b<=10000):
        break;

if a>b:
    print(">")
elif a<b:
    print("<")
elif a==b:
    print("==")