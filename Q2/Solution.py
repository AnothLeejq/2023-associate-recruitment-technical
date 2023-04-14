# -*- coding: utf-8 -*-
N = int(input())
inputs = []
for i in range(N):
    inputs.append(input())
allValid = True
errorCodes = []
for record in inputs:
    message = record.split(' ')
    if len(message) > 2:
        allValid = False
        errorCodes.append(message[2])

if allValid is True:
    print("Yes")
else:
    print("No")
    for err in errorCodes:
        print(err,end=" ")
