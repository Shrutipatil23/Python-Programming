def sum(exp):
    total = 0
    for i in exp:
     total = total + i
    return total

list_one = [2300 , 3000 , 2000]
list_second = [1500 , 8000 ,1400]


list_one_total = sum(list_one)
list_second_total = sum(list_second)

print("List one total = ",list_one_total)
print("List second total = ",list_second_total)