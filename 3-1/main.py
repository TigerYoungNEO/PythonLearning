# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#3-1
def right_justify(s):
    i=0
    while(i<70-len(s)):
        print(' ',end='')
        i=i+1
    print(s)


s=input()
right_justify(s)

#3-2
def do_twice(f, a):
    f(a)
    f(a)

def print_spam(spam):
    print(spam)

#do_twice(print_spam)
def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice,'spam')

def do_four(f,b):
    do_twice(f,b)
    do_twice(f,b)

do_four(print_spam,'Lkl&zbq&pp yyds')

#3-3
def draw4_4():
    #i=j=0
    for i in range(0,4):
        for j in range(0,4):
            print('#',end='')
        print('')
draw4_4()