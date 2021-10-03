#function to do operations
def operations(left: int,middle: str, right: int):
    #checks for the operations
    if middle=='+':
        print(left + right)
    if middle=='-':
        print(left - right)
    if middle=='/':
        print(left / right)
    if middle=='*':
        print(left * right)
#gets input rom the user             
first=int(input("enter first numner:"))
second=int(input("enter second numner:"))
operation=str(input("enter operation:"))
#calls the operation function
operations(first ,operation ,second)
