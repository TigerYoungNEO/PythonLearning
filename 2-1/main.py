# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#2-1
r=input("Please enter the r of the circle:")
V= int(r) **3*math.pi*4/3
print(V)

#2-2
n=input("Please enter the number of the book:  ")
n=int(n)
if(n>1):
    V1 = 24.95*n + 3 + 0.75*(n-1)
else:
    V1 = 24.95+3
print(V1)
