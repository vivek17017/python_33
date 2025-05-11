"""

#Q1
def check(n):
    if n%2==0:
        return "even"
    else:
        return "not even"
a=check(7)
print(a)


#Q2
def greater(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
x=greater(4,6,2)
print("greater no is",x)


#Q3
def prime(a):
    for e in range(2,a):
        if a%e==0:
            return "not a prime number"
    else:
        if a<=1:
            return "not a prime number"
        else:
            return "prime number"
x=prime(0)
print(x)





def leap(a):
    if a%4==0:
        if a%100==0:
            if a%400==0:
                return "leap year"
            else:
                return "not a leap year"
        else:
            return "leap year"
    else:
        return "not a leap year"


x=leap(2022)
print(x)



def fac(n):
    a=1
    for e in range(1,n+1):
        a=e*a
    return a
b=fac(5)
print("fac is",b)



def isEven(n):
    return n%2==0
print(isEven(7))


def check(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
         

def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

print(isPrime(4))


"""
def isLeapYear(year):
    return year%400==0 if year%100==0 else year%4==0

print(isLeapYear(2001))


