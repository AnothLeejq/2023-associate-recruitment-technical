# -*- coding: utf-8 -*-
N = int(input())
shop = input().split(' ')
M = int(input())
request = input().split(' ')
result = "Yes"
#No enough T-shirts
if N<M:
    result = "No"
else:
    shop_new,request_new = [],[]
    
    for t in shop:
        if t == "M":
            shop_new.append(0)
        if "L" in t:
            shop_new.append(len(t))
        if "S" in t:
            shop_new.append((-1)*(len(t)))
    for t in request:
        if t == "M":
            request_new.append(0)
        if "L" in t:
            request_new.append(len(t))
        if "S" in t:
            request_new.append((-1)*(len(t)))
    
    shop_new.sort()
    request_new.sort()
    #assume we never need the smallest (N-M) T-shirts
    while N > M:
        shop_new.remove(shop_new[0])
        N-=1
    
    for i in range(M):
        if request_new[i] > shop_new[i]:
            result = "No"
            break
        
print(result)

