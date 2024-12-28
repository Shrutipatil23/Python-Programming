#Cuisine Indentification Using If - Else

IndianCuisine = ["Palak Paneer","Samosa","Biryani","Daal Tadka"]
ItalianCuisine = ["Pasta","Pizza","Caprese Salad","Garlic Bread"]
ChinesseCuisine = ["Manchurian","Soup","Hakka Noodles","Fried Rice"]

Dish = input("Enter The Dish Name : ")

if Dish in IndianCuisine:
    print("Its an Indian Cuisine")
elif Dish in ItalianCuisine:
    print("Its an Italian Cuisine")
elif Dish in ChinesseCuisine:
    print("Its an Chinesse Cuisine")
else :
    print("Based on little Knowledge I don't know which cuisine is",Dish)

