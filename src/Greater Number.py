x = int(input())
y = int(input())
n = x - y
if n < 0:
    print str(x) + " is less than " + str(y)
elif n > 0:
    print str(x) + " is greater than " + str(y)
elif n == 0:
    print str(x) + " is epual to " + str(y)
