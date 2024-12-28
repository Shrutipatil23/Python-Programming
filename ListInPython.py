#creating List
myList = ["Orange","Apple","Banana","Jackfruit","Avacoda","Jamun"]

#Changing items from particular index
myList[1] = "Pineapple"
print(myList)

#Adding new item to list
myList.append("CustardApple")
print(myList)

#Adding new item in particular index
myList.insert(1,"Papaya")
print(myList)

#Concatenating two list
myList1 =["Tomato","Potato","Cucumber","Spinach"]
myFinalList = myList + myList1
print(myFinalList)

#Counting length of list
print(len(myFinalList))