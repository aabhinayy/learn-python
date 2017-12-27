print("Please tell me how manynumbers i should add.")
n = int(input())
#s = n
#x = n
s = 0
while n > 0:
    print("please enter the next number")
    x = int(input())
    s = s + x
    n = n - 1
print(s)