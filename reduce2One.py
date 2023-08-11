def reduce2One(arr):
    arr.sort()  
    
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] > 1:
            return False  
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if reduce2One(a):
        print("YES")
    else:
        print("NO")
