my_set={"January", "Febuary","March"}

for month in my_set:
    print(month)
    
my_set.add("April")  
print(my_set)  
my_set.remove("January")
print(my_set)

my_list=["January", "Febuary","March","January"]
my_list.remove("January")
print(my_list)