l1=[5,19,30,"list","P","operations"]
l2=[5,2,7,5]
print("List1 elements are:",l1)
print("List2 elements are:",l2)
print("1.DataType\n2.Length\n3.Append\n4.Extend\n5.Insertion\n6.Remove\n7.Reverse\n8.Maximum Elements\n9.Minimum Element\n10.Sort\n11.Count\n12.Indexing\n13.Concatenation\n14.Multiply\n15.Clear\n16.Pop")
n = int(input("Press any number:"))
if(n ==1):
print("The date type is:",type(l1))
print("The date type is:",type(l2))
elif(n==2):
print("Total length of list1 is",len(l1))
print("Total length of list2 is",len(l2))
elif(n==3):
l1.append(20)
print("After appending the elements are:",l1)
elif(n==4):
l1.extend([8,"scale"])
print("After extending the elements are:",l1)
elif(n==5):
l1.insert(3,"linux")
print("After inserting the elements are:",l1)
elif(n==6):
l1.remove('P')
print("After removing the items are:",l1)
elif(n==7):
l2.reverse()
print("After reversing the elements are:",l2)
elif(n==8):
print("The maximum element is",max(l2))
elif(n==9):
print("The minimum element is",min(l2))
elif(n==10):
l2.sort()
print("After sorting the elements are",l2)
elif(n==11):
print(l2.count(5))
elif(n==12):
print(l1.index("list"))
elif(n==13):
print("Concatenation of elements:",l1+l2)
elif(n==14):
print("The total elements are:",l2*3)
elif(n==15):
l2.clear()
print("After clearing the list:",l2)
elif(n==16):
l1.pop(3)
print("After popping:",l1)
else:
print("Enter valid number")
