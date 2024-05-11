print("Area of a traingle can be found using 2 ways ")
n = float(input("if lenght and height of a triangle is given select 1 : /n else if measure of all 3 sides are given select 2 : "))
if(n==1):
    p= float(input(("enter the lenght :")))
    q= float(input(("eneter the height : ")))
    area= .5*p*q
    print(" the area of the traingle is :",area)
if(n==2):
    print("enter all the values : ")
    p=float(input("1: "))
    q=float(input("2 : "))
    r=float(input("3 : "))
    s=(p+q+r)/2
    area=(s*(s-p)*(s-q)*(s-r)) ** 0.5 
    print("the area of the traingle is :",area) 
if(n!=(1 or 2)):
    print("selected invalid option ")