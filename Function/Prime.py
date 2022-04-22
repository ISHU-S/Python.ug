def prime_checker(n):
  c=0
  if n!=1:
    for i in range (1,n+1):
      if(n%i==0):
        c=c+1
  if(c==2):
    print("it is a prime number")
  else:
    print("it is not a prime number")

n=int(input("enter a number : "))
prime_checker(n)
	
