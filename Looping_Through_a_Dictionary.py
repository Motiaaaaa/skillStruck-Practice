# measurement = {"length": 10, "width": 5, "depth": 3}

# for num in measurement.values():
# 	print(num)


# amanda_value = int(input("How many in Amanda's group?"))
# jane_value = int(input("How many in Jane's group?"))

# group = {
# 	"Fred" : 12,
# 	"Jackson" : 15,
# 	"Sophie" : 20,
# 	"Amanda" : amanda_value,
# 	"Jane" : jane_value,
# }

# total = 0

# for num in group.values():
# 	total += num
	
# print(total)



first = int(input("Pick a first number"))
second = int(input("Pick a second number"))			
group = {
	3 : 10,
	5 : 3,
	10 : 6,
	4 : 30,
	first : second
}

total = 0
for key,value in group.items():
	total += key*value

print(total)