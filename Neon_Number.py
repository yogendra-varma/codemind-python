n=int(input())
i=n*n
sum=0
while(i):
    sum=sum+i%10
    i=i//10
if(n==sum):
    print("Neon Number")
else:
    print("Not Neon Number")