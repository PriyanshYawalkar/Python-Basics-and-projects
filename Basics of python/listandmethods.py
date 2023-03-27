l1 = [3, 5, 234, 234, 234, "ggg"]

print(type(l1))
print(l1)
l1.remove("ggg")
l1.append(56) # using this we add anything into the list.
l1.extend([44, 54, 65, 66]) # using this we can extend over list with new values.
print(l1)