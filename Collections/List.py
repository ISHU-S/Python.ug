list1=["python","linux","158","623","Computing","Windows"]
list2=[17,80,95,30,62]
print("List1 elements are:",list1)
print("List2 elements are:",list2)
print("1.DataType\n2.Length\n3.Append\n4.Extend\n5.Insertion\n6.Remove\n7.Reverse\n8.Maximum Elements\n9.Minimum Element\n10.Sort\n11.Count\n12.Indexing\n13.Concatenation\n14.Multiply\n15.Clear\n16.Pop")
n = int(input("Press any number:"))
if(n ==1):
 print("The data type is:",type(list1))
 print("The data type is:",type(list2))
elif(n==2):
   print("Total length of list1 is",len(list1))
   print("Total length of list2 is",len(list2))
elif(n==3):
   list1.append(70)
   print("After appending the elements are:",list1)
elif(n==4):
   list1.extend([8,"scale"])
   print("After extending the elements are:",list1)
elif(n==5):
   list1.insert(3,"webex")
   print("After inserting the elements are:",list1)
elif(n==6):
   list1.remove('python')
   print("After removing the items are:",list1)
elif(n==7):
   list2.reverse()
   print("After reversing the elements are",list2)
elif(n==8):
   print("The maximum element is",max(list2))
elif(n==9):
   print("The minimum element is",min(list2))
elif(n==10):
   list2.sort()
   print("After sorting the elements are",list2)
elif(n==11):
   print(list2.count(17))
elif(n==12):
   print(list1.index("linux"))
elif(n==13):
   print("Concatenation of elements:",list1+list2)
elif(n==14):
   print("The total elements are:",list2*2)
elif(n==15):
   list2.clear()
   print("After clearing the list:",list2)
elif(n==16):
   list1.pop(3)
   print("After popping:",list1)
else:
 print("Enter valid number")




	
	
	
