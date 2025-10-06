print("sum of N Number")
print("---------------")
a=int(input("Enter the Starting Number:"))
b=int(input("Enter the Ending Number:"))
c=int(input("Enter the Difference:"))
print("Result")
print("-------")
print("Series")
count=0
sum=0
for i in range(a,b+1,c):
    print("+",+i)
    sum=sum+i;
    count=c;
print("sum value:",sum)
print("count value:",count)
