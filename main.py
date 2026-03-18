#1-m
students = {"Ali": 85, "vali": 90, "Hasan": 78, "Husan" : 92}
print(students)

max_ball = max(students.values())

for v, k in enumerate(students):
    if max_ball == students[k]:
        print(k)
        break

#2-m
sales = {"apples": 50, "oranges": 75, "bananas": 30, "pears": 45}
print(sales)

s = (sales.values())

for v, k in enumerate(sales):
    sum += s
    print(s)


#3-m
grades = {"Math": 80, "Physics": 75, "Chemistry": 85, "Biology": 90}
print(grades)

x = (grades.values())

for v , k in enumerate(grades):
    if v > 75:
        print(f"Hammasidan katta bo'lgan son {v}")

# 4-m
inventory = {"pen": 10, "pencil": 20, "notebook": 15, "eraser": 5}
print(inventory)

max_ball = max(inventory.values())

for v, k in enumerate(inventory):
    if max_ball == inventory[k]:
        print(k)
        break

#5-m
products = {"A": 100, "B": 200, "C": 150, "D": 250}
print(products)

summa = sum(products.values())
print(summa)

s = summa // sum(products.values())
print(s)

#6-m
d = dict()
print(d)

d["x"] = 10
d["y"] = 20
d["z"] = 30
print(d)

#7-m
d = dict(name="Ali", age=20)
print(d)

d["c"] = 15
d["d"] = 20
print(d)


#8-m
d = dict(name="Ali", age=20)
print(d)

print(d)

#9-m
d = {}

d1 = int(input("3-ta Son kiriting"))
print(d)

#10-m
d1 = {"x":1, "y":2}
d2 = {"y":3, "z":4}

print(d1 , d2)

#11-m
grades = {"Math": 80, "Physics": 90, "Chemistry": 85}
print(grades)

s = (grades.keys())
print(s)



#12-m
grades = {"Math": 80, "Physics": 90, "Chemistry": 85}
print(grades)

s = (grades.values())
print(s)


#13-m
grades = {"Math": 80, "Physics": 90, "Chemistry": 85}
print(grades)

s = (grades.items())

print(s)
