tpl = (1, 2, 0, "a", "b", "c")
print(tpl[1])
tpl2 = (0,) + tpl
print(tpl2)
print(tpl * 2)
print("b" in tpl)
a, b = "a", "b"
print(a, b)
print(cmp(tpl, tpl2))
print(list(tpl))
print(tpl[:4])
print(len(tpl))
print(max(tpl))
print(min(tpl))
