lst = [1, 2, 3, "a", "b", "c"]
print(lst[1])
print(lst[1:3])
lst[1] = "two"
print(lst[1])
lst.append("d")
print(lst)
del lst[1]
print(lst)
lst.remove("d")
print(lst)
print(lst + ["yeah", "yes"])
print(lst * 2)
print(3 in lst)
print(lst[1])
print(lst[-1])
print(lst[3:])
print(max(lst) + " " + str(min(lst)))
lst2 = [4, 5, 6]
lst.extend(lst2)
print(lst)
lst.insert(3, lst2)
print(lst[3][0])
lst.pop()
print(lst)
