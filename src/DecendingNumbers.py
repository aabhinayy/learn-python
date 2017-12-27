x = int(input())
y = int(input())
z = int(input())
if x > y:
    if y > z:
        myList = x, y, z
        print myList
    if z > y:
        myList = x, z, y
        print myList
if x < y:
    if x > z:
        myList = y, x, z
        print myList
    if x < z:
        myList = y, z, x
        print myList
if z > x:
    if x > y:
        myList = z, x, y
        print myList
    if x < y:
        myList = z, y, x
        print myList