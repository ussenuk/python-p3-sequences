#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        fib = []
    elif length == 1:
        fib = [0]
    elif length == 2:
        fib = [0, 1]
    else:
        fib =[0, 1]
        for i in range (2, length):
            fib.append(fib[i-1] + fib[i-2])
    print(fib)
    return fib
    
