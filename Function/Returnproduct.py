def product_or_sum(a,b):
  sum=0
  rem=0
  product=a*b
  if(product > 500):
    print("product of ",a," and ",b," is grater than 500 ")
    print("product is : ",product)
    while(product>0):
      rem = product % 10
      sum=sum+rem
      product=product//10
    print("sum of their product is ",sum)
  else:
    print("product is : ",product)

n1=int(input("enter n1 value : "))
n2=int(input("enter n2 value : "))
product_or_sum(n1,n2)
