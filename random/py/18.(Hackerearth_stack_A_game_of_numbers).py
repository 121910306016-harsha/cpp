#https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/a-game-of-numbers-1-5d3a8cb3/

#Python Solution
arr = []
n = int(input())
a, b, s1, s2 = dict(), dict(), [], []
for i in range(n):
    arr.append(int(input()))
    x = arr[i]
    while(s1!=[] and s1[-1][0]<x):
        a[s1.pop()[1]] = i
    s1.append((x, i))
    while(s2!=[] and s2[-1][0]>x):
        b[s2.pop()[1]] = i
    s2.append((x, i))
for i in range(n):
    if i in a:
        if a[i] in b:
            print(arr[b[a[i]]], end = " ")
        else:
            print(-1, end = " ")
    else:
        print(-1, end = " ")
print()




"""
In this solution we take 2 stacks and 2 dictionaries to get the output generated by two functions F and G.

For function F: 

Basically, for each index i we need to nd the next greater element( say present at index j ) to the right of it such that mod(i-j) is minimum. 

For this we use the stack "s1" and dictionary "a". We push an element into the stack "S1" whenever it is lesser than the top element of the stack. 

Else, we pop elements from the stack and keep storing the result in dict "a" until the stack is empty or (stack->top >the compared element). 

For function G: 

Basically, for each index i we need to nd the next smaller element( say present at index j ) to the right of it such that mod(i-j) is minimum. 

For this we use the stack "s2" and dictionary "b". We push an element into the stack "S2" whenever it is greater than the top element of the stack. 

Else, we pop elements from the stack and keep storing the result in dict "b" until the stack is empty or (stack->top < the compared element). 

"""

