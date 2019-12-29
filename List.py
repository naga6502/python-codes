names = ["mohan", "arun", "balu", "ravi"]

print("Names list = ", names)

names.append("siva")
names.append("siva")
print("after append = ", names)

names.insert(2, "teja")
print("after insert = ", names)
names.sort()
print("after sort = ", names)

print(names.count("siva"))
names.reverse()
print("after reverse = ", names)

print(names[0:3])

print(len(names))

for i in range(len(names)):
    print(names[i])


names.clear()
print("after clear = ", names)



