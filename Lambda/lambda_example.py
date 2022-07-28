def topla(x):
    return x+10

toplaLambda = lambda x: x+10

print(topla(5))
print(toplaLambda(5))

print((lambda x: (x+3)*5 / 2)(3))


print()

def carp(n):
    return lambda a: a * n      # iç içe 2 fonksiyon // nested functions

carpan = carp(2)
print(carpan(11),end='\n\n')
carpan = carp(4)
print(carpan(11),end="\n\n")

print(carp(2)(12))  # n = 2 , a = 12 