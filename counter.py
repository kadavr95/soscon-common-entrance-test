def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

n=int(input())
arr=input().split(" ")
if len(arr)!=n:
    print("Oops, you don't have as much numbers as it should be")
d=int(input())
counter=0
for i in arr:
    if sum_digits(int(i))%d == 0:
        counter+=1
print(counter)