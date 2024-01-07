my_set={"January", "February","March"}

for month in my_set:
    print(month)
    
my_set.add("April")  
print(my_set)  
my_set.remove("January")
my_set.add("May")
print(my_set)

my_list=["January", "February","March","January"]
my_list.remove("January")
print(my_list)