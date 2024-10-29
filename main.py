T = int(input())

list = 0

for i in range(T):
    A, B= map(int, input().split())
    list.append(A+ B)

for l in list:
    print(list)
    
