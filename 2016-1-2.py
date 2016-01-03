#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
name = "杨佰"
name_bytes = name.encode("utf-8")
name_str = name_bytes.decode("utf-8")

print(name_bytes, len(name_bytes), name_str, len(name))

print("72 / 85 = %.2f%%" % (72/86))

list1 = [1, 2, 3]
tuple1 = (1, 2)
print(list1)

sum = 0;

for i in range(1, 101):
    sum += i
print(sum)

set1 = ([1, 2, 3], [1, [2, 3]])
set1[1][1] = 3
print(set1)

print(hex(12))
'''

def test(x, y, *, z=1,  **d):
    print(x, y, z, d)

test(1, 2, z=3,**{"name": "yangbai"})

def hannuota(n, a, b, c):
    if n == 1:
        print(a, "->", c)
    else:
        hannuota(n-1, a, c, b)
        print(a, '->', c)
        hannuota(n-1, b, a, c)

hannuota(2, "A", "B", "C")