# Python 3 program to find factorial of given number
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1);
 
num = int(input("Enter a Number");
print("Factorial of",num,"is",
factorial(num))
