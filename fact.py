
#1
def f1(x):
    a = 2
    return x * a

def f2(x):
    return x + 3


def f3(x):
   return f2(f1(x + 5))


#print(f3(2))

#2

# call stack - LIFO - Last In First Out

# FIFO - First in First out


#3
# 1 * 2 * 3 * 4 * 5 ...

def fact(n):
    fc = 1;
    for i in range(1, n + 1):
        fc = fc * i
        print("i=%i fc=%i" % (i, fc))
    return fc

print("fact: %i" % (fact(3)))


#4
def r_fact(n):
    if n > 1:
        return n * r_fact(n - 1)
    else:
        return n

    
print("r_fact: %s" %  r_fact(3))    
